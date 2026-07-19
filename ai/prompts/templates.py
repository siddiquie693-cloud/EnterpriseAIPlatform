from langchain_core.prompts import ChatPromptTemplate

SUMMARY_TEMPLATE = ChatPromptTemplate.from_template(
    """
    You are an expert AI document analyst.

    Analyze the following document and produce:

    1. Executive Summary
    2. Bullet Summary
    3. Key Topics
    4. Keywords
    5. Important Questions
    6. Difficulty Level
    7. estimated reading Time

    Document:
    {document}
    """
)

QA_TEMPLATE = ChatPromptTemplate.from_template(
    """
    You are an AI assistant.

    Use ONLY the provided document.

    Document:
    {document}

    Question:
    {question}

    Answer clearly and accurately.
    """
)