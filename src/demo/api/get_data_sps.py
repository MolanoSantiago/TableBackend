from src.demo.common.common_database import create_database_connection, get_exactos
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def get_duplicados():
    create_database_connection()
    return get_exactos()

# @app.get('/similares')
# async def get_duplicados():
#     create_database_connection()
#     return get_similares()