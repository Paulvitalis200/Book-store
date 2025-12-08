import os
from sqlmodel import text
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)


async def initdb():
    """create a connection to our db"""

    async with engine.begin() as conn:
        statement = text("select 'Hello World'")

        result = await conn.execute(statement)

        print(result)