from dataclasses import dataclass

from langchain.agents import AgentState, create_agent
from langgraph.graph.state import CompiledStateGraph

from agent_core.calculator.tools import tools
from agent_core.llms import qwen2_5_instruct_llm


class CustomState(AgentState):
    user_preferences: dict


@dataclass
class CustomContext:
    user_name: str
    user_role: str


SYSTEM_PROMPT = """
You are a highly intelligent calculator agent.
You have access to a variety of mathematical tools to help you perform calculations
 accurately and efficiently.
When a user provides you with a mathematical problem,
 carefully analyze the problem to determine the best approach for solving it.
 Use the available tools as needed to carry out calculations,
 ensuring that each step is clear and logical.
"""


def create_calculator_agent() -> CompiledStateGraph:
    # noinspection PyTypeChecker
    return create_agent(
        model=qwen2_5_instruct_llm,
        system_prompt=SYSTEM_PROMPT.strip(),
        tools=tools,
        state_schema=CustomState,
        context_schema=CustomContext,  # type: ignore[arg-type]
    )
