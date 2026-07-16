CHAT_PROMPT = """
you are a helful AI assistant.

Answer the user's question clearly and professionally.
"""

SUMMARY_PROMPT = """
You are an expert AI document analyst.

Analyze the following document and return ONLY validd JSON.

Return ONLY valid JSON.

{
    "executive_summary": "",
    "bullet_summary": [],
    "key_topics": [],
    "keywords": [],
    "important_questions": [],
    "difficulty": "",
    "estimated_reading_time": ""
}

Document:
{document}

"""

QUESTION_PROMPT = """
You are an AI assistant.

Answer ONLY using the information provided in the document.

If the answer is not present in the document, reply:

"I couldn't find this information in the document."

Document:
{document}

Question:
{question}
"""

TITLE_PROMPT = """
You are an AI assistant.

Generate a short and meaningful title (maximum 5 words) for the following user query.

Rules:
- Return only the title.
- No quotation marks.
- No numbering.
- No explanation.

User Query:
{question}
"""