import os
import tempfile
from llama_index.core import Settings, VectorStoreIndex
from llama_index.core import PromptTemplate
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core import SimpleDirectoryReader
from llama_index.readers.docling import DoclingReader
from config.constants import LLM_MODEL, LLM_TIMEOUT, EMBEDDING_MODEL, QA_PROMPT_TEMPLATE


def process_document(file_content, filename):
    """Process uploaded document and create query engine."""
    llm = Ollama(model=LLM_MODEL, request_timeout=LLM_TIMEOUT)
    embed_model = HuggingFaceEmbedding(
        model_name=EMBEDDING_MODEL,
        trust_remote_code=True
    )

    Settings.embed_model = embed_model
    Settings.llm = llm

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, filename)

        with open(file_path, "wb") as f:
            f.write(file_content)

        if os.path.exists(temp_dir):
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

            query_engine = index.as_query_engine(streaming=True)
            qa_prompt_tmpl = PromptTemplate(QA_PROMPT_TEMPLATE)
            query_engine.update_prompts(
                {"response_synthesizer:text_qa_template": qa_prompt_tmpl}
            )

            return query_engine
        return None