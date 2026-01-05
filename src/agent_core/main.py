# ruff: noqa: T201
import logging
from collections.abc import Callable

from agent_core.calculator import test_calculator
from agent_core.chatbot import test_chatbot
from agent_core.structured import test_structured_output

logging.basicConfig(level=logging.INFO)

_options: list[Callable[[], None]] = [
    test_calculator,
    test_structured_output,
    test_chatbot,
]


def main() -> None:
    print("Select an option by number:")
    for idx, option in enumerate(_options, start=1):
        print(f"{idx}. {option.__name__}")

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

    func = _options[idx - 1]
    func()


if __name__ == "__main__":
    main()
