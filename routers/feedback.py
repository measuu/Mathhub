from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Feedback
from schemas import FeedbackCreate, FeedbackOut

router = APIRouter()


@router.post("/", response_model=FeedbackOut)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    new_feedback = Feedback(
        username=feedback.username, comment=feedback.comment, rating=feedback.rating
    )
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback


@router.get("/", response_model=List[FeedbackOut])
def get_feedbacks(db: Session = Depends(get_db)):
    return db.query(Feedback).all()
