# ruff: noqa: T201
import logging
from collections.abc import Callable

from agent_boilerplate.features.calculator import test_calculator
from agent_boilerplate.features.chatbot import test_chatbot
from agent_boilerplate.features.structured_output import test_structured_output

logging.basicConfig(level=logging.INFO)

_options: list[tuple[str, Callable[[], None]]] = [
    ("聊天机器人 (流式输出)", test_chatbot),
    ("电影推荐 (结构化输出)", test_structured_output),
    ("计算器 (工具调用)", test_calculator),
]


def main() -> None:
    print("Select an option by number:")
    for idx, option in enumerate(_options, start=1):
        print(f"{idx}. {option[0]}")

    try:
        choice = input("Enter choice: ").strip()
    except EOFError:
        print("No input received. Exiting.")
        return

    if not choice.isdigit():
        print("Invalid selection.")
        return

    idx = int(choice)
    if idx < 1 or idx > len(_options):
        print("Invalid selection.")
        return

    func = _options[idx - 1][1]
    func()


if __name__ == "__main__":
    main()
