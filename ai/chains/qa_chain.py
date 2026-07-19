from langchain_core.output_parsers import StrOutputParser

from ai.prompts.templates import QA_TEMPLATE
from ai.chains.llm import llm

qa_chain = (
    QA_TEMPLATE
    | llm 
    | StrOutputParser()
)