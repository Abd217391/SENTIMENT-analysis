from pydantic import BaseModel


class SentimentCreate(BaseModel):
    comment: str


class SentimentResponse(BaseModel):
    id: int
    user_id: int
    user_name: str
    comment: str
    sentiment: str

    class Config:
        from_attributes = True
