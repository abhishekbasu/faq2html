from dataclasses import dataclass

@dataclass
class QnA:
    """represents a question and answer pair"""
    question: str
    answer: str
