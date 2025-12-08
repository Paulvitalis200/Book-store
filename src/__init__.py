from fastapi import FastAPI
from src.books.routes import book_router
from src.db.main import initdb
from contextlib import asynccontextmanager


#the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):    
    await initdb()
    print("Server is starting...")
    yield
    print("server is stopping")


version = 'v1'

app = FastAPI(
    title="Bookly",
    description="A RESTful API for a book review web service",
    version=version,
    lifespan=lifespan
)

app.include_router(
    book_router, 
    prefix=f"/api/{version}/books",
    tags=['books']
)

