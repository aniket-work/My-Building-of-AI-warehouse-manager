import tempfile
import os
import pandas as pd
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.docling import DoclingReader
from llama_index.core.node_parser import MarkdownNodeParser

def process_document(temp_dir: str, file_path: str):
    reader = DoclingReader()
    loader = SimpleDirectoryReader(
        input_dir=temp_dir,
        file_extractor={".xlsx": reader},
    )
    docs = loader.load_data()
    node_parser = MarkdownNodeParser()
    index = VectorStoreIndex.from_documents(
        documents=docs,
        transformations=[node_parser],
        show_progress=True
    )
    return index