"""Rolvio configuration management."""
import os
from pathlib import Path
from pydantic import BaseModel, Field
from platformdirs import user_data_dir, user_config_dir, user_log_dir
from dotenv import load_dotenv

APP_NAME = "Rolvio"
APP_AUTHOR = "NORVI"

class AppPaths(BaseModel):
    data_dir: Path = Field(default_factory=lambda: Path(user_data_dir(APP_NAME, APP_AUTHOR)))
    config_dir: Path = Field(default_factory=lambda: Path(user_config_dir(APP_NAME, APP_AUTHOR)))
    log_dir: Path = Field(default_factory=lambda: Path(user_log_dir(APP_NAME, APP_AUTHOR)))

    def ensure_paths(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)

class Settings(BaseModel):
    paths: AppPaths = Field(default_factory=AppPaths)
    env: str = Field(default="development")

_settings_instance = None

def get_settings() -> Settings:
    global _settings_instance
    if _settings_instance is None:
        load_dotenv()
        _settings_instance = Settings(
            env=os.getenv("ROLVIO_ENV", "development")
        )
        _settings_instance.paths.ensure_paths()
    return _settings_instance
