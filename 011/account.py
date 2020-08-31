from functools import total_ordering


@total_ordering
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self):
        return len(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __getitem__(self, index):
        return self._transactions[index]

    def __add__(self, num):
        if not type(num) == int:
            raise ValueError
        self._transactions.append(num)

    def __sub__(self, num):
        self.__add__(num*-1)

    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"
