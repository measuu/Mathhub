from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class FeedbackCreate(BaseModel):
    username: str
    comment: str
    rating: float = Field(..., ge=1, le=5, description="Оцінка від 1 до 5")

class FeedbackOut(BaseModel):
    username: str
    comment: str
    rating: float

    class Config:
        orm_mode = True