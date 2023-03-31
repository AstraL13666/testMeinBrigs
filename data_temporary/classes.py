from dataclasses import dataclass


@dataclass
class Test:
    question: int


@dataclass
class Answer:
    user: dict
