from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_score
from db.database import get_db
from schema import ScoreBase, PostScoreDisplay, GetScoreDisplay


router = APIRouter(prefix='/game/score', tags=['score'])


@router.post('', response_model=PostScoreDisplay)
def create_score(request: ScoreBase, db: Session = Depends(get_db)):
    return db_score.create_score(request, db)


@router.get('', response_model=GetScoreDisplay)
def get_score(player_id: int, db: Session = Depends(get_db)):
    return db_score.get_score(player_id, db)

