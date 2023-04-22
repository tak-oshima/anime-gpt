from linebot import LineBotApi, WebhookHandler
from app.core.config import settings

line_bot_api = LineBotApi(settings.line_channel_access_token)
handler = WebhookHandler(settings.line_channel_secret)
