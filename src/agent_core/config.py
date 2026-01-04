from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    siliconflow_api_key: str

    qwen2_5_7b_instruct: str

    base_url: str = "https://api.siliconflow.cn/v1"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
