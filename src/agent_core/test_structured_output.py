from langchain_core.messages import HumanMessage

from agent_core.models import model_with_structure


def test_structured_output() -> None:
    user_query = "请为我推荐一部电影"
    response = model_with_structure.invoke([HumanMessage(content=user_query)])
    print(f"Structured Output Response: \n{response}")
