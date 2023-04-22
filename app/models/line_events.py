from typing import Union
from pydantic import BaseModel
from app.models.line_messages import TextMessage


class BaseEvent(BaseModel):
    type: str
    reply_token: str
    timestamp: int


class SourceUser(BaseModel):
    type: str
    userId: str


class MessageEvent(BaseEvent):
    message: Union[TextMessage]
    source: SourceUser
