from pydantic import BaseModel

class ErrorMessage(BaseModel):
    detail: str
    code: int
    message: str
