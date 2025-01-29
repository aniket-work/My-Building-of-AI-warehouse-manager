import streamlit as st
import pandas as pd
from config.constants import SUPPORTED_FILE_TYPES, SUCCESS_MESSAGE

def render_document_uploader():
    """Render the document upload interface."""
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### Document Processing Center")

    uploaded_file = st.file_uploader(
        "Upload Excel Document",
        type=SUPPORTED_FILE_TYPES,
        help=f"Supported formats: {', '.join(SUPPORTED_FILE_TYPES)}"
    )

    return uploaded_file

def show_document_preview(file):
    """Show preview of uploaded document."""
    st.success(SUCCESS_MESSAGE)
    st.markdown("### Document Preview")
    df = pd.read_excel(file)
    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )