from contextlib import asynccontextmanager

from fastapi import FastAPI
from db.engine import SessionDep, create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
