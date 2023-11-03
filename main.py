from fastapi import FastAPI

from db.database import engine
from db.models import Base
from routers import user, score

app = FastAPI()
app.include_router(user.router)
app.include_router(score.router)


Base.metadata.create_all(engine)

