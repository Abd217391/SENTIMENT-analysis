from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.core.config import get_current_user
from app.core.sentiment import analyze_sentiment
from app.models.sentiment import Sentiment
from app.schemas.sentiment import SentimentCreate, SentimentResponse
from app.models.user import User

router = APIRouter(
    prefix="/sentiment",
    tags=["Sentiment"]
)


@router.post("/", response_model=SentimentResponse)
def create_sentiment(
    data: SentimentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = analyze_sentiment(data.comment)

    sentiment = Sentiment(
        user_id=current_user.id,
        user_name=current_user.name,
        comment=data.comment,
        sentiment=result,
    )

    db.add(sentiment)
    db.commit()
    db.refresh(sentiment)

    return sentiment
