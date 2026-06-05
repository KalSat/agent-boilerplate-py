import logging
from pathlib import Path

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState
from langgraph.graph.state import CompiledStateGraph

from agent_boilerplate.features.calculator.agent import create_calculator_agent

_logger = logging.getLogger(__name__)


def _save_graph_image(agent_graph: CompiledStateGraph) -> None:
    """
    Saves the graph visualization as an image file.
    """
    try:
        graph_image = agent_graph.get_graph(xray=True).draw_mermaid_png()
        with Path("agent_graph.png").open("wb") as f:
            f.write(graph_image)
        _logger.info("Graph image saved as agent_graph.png")
    except Exception:
        _logger.error("Failed to save graph image.")


def _run_execution_loop(agent_graph: CompiledStateGraph, query: str) -> None:
    """
    Handles the I/O: sends the query to the app and prints the stream.
    """
    print(f"\n>>> User Query: {query}\n")  # noqa: T201

    input_state = MessagesState(
        messages=[HumanMessage(content=query)],
    )

    try:
        # noinspection PyTypeChecker
        output_state = agent_graph.invoke(input_state)
        for m in output_state["messages"]:
            m.pretty_print()
        print("==============================")  # noqa: T201

    except Exception as e:
        print(f"Error during execution: {e}")  # noqa: T201


def test_calculator() -> None:
    # Build Agent
    # agent_graph = build_calculator_graph()
    agent_graph = create_calculator_agent()

    _save_graph_image(agent_graph)

    # Execute
    user_query = "请计算123×456+800÷2。"  # noqa: RUF001
    _run_execution_loop(agent_graph, user_query)
