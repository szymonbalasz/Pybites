import itertools


class Animal:

    table = []
    counter = itertools.count(10001)

    def __init__(self, name):
        self.name = name.title()
        self.num = next(self.counter)
        self.table.append(str(self))

    def __str__(self):
        return "{}. {}".format(self.num, self.name)

    @classmethod
    def zoo(cls):
        return cls.table
