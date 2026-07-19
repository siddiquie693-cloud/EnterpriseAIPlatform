from langchain_core.output_parsers import StrOutputParser

from ai.prompts.templates import SUMMARY_TEMPLATE
from ai.chains.llm import llm

summary_chain = (
    SUMMARY_TEMPLATE
    | llm
    | StrOutputParser()
)