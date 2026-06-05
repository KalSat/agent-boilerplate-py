import logging

from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from agent_boilerplate.shared.config import settings

_logger = logging.getLogger(__name__)

_logger.info(f"--- Initializing Model: {settings.model} ---")
base_llm: BaseChatModel = ChatOpenAI(
    model=settings.model,
    api_key=settings.api_key,
    base_url=settings.base_url,
    temperature=0.3,
)

_logger.info(f"--- Initializing Small Fast Model: {settings.small_fast_model} ---")
small_fast_llm: BaseChatModel = ChatOpenAI(
    model=settings.small_fast_model,
    api_key=settings.api_key,
    base_url=settings.base_url,
    temperature=0.3,
    extra_body={"enable_thinking": False},
)
