from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ARXIV_BASE_URL: str = "https://arxiv.org/search/?query=machine+learning&searchtype=all"
    BRONZE_DATA_PATH: str = "data/bronze/arxiv"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()