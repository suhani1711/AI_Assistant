from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai import ask_ai


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class StudyRequest(BaseModel):
    question: str
    notes: str


@app.get("/")
def home():
    return {
        "message": "AI Study Assistant is running!"
    }


@app.post("/ask")
def ask_question(request: StudyRequest):

    answer = ask_ai(
        request.question,
        request.notes
    )

    return {
        "question": request.question,
        "answer": answer
    }