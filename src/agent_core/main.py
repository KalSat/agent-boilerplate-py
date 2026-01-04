from langchain_core.messages import HumanMessage
from langgraph.graph.state import CompiledStateGraph

from agent_core.agnets import build_calculator_graph, MyMessagesState


def _save_graph_image(agent_graph: CompiledStateGraph) -> None:
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


def _run_execution_loop(agent_graph: CompiledStateGraph, query: str) -> None:
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


def main() -> None:
    """
    Orchestrator function.
    """

    # Build Agent
    agent_graph = build_calculator_graph()

    # _save_graph_image(agent_graph)

    # Execute
    user_query = "请计算123乘以456。"
    _run_execution_loop(agent_graph, user_query)


if __name__ == "__main__":
    main()
