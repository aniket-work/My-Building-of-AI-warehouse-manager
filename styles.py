CUSTOM_CSS = """
    /* Hide message action icons */
    .stChatMessage [data-testid="StChatMessageActions"] {
        display: none !important;
    }

    /* Hide message avatars */
    .stChatMessage [data-testid="stChatMessageAvatar"] {
        display: none !important;
    }

    /* Global Dark Theme */
    .main {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }

    /* Enterprise Header */
    .enterprise-header {
        text-align: center;
        padding: 4rem 0;
        background: #1a237e;
        margin: -4rem -4rem 2rem -4rem;
    }

    .header-title {
        font-size: 3.5rem !important;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
    }

    .header-subtitle {
        font-size: 1.8rem;
        color: rgba(255, 255, 255, 0.9);
    }

    /* Chat Messages */
    .chat-message {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: #E0E0E0;
    }

    .user-message {
        background-color: #2C3E50;
        margin-left: 2rem;
        border-left: 4px solid #3498DB;
    }

    .assistant-message {
        background-color: #2D2D2D;
        margin-right: 2rem;
        border-right: 4px solid #2ECC71;
    }
"""