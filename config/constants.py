import os
from pathlib import Path

# File settings
SUPPORTED_FILE_TYPES = ["xlsx", "xls"]
PREVIEW_HEIGHT = 400

# Messages
SUCCESS_MESSAGE = "✅ Document processed successfully!"
UPLOAD_ERROR_MESSAGE = "❌ Document upload failed. Please try again."
NO_DOCUMENT_WARNING = "Please upload a document first"

# LLM Settings
LLM_MODEL = "llama3.2:3b"
LLM_TIMEOUT = 120.0
EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"

# Prompt Templates
QA_PROMPT_TEMPLATE = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Provide a professional analysis following these guidelines:\n"
    "1. Start with a clear summary\n"
    "2. Use bullet points for key findings\n"
    "3. Include relevant metrics where available\n"
    "4. End with actionable insights\n\n"
    "Query: {query_str}\n"
    "Analysis: "
)