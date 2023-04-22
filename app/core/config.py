from pydantic import BaseSettings

class Settings(BaseSettings):
    line_channel_secret: str
    line_channel_access_token: str

    class Config:
        env_file = ".env"

settings = Settings()
