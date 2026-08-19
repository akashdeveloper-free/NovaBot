from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
BASE_DIR=Path(__file__).resolve().parent.parent
class Settings(BaseSettings):
    BOT_TOKEN:str
    DB_PATH:str=str(BASE_DIR/'data'/'novabot.db')
    LOG_LEVEL:str='INFO'
    model_config=SettingsConfigDict(env_file='.env', extra='ignore')
settings=Settings()
