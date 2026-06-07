from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph

from agent_boilerplate.features.calculator.prompts import SYSTEM_PROMPT
from agent_boilerplate.features.calculator.tools import tools
from agent_boilerplate.shared.llms import small_fast_llm


def create_calculator_agent() -> CompiledStateGraph:
    # noinspection PyTypeChecker
    return create_agent(
        # The model to use - supports "provider:model" format
        model=small_fast_llm,
        # System prompt defining agent behavior
        system_prompt=SYSTEM_PROMPT.strip(),
        # Tools available to the agent
        tools=tools,
        # Optional: Add middleware for advanced customization
        # middleware=[
        #     summarization_middleware(
        #         model=small_fast_llm,
        #         trigger={"tokens": 4000},
        #     ),
        #     human_in_the_loop_middleware(
        #         interrupt_on={
        #             "sensitive_tool": {"allowed_decisions": ["approve", "reject"]},
        #         },
        #     ),
        # ],
    )
