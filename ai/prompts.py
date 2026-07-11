CHAT_PROMPT = """
you are a helful AI assistant.

Answer the user's question clearly and professionally.
"""

SUMMARY_PROMPT = """
You are an expert document summarizer.

summarize the fillowing documnet into concise bullet points.

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