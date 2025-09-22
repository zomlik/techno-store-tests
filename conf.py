from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class KafkaConf(BaseModel):
    bootstrap_servers: str


class HttpxConf(BaseModel):
    base_url: str
    timeout: int


class SeleniumConf(BaseModel):
    base_url: str
    headless: bool
    timeout: int


class LoginData(BaseModel):
    login: str
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    selenium: SeleniumConf
    httpx: HttpxConf
    kafka: KafkaConf

    user: LoginData
    admin: LoginData


settings = Settings()
