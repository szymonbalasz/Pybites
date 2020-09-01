from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:

    def __init__(self, name):
        self._name = name
        self._karma = []
        self._transactions = []
        self._fans = []

    @property
    def name(self):
        return self._name

    @property
    def karma(self):
        return sum(self._karma)

    @property
    def fans(self):
        return len(self._fans)

    @property
    def points(self):
        return self._karma

    def __str__(self):
        a = f"{self.name} has a karma of {self.karma} and {self.fans} fan"
        b = f"s"
        return "".join([a, b if not (self.fans == 1) else ""])

    def __add__(self, other):
        self._transactions.append(other)
        self._karma.append(other.points)
        if not other.giver in self._fans:
            self._fans.append(other.giver)
