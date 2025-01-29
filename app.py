import os
import tempfile

import pandas as pd
import streamlit as st
import gc
import uuid
from config import PAGE_CONFIG, init_models
from prompts import QA_TEMPLATE
from styles import CUSTOM_CSS
from utils import process_document

# Initialize app
st.set_page_config(**PAGE_CONFIG)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
if "id" not in st.session_state:
    st.session_state.id = uuid.uuid4()
    st.session_state.file_cache = {}
    st.session_state.messages = []

# Header
st.markdown("""
    <div class="enterprise-header">
        <div class="logo-container">🏭</div>
        <div class="header-title">AI Warehouse Manager</div>
        <div class="header-subtitle">AI Powered Warehouse Analysis System</div>
    </div>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### Document Processing Center")

    uploaded_file = st.file_uploader(
        "Upload Excel Document",
        type=["xlsx", "xls"],
        help="Supported formats: .xlsx, .xls"
    )

    if uploaded_file:
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                file_path = os.path.join(temp_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getvalue())

                file_key = f"{st.session_state.id}-{uploaded_file.name}"

                with st.spinner("🔄 Processing document..."):
                    if file_key not in st.session_state.file_cache:
                        index = process_document(temp_dir, file_path)
                        query_engine = index.as_query_engine(streaming=True)
                        query_engine.update_prompts(
                            {"response_synthesizer:text_qa_template": QA_TEMPLATE}
                        )
                        st.session_state.file_cache[file_key] = query_engine

                st.success("✅ Document processed successfully!")
                st.markdown("### Document Preview")
                df = pd.read_excel(uploaded_file)
                st.dataframe(df, use_container_width=True, height=400)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.stop()

with col2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### Interactive Analysis Portal")

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            icon_class = "user-icon" if message["role"] == "user" else "assistant-icon"
            message_class = "user-message" if message["role"] == "user" else "assistant-message"
            st.markdown(f"""
                <div class='{icon_class} chat-message {message_class}'>
                    {message["content"]}
                </div>
            """, unsafe_allow_html=True)

    # Chat input
    if prompt := st.chat_input("Ask a question about your document..."):
        if not uploaded_file:
            st.warning("Please upload a document first")
        else:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(f"""
                    <div class='user-icon chat-message user-message'>
                        {prompt}
                    </div>
                """, unsafe_allow_html=True)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                streaming_response = query_engine.query(prompt)
                for chunk in streaming_response.response_gen:
                    full_response += chunk
                    message_placeholder.markdown(f"""
                        <div class='assistant-icon chat-message assistant-message'>
                            {full_response}▌
                        </div>
                    """, unsafe_allow_html=True)

# Footer
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🔄 Reset Conversation", type="primary"):
        st.session_state.messages = []
        st.session_state.context = None
        gc.collect()
        st.rerun()