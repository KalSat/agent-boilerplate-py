from typing import Callable

from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import AIMessage
from langchain_core.runnables import Runnable
from langgraph.constants import START
from langgraph.graph import StateGraph, MessagesState
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from agent_core.models import qwen2_5_instruct_llm
from agent_core.tools import tools


class MyMessagesState(MessagesState):
    llm_calls: int


def build_calculator_graph() -> CompiledStateGraph:
    """
    Constructs the StateGraph logic (Nodes & Edges).
    Returns a compiled application ready to run.
    """

    # noinspection PyTypeChecker
    workflow = StateGraph(MyMessagesState)

    # Define the Tool Node
    tool_node = ToolNode(tools)

    # Add Nodes
    workflow.add_node("agent", _build_calculator_agent_node())
    workflow.add_node("tools", tool_node)

    # Add Edges
    workflow.add_edge(START, "agent")

    # Conditional Edge: Agent -> Tools OR End
    workflow.add_conditional_edges("agent", tools_condition)

    # Normal Edge: Tools -> Agent (Loop back)
    workflow.add_edge("tools", "agent")

    return workflow.compile()


def _build_calculator_agent_node() -> Callable[..., MyMessagesState]:
    """
    Initializes the LLM and binds tools to it, returning a Runnable that represents the agent node.
    """

    # Bind tools immediately here
    llm_with_tools: Runnable[LanguageModelInput, AIMessage] = qwen2_5_instruct_llm.bind_tools(tools)

    # Define the Agent Node
    # Logic: Call the LLM with the current conversation state
    def call_model(state: MyMessagesState) -> MyMessagesState:
        ai_message = llm_with_tools.invoke(state["messages"])
        return {
            "messages": [ai_message],
            "llm_calls": state.get('llm_calls', 0) + 1,
        }

    return call_model
