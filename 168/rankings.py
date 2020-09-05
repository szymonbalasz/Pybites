from dataclasses import dataclass
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __init__(self, name: str, bites: int):
        self.name = name
        self.bites = bites

    def __str__(self):
        return f"[{self.bites}] {self.name}"

    def __lt__(self, other):
        return self.bites < other.bites

    def __gt__(self, other):
        return self.bites > other.bites

    def __eq__(self, other):
        return self.bites == other.bites


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    rankings: list

    def __init__(self):
        self.rankings = []

    def __str__(self):
        return str(self.rankings)

    def add(self, ninja):
        self.rankings.append(ninja)
        self.rankings.sort()

    def dump(self):
        result = self.rankings[0]
        del self.rankings[0]
        return result

    def lowest(self, count=1):
        return[self.rankings[i] for i in range(count)]

    def highest(self, count=1):
        return [self.rankings[(-1 - i)] for i in range(count)]

    def pair_up(self, count=3):
        return [(self.highest(i+1)[i], self.lowest(i+1)[i]) for i in range(count)]

    def __len__(self):
        return len(self.rankings)
