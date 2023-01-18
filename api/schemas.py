from pydantic import BaseModel


class EncodeRequestModel(BaseModel):
    url: str
