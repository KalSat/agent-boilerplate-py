from langchain_core.messages import HumanMessage

from agent_core.llms import structured_llm


def test_structured_output() -> None:
    user_query = "请为我推荐一部电影"
    response = structured_llm.invoke([HumanMessage(content=user_query)])
    print(f"Structured Output Response: \n{response}")
