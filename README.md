# LangChain Agent Boilerplate

A Python starter template for building agentic applications using **LangChain** and **LangGraph**. This boilerplate provides a clean, feature-organized foundation for building AI agents with tool calling, structured output, and multi-turn conversation support.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
uv sync
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Add your API credentials to `.env`:

```bash
# SiliconFlow API key
SILICONFLOW_API_KEY=your-key-here

# Model name to use (e.g. Qwen/Qwen2.5-7B-Instruct)
QWEN2_5_7B_INSTRUCT=Qwen/Qwen2.5-7B-Instruct

# Optional: override the default base URL
# BASE_URL=https://api.siliconflow.cn/v1
```

### 3. Run the Agent

```bash
# List available tasks
uv run poe --help

# Run the interactive CLI
uv run poe run
```

## 📁 Project Structure

```yaml
src/
└── agent_boilerplate/
    ├── main.py                   # CLI entry point
    ├── features/
    │   ├── __init__.py
    │   ├── calculator/
    │   │   ├── agent.py          # ReAct agent definition
    │   │   ├── calculator.py     # Calculator feature entry point
    │   │   ├── prompts.py        # System prompts and templates
    │   │   └── tools.py          # Tool definitions
    │   ├── chatbot/
    │   │   ├── chatbot.py        # Multi-turn chatbot implementation
    │   │   └── prompts.py        # Chatbot prompts and templates
    │   └── structured_output/
    │       ├── models.py         # Pydantic output models
    │       └── structured_output.py  # Structured output feature entry point
    ├── shared/
    │   ├── config.py             # Pydantic settings (loads from .env)
    │   └── llms.py               # LLM client setup
    └── utils/
        └── time_util.py          # Utility functions
tests/                            # Pytest test suite
```
