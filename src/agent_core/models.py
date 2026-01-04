from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from agent_core.config import settings

print(f"--- Initializing Model: {settings.qwen2_5_7b_instruct} ---")
qwen2_5_instruct_llm: BaseChatModel = ChatOpenAI(
    model=settings.qwen2_5_7b_instruct,
    api_key=settings.siliconflow_api_key,
    base_url=settings.base_url,
    temperature=0.7
)
