# ruff: noqa: T201
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage

from agent_boilerplate.features.chatbot.prompts import PROMPTS
from agent_boilerplate.shared.llms import small_fast_llm


def test_chatbot() -> None:
    print("聊天机器人启动...")
    messages: list[AnyMessage] = [
        SystemMessage(
            content=PROMPTS["friendly"],
        ),
    ]

    print("输入 'exit' 退出对话。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "exit":
            print("聊天机器人已退出。")
            break

        messages.append(HumanMessage(content=user_input))

        print("机器人: \n", end="", flush=True)
        full_reply = ""
        for chunk in small_fast_llm.stream(messages):
            if chunk.content and isinstance(chunk.content, str):
                print(chunk.content, end="", flush=True)
                full_reply += chunk.content

        print("\n" + "-" * 40)

        messages.append(AIMessage(content=full_reply))

        messages = messages[-10:]
