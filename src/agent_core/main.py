from langchain_openai import ChatOpenAI

from agent_core.config import settings


def test_llm_connection() -> None:
    """
    测试 LLM 连接并打印回复
    """
    print(f"--- 正在初始化模型: {settings.default_model} ---")

    # 1. 初始化 LLM
    # 从 settings 中读取配置，而不是硬编码
    llm = ChatOpenAI(
        model=settings.default_model,
        api_key=settings.siliconflow_api_key,
        base_url=settings.base_url,
        temperature=0.7,
    )

    # 2. 测试连接
    print(">>> 正在发送请求...")
    try:
        # 这里的 invoke 是同步调用，适合简单测试
        response = llm.invoke("你好，你是谁？请用一句话简短回答。")

        print("\n=== 测试成功！模型回复如下 ===")
        print(response.content)
        print("==============================")

    except Exception as e:
        print("\n!!! 连接失败 !!!")
        print(f"错误信息: {e}")
        # 可以在这里建议用户检查 .env
        print("提示: 请检查 .env 文件中的 SILICONFLOW_API_KEY 是否正确。")


def main() -> None:
    # 入口函数
    test_llm_connection()


if __name__ == "__main__":
    main()
