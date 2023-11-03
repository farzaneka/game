from datetime import datetime

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.database import get_db
from db.models import Score
from helper import to_dict
from log import logger
from schema import ScoreBase


def create_score(request: ScoreBase, db: Session = Depends(get_db)):
    from routers.score import router

    if request.score < 0 or request.score > 100:
        return JSONResponse(
            status_code=400,
            content={'msg': 'invalid_score', 'data': ['SEND SCORE']},
        )

    score = db.query(Score).filter(Score.player_id == request.player_id).one_or_none()
    if score is not None:
        score.date_time = datetime.now()
        score.score += request.score
        db.commit()

    elif score is None:
        score = Score(
            player_id=request.player_id,
            score=request.score,
            date_time=datetime.now(),
        )
        db.add(score)
        db.commit()

    logger.info(f'Endpoint url: {router.prefix}')
    return score


def get_score(player_id: int, db: Session = Depends(get_db)):
    from routers.score import router

    score = db.query(Score).filter(Score.player_id == player_id).one_or_none()
    if score is not None:
        records = db.query(Score).order_by(Score.score.desc()).all()
        if len(records) != 0:
            score.records = to_dict(records)
            db.commit()

    logger.info(f'Endpoint url: {router.prefix}?playerId={player_id}')
    return score

