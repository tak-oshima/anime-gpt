from linebot.models import TextMessage
from app.core.line_client import line_bot_api
import logging

logger = logging.getLogger(__name__)


async def handle_text_message(event):
    reply_token = event.reply_token
    text = event.message.text
    response = TextMessage(text=f"{text}")
    await line_bot_api.reply_message(reply_token, response)
