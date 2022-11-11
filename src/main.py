from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.functions.exactos import exactos_function
from src.functions.similares import similares_function

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

app.include_router(exactos_function.router)
app.include_router(similares_function.router)