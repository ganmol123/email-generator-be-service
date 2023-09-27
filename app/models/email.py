from pydantic import BaseModel
from typing import List


class EmailRequest(BaseModel):
    recipient_name: str
    recipient_email: str
    subject: str
    keywords: List[str]
    length: int
