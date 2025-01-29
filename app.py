import gc
import uuid
import pandas as pd
import streamlit as st
from utils.document_processor import process_document
from components.header import render_header
from components.styles import CUSTOM_STYLES
from config.constants import (
    SUPPORTED_FILE_TYPES,
    PREVIEW_HEIGHT,
    SUCCESS_MESSAGE,
    UPLOAD_ERROR_MESSAGE,
    NO_DOCUMENT_WARNING
)

# Page configuration
st.set_page_config(
    page_title="AI Warehouse Manager",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom styles
st.markdown(f"<style>{CUSTOM_STYLES}</style>", unsafe_allow_html=True)

# Initialize session state
if "id" not in st.session_state:
    st.session_state.id = uuid.uuid4()
    st.session_state.file_cache = {}

session_id = st.session_state.id

# Render header
render_header()

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### Document Processing Center")

    uploaded_file = st.file_uploader(
        "Upload Excel Document",
        type=SUPPORTED_FILE_TYPES,
        help="Supported formats: .xlsx, .xls"
    )

    if uploaded_file:
        try:
            file_key = f"{session_id}-{uploaded_file.name}"

            with st.spinner("🔄 Processing document..."):
                if file_key not in st.session_state.get('file_cache', {}):
                    query_engine = process_document(
                        uploaded_file.getvalue(),
                        uploaded_file.name
                    )
                    if query_engine:
                        st.session_state.file_cache[file_key] = query_engine
                    else:
                        st.error(UPLOAD_ERROR_MESSAGE)
                        st.stop()
                else:
                    query_engine = st.session_state.file_cache[file_key]

                st.success(SUCCESS_MESSAGE)

                # Display preview
                st.markdown("### Document Preview")
                df = pd.read_excel(uploaded_file)
                st.dataframe(
                    df,
                    use_container_width=True,
                    height=PREVIEW_HEIGHT
                )

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.stop()

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### Interactive Analysis Portal")

    # Initialize chat
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.context = None

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            icon_class = "user-icon" if message["role"] == "user" else "assistant-icon"
            message_class = "user-message" if message["role"] == "user" else "assistant-message"
            st.markdown(f"""
                <div class='{icon_class} chat-message {message_class}'>
                    {message["content"]}
                </div>
            """, unsafe_allow_html=True)

    # Chat input handling
    if prompt := st.chat_input("Ask a question about your document..."):
        if not uploaded_file:
            st.warning(NO_DOCUMENT_WARNING)
        else:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(f"""
                    <div class='user-icon chat-message user-message'>
                        {prompt}
                    </div>
                """, unsafe_allow_html=True)

            # Add assistant response
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                streaming_response = query_engine.query(prompt)
                for chunk in streaming_response.response_gen:
                    full_response += chunk
                    formatted_response = full_response.replace('\n', '<br>')
                    message_placeholder.markdown(f"""
                        <div class='assistant-icon chat-message assistant-message'>
                            {formatted_response}▌
                        </div>
                    """, unsafe_allow_html=True)

# Footer with reset button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🔄 Reset Conversation", type="primary"):
        st.session_state.messages = []
        st.session_state.context = None
        gc.collect()
        st.rerun()