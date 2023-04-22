from fastapi import FastAPI
from app.api import line_webhook
from app.core.logging_config import setup_logging

setup_logging()

app = FastAPI()

app.include_router(line_webhook.router)
