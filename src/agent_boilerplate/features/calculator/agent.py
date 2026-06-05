from dataclasses import dataclass

from langchain.agents import AgentState, create_agent
from langgraph.graph.state import CompiledStateGraph

from agent_boilerplate.features.calculator.prompts import SYSTEM_PROMPT
from agent_boilerplate.features.calculator.tools import tools
from agent_boilerplate.shared.llms import qwen2_5_instruct_llm


class CustomState(AgentState):
    user_preferences: dict


@dataclass
class CustomContext:
    user_name: str
    user_role: str


def create_calculator_agent() -> CompiledStateGraph:
    # noinspection PyTypeChecker
    return create_agent(
        model=qwen2_5_instruct_llm,
        system_prompt=SYSTEM_PROMPT.strip(),
        tools=tools,
        state_schema=CustomState,
        context_schema=CustomContext,  # type: ignore[arg-type]
    )
