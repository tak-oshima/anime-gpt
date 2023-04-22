import asyncio
import aiohttp
from linebot.models import MessageEvent
from linebot import AsyncLineBotApi, WebhookHandler
from linebot.aiohttp_async_http_client import AiohttpAsyncHttpClient
from app.core.config import settings
import logging


logger = logging.getLogger(__name__)


class AsyncWebhookHandler(WebhookHandler):
    async def handle(self, body, signature):
        payload = self.parser.parse(body, signature, as_payload=True)

        for event in payload.events:
            func = None
            key = None

            if isinstance(event, MessageEvent):
                key = WebhookHandler._WebhookHandler__get_handler_key(
                    event.__class__, event.message.__class__
                )
                func = self._handlers.get(key, None)

            if func is None:
                key = WebhookHandler._WebhookHandler__get_handler_key(event.__class__)
                func = self._handlers.get(key, None)

            if func is None:
                func = self._default

            if func is None:
                logger.info("No handler of " + key + " and no default handler")
            else:
                await self.__invoke_func(func, event, payload)

    @classmethod
    async def __invoke_func(cls, func, event, payload):
        (has_varargs, args_count) = WebhookHandler._WebhookHandler__get_args_count(func)
        if asyncio.iscoroutinefunction(func):
            if has_varargs or args_count == 2:
                await func(event, payload.destination)
            elif args_count == 1:
                await func(event)
            else:
                await func()
        else:
            WebhookHandler._WebhookHandler__invoke_func(func, event, payload)


line_bot_api = AsyncLineBotApi(
    settings.line_channel_access_token, AiohttpAsyncHttpClient(aiohttp.ClientSession())
)
handler = AsyncWebhookHandler(settings.line_channel_secret)
