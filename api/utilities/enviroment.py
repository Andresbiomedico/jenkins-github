from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
