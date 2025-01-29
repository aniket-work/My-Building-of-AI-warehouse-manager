import streamlit as st


class ChatInterface:
    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []
            st.session_state.context = None

    def render_messages(self):
        """Render existing chat messages."""
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                icon_class = "user-icon" if message["role"] == "user" else "assistant-icon"
                message_class = "user-message" if message["role"] == "user" else "assistant-message"
                st.markdown(f"""
                    <div class='{icon_class} chat-message {message_class}'>
                        {message["content"]}
                    </div>
                """, unsafe_allow_html=True)

    def handle_user_input(self, query_engine):
        """Handle user input and generate response."""
        if prompt := st.chat_input("Ask a question about your document..."):
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
                    formatted_response = full_response.replace('\n', '<br>')
                    message_placeholder.markdown(f"""
                        <div class='assistant-icon chat-message assistant-message'>
                            {formatted_response}▌
                        </div>
                    """, unsafe_allow_html=True)