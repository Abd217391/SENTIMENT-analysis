from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1 import auth, sentiment
from app.database.db import engine, Base
from app.models.user import User  # noqa: F401
from app.api.v1 import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


APP = FastAPI(lifespan=lifespan)





APP.include_router(auth.router)
APP.include_router(sentiment.router)



@APP.get("/")
def root():
    return {"status": "API running"}




