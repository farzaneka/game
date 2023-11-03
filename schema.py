from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class ScoreBase(BaseModel):
    player_id: int
    score: int


class PostScoreDisplay(BaseModel):
    player_id: int
    score: int
    date_time: datetime

    class Config:
        orm_mode = True


class GetScoreDisplay(BaseModel):
    player_id: int
    score: int
    date_time: datetime
    records: list

    class Config:
        orm_mode = True

