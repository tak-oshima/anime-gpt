from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from app.models.line_events import MessageEvent
from app.handlers.message_handler import handle_text_message
from app.core.line_client import handler
from linebot.models import TextMessage
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/webhook")
async def webhook(request: Request):
    signature = request.headers["X-Line-Signature"]
    body = (await request.body()).decode("utf-8")
    logger.info(f"Request body: {body}")

    try:
        await handler.handle(body, signature)
    except Exception as e:
        logger.error(f"Request body handling failed: {str(e)}")
        return JSONResponse(
            content={"error": str(e)}, status_code=status.HTTP_400_BAD_REQUEST
        )

    return JSONResponse(content={"message": "OK"})


@handler.add(MessageEvent, message=TextMessage)
async def handle_message(event: MessageEvent):
    logger.info(f"Received message: {event.message.text}")
    if event.message.type == "text":
        await handle_text_message(event)
