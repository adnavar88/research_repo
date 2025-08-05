
from langchain.prompts import PromptTemplate

insight_prompt = PromptTemplate(
    input_variables=["query", "docs"],
    template="""
You are a helpful UX research assistant. A user asked: "{query}".

These are the related research documents:

{docs}

Summarize the key insights, themes, and user quotes. Cite document IDs.
"""
)
