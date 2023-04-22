from pydantic import BaseModel

class TextMessage(BaseModel):
    id: str
    type: str
    text: str
