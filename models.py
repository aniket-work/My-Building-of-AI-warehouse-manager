from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import json


def initialize_models():
    with open('settings.json') as f:
        settings = json.load(f)

    llm = Ollama(
        model=settings['models']['llm']['name'],
        request_timeout=settings['models']['llm']['request_timeout']
    )

    embed_model = HuggingFaceEmbedding(
        model_name=settings['models']['embedding']['model_name'],
        trust_remote_code=settings['models']['embedding']['trust_remote_code']
    )

    Settings.embed_model = embed_model
    Settings.llm = llm

    return llm, embed_model