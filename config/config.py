"""Global configuration for this project"""

import os
from pathlib import Path as path

from loguru import logger
from pydantic.v1 import BaseSettings

current_file_path = os.path.abspath(__file__)
env_directory = path(current_file_path).parent.parent

ENV_FILE = os.path.join(env_directory, ".env")


class Configs(BaseSettings):
    app_name: str
    app_desc: str
    version: str
    host: str
    port: int
    workers: int
    device: str
    embedding_model_path: str
    api_version: str
    log_file: str
    online: bool
    default_collection_name: str
    connection: str
    endpoint_url: str
    llm_model: str
    dashscope_api_key: str
    crawl_url: str

    class Config:
        env_file = ENV_FILE


configs = Configs()


def init_log():
    logger.add(configs.log_file)


init_log()
