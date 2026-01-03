from typing import Callable

from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from agent_core.config import settings
from agent_core.state import MyMessagesState
from agent_core.tools import tools


def build_agent_node() -> Callable[..., MyMessagesState]:
    """
    Initializes the LLM and binds tools to it, returning a Runnable that represents the agent node.
    """
    print(f"--- Initializing Model: {settings.default_model} ---")

    llm = ChatOpenAI(
        model=settings.default_model,
        api_key=settings.siliconflow_api_key,
        base_url=settings.base_url,
        temperature=0.7
    )
    # Bind tools immediately here
    llm_with_tools: Runnable[LanguageModelInput, AIMessage] = llm.bind_tools(tools)

    # Define the Agent Node
    # Logic: Call the LLM with the current conversation state
    def call_model(state: MyMessagesState) -> MyMessagesState:
        return {
            "messages": [llm_with_tools.invoke(state["messages"])],
            "llm_calls": state.get('llm_calls', 0) + 1,
        }

    return call_model


def build_graph(agent_node: Callable[..., MyMessagesState]) -> CompiledStateGraph:
    """
    Constructs the StateGraph logic (Nodes & Edges).
    Returns a compiled application ready to run.
    :param agent_node: The agent node callable.
    """

    # noinspection PyTypeChecker
    workflow = StateGraph(MyMessagesState)

    # Define the Tool Node
    tool_node = ToolNode(tools)

    # Add Nodes
    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tool_node)

    # Add Edges
    workflow.add_edge(START, "agent")

    # Conditional Edge: Agent -> Tools OR End
    workflow.add_conditional_edges("agent", tools_condition)

    # Normal Edge: Tools -> Agent (Loop back)
    workflow.add_edge("tools", "agent")

    return workflow.compile()


def run_execution_loop(agent_graph: CompiledStateGraph, query: str) -> None:
    """
    Handles the I/O: sends the query to the app and prints the stream.
    """
    print(f"\n>>> User Query: {query}\n")

    # Explicit Type Casting for MyPy strict mode
    input_state: MyMessagesState = {
        "messages": [HumanMessage(content=query)],
        "llm_calls": 0,
    }

    try:
        # noinspection PyTypeChecker
        output_state = agent_graph.invoke(input_state)
        for m in output_state["messages"]:
            m.pretty_print()
        print("==============================")

    except Exception as e:
        print(f"Error during execution: {e}")


def save_graph_image(agent_graph: CompiledStateGraph) -> None:
    """
    Saves the graph visualization as an image file.
    """
    try:
        graph_image = agent_graph.get_graph(xray=True).draw_mermaid_png()
        with open("agent_graph.png", "wb") as f:
            f.write(graph_image)
        print("Graph image saved as agent_graph.png")
    except Exception as e:
        print("Failed to save graph image.")


def main() -> None:
    """
    Orchestrator function.
    """
    # 1. Setup Resources
    agent_node = build_agent_node()

    # 2. Build Logic
    agent_graph = build_graph(agent_node)

    save_graph_image(agent_graph)

    # 3. Execute
    user_query = "请计算123乘以456。"
    run_execution_loop(agent_graph, user_query)


if __name__ == "__main__":
    main()
