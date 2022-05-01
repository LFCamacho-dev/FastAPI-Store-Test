import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "postgresql://postgres:luisfer123@localhost/store"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all()

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
