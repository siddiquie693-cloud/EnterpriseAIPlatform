from django.conf import settings
from groq import APIError

from ai.prompts import (
    CHAT_PROMPT,
    SUMMARY_PROMPT,
    QUESTION_PROMPT,

)

from ai.exceptions import LLMServiceError
from ai.logger import logger
from ai.services.client import client

class LLMService:
    """
    Service class for interacting with the Groq LLM .
    """

    @staticmethod
    def chat(prompt: str) -> str:
        try:
            logger.info("Sending chat request to Groq")

            response = client.chat.completions.create(
                model=settings.GROQ_MODEL,
                messages=[
                    {
                        "role": "system",
                         "content": CHAT_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                temperature=0.7,
            )
            logger.info("Chat response received successfully")

            return response.choices[0].message.content
        
        except APIError as exc:
            logger.exception("Groq Chat API Error")
            raise LLMServiceError(f"Groq Chat Error: {str(exc)}")
        
        except Exception as exc:
            logger.exception("Unexpected Chat Error")
            raise LLMServiceError(f"Unexpected Error: {str(exc)}")
    
    @staticmethod
    def summarize(text: str) -> str:
        try:
            logger.info("Generating document summary")

            prompt = SUMMARY_PROMPT.format(
                document=text
            )
            response = client.chat.completions.create(
                model=settings.GROQ_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=0.3,
            )
            logger.info("Document summary generated successfully")

            return response.choices[0].message.content
        
        except APIError as exc:
            logger.exception("Groq Summary API Error")
            raise LLMServiceError(f"Groq Summary Error: {str(exc)}")
        
        except Exception as exc:
            logger.exception("Unexpected Summary Error")
            raise LLMServiceError(f"Unexpected Error: {str(exc)}")
    
    @staticmethod
    def answer_question(document: str, question: str) -> str:
        try:
            logger.info("Answering question from document")

            prompt = QUESTION_PROMPT.format(
                document=document,
                question=question,
            )
            response = client.chat.completions.create(
                model=settings.GROQ_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=0.2,
            )
            logger.info("Question answered successfully")

            return response.choices[0].message.content 
        
        except APIError as exc:
            logger.exception("Groq Question Answering API Error")
            raise LLMServiceError(f"Groq Question Answering Error: {str(exc)}")
        
        except Exception as exc:
            logger.exception("Unexpected Question Answering Error")
            raise LLMServiceError(f"Unexpected Error: {str(exc)}")





    
