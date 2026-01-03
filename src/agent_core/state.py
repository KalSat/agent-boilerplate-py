from langgraph.graph import MessagesState


class MyMessagesState(MessagesState):
    llm_calls: int
