from dataclasses import dataclass, field


@dataclass
class Bite:
    """class that manages 3 attributes: number, title and level"""
    number: int
    title: str
    level: str = 'Beginner'

    def __post_init__(self):
        self.title = self.title.capitalize()

    def __lt__(self, other):
        return self.number < other.number
