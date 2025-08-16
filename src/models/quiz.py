# src/models/quiz.py
from pydantic import BaseModel
from typing import List

class QuizQuestion(BaseModel):
    id: str
    class_level: str
    subject: str
    question: str
    options: List[str]
    answer_index: int
