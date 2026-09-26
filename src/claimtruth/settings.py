"""Runtime configuration, read from environment variables prefixed with CLAIMTRUTH_."""

from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelAlias(BaseModel):
    """A named model entry: a pinned model snapshot and the family it belongs to."""

    model_id: str
    family: str
    max_tokens: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CLAIMTRUTH_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    contact_email: str | None = None
    data_dir: Path = Path(".cache")
    model_aliases: dict[str, ModelAlias] = Field(default_factory=dict[str, ModelAlias])


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
