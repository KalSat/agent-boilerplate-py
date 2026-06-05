# ruff: noqa: T201
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage

from agent_boilerplate.shared.llms import qwen2_5_instruct_llm


def test_chatbot() -> None:
    print("聊天机器人启动...")
    messages: list[AnyMessage] = [
        SystemMessage(
            content="你叫小智，是一名乐于助人的智能助手。请在对话中保持友好、有耐心、温和的语气。",
        ),
    ]

    print("输入 'exit' 退出对话。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "exit":
            print("聊天机器人已退出。")
            break

        messages.append(HumanMessage(content=user_input))

        print("小智: ", end="", flush=True)
        full_reply = ""
        for chunk in qwen2_5_instruct_llm.stream(messages):
            if chunk.content and isinstance(chunk.content, str):
                print(chunk.content, end="", flush=True)
                full_reply += chunk.content

        print("\n" + "-" * 40)

        messages.append(AIMessage(content=full_reply))

        messages = messages[-10:]
