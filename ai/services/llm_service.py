from django.conf import settings
from groq import APIError
import json

from ai.prompts import (
    CHAT_PROMPT,
    SUMMARY_PROMPT,
    QUESTION_PROMPT,
    TITLE_PROMPT,

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
    def summarize(text: str):
        """
        Generate a structured AI summary of a document.
        Return a Python dictionary.
        """
        try:
            logger.info("Generating document summary")

            prompt = SUMMARY_PROMPT.replace(
                "{document}",
                text,
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

            content = response.choices[0].message.content.strip()

            # Remove Markdown code fences if present 
            content = (
                content.replace("```json", "")
                .replace("```", "")
                .strip()
            )

            try:
                return json.loads(content)
        
            except json.JSONDecodeError:
                logger.warning("Groq return invalid JSON. Returing fallback response.")

                return {

                    "executive_summary": content,
                    "bullet_summary": [],
                    "key_topics": [],
                    "keywords": [],
                    "important_questions": [],
                    "difficulty": "Unknown",
                    "estimated_reading_time": "Unknown",
                }
        except APIError as exc:
                
                logger.exception("Groq Summary API Error")
                raise LLMServiceError(f"Groq Summary Error: {str(exc)}")
        except Exception as exc:
                logger.exception("Unexpected Summary Error")
                raise LLMServiceError(f"Unexpected Error: {str(exc)}")
    
    @staticmethod
    def answer_question(document: str, question: str, history=None) -> str:
        try:
            logger.info("Answering question from document")

            prompt = QUESTION_PROMPT.format(
                document=document,
                question=question,
            )

            messages = []

            # System instruction
            messages.append(
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI assistent. "
                        "Use the provided document context and the previous "
                        "conversation to answer naturally."
                    ),
                }
            )

            # Previous conversation 
            if history:
                messages.extend(history)

            # Current question 
            messages.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )    
            response = client.chat.completions.create(
                model=settings.GROQ_MODEL,
                messages=messages,
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
        
    @staticmethod
    def generate_title(question: str) -> str:
        """
        Generate a short AI title for a conversation.
        """
        try:
            logger.info("Generating conversation title")

            prompt = TITLE_PROMPT.format(
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

            logger.info("Conversation title generated successfully")

            return response.choices[0].message.content.strip()

        except APIError as exc:
            logger.exception("Groq Title Generation API Error")
            raise LLMServiceError(f"Groq Title Generation Error: {str(exc)}")

        except Exception as exc:
            logger.exception("Unexpected Title Generation Error")
            raise LLMServiceError(f"Unexpected Error: {str(exc)}")   

    @staticmethod
    def stream_chat(prompt: str):
        """
        Stream chat response from Groq.
        """
        try:
            logger.info("Streaming response from Groq")

            stream = client.chat.completions.create(
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
                stream=True,
            )

            for chunk in stream:
                if (
                    chunk.choices
                    and chunk.choices[0].delta.content
                ):
                    yield chunk.choices[0].delta.content

            logger.info("Streaming completed")
        except APIError as exc:
            logger.exception("Groq Streaming API Error")
            yield f"\nError: {str(exc)}"

        except Exception as exc:
            logger.exception("Unexpected Streaming Error")
            yield f"\nError: {str(exc)}"

    

    @staticmethod
    def summarize_document(document: str):
        """
        Generate structured AI documnet analysis.
        """
        try:
            logger.info("Generating document analysis")

            prompt = SUMMARY_PROMPT.format(
                document=document,
            )

            response = client.chat.completions.create(
                model=settings.GROQ_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert document analyst. "
                        
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                temperature=0.2,
            )

            content = response.choices[0].message.content.strip()

            logger.info("Documnet analysis generated successfully")

            return json.loads(content)

        except json.JSONDecodeError:
            logger.exception("Failed to parse JSON response")

            raise LLMServiceError(
                "LLM return invalid JSON."
            )
        
        except APIError as exc:
            logger.exception("Groq API Error")
            raise LLMServiceError(str(exc))
        
        except Exception as exc:
            logger.exception("Unexpected Error")
            raise LLMServiceError(str(exc))
                






    
