from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

PAGE_CONFIG = {
    "page_title": "AI Warehouse Manager",
    "page_icon": "🏭",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

def init_models():
    llm = Ollama(model="llama3.2:3b", request_timeout=120.0)
    embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-large-en-v1.5",
        trust_remote_code=True
    )
    Settings.embed_model = embed_model
    Settings.llm = llm
    return llm, embed_model