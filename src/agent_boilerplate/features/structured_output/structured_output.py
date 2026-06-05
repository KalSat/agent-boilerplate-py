import logging
from typing import cast

from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import HumanMessage
from langchain_core.runnables import Runnable

from agent_boilerplate.features.structured_output.models import Movie
from agent_boilerplate.shared.llms import qwen2_5_instruct_llm

_logger = logging.getLogger(__name__)

_structured_llm = cast(
    Runnable[LanguageModelInput, Movie],
    qwen2_5_instruct_llm.with_structured_output(Movie),
)


def test_structured_output() -> None:
    user_query = "请为我推荐一部电影"
    response = _structured_llm.invoke([HumanMessage(content=user_query)])
    _logger.info(f"Structured Output Response: \n{response}")
