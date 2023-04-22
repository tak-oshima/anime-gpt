from linebot.models import TextMessage
from app.core.line_client import line_bot_api
import logging

logger = logging.getLogger(__name__)

def handle_text_message(event):
    logger.info(f"Event: {event}")

    reply_token = event.reply_token
    text = event.message.text
    response = TextMessage(text=f"{text}")

    line_bot_api.reply_message(reply_token, response)
    logger.info(f"Replied to {reply_token}: {text}")