from llama_index.core import PromptTemplate

QA_TEMPLATE = PromptTemplate(
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