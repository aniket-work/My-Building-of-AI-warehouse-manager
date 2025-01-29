import os
from typing import Dict, List

SUPPORTED_FILE_TYPES: List[str] = ["xlsx", "xls"]
FILE_HELP_TEXT: str = "Supported formats: .xlsx, .xls"

class MessageRoles:
    USER = "user"
    ASSISTANT = "assistant"

class StyleClasses:
    USER_MESSAGE = "user-message"
    ASSISTANT_MESSAGE = "assistant-message"
    CHAT_MESSAGE = "chat-message"