import statistics
from decimal import Decimal


class IntList(list):

    def __init__(self, ls):
        list.__init__(self, ls)
        self._values = ls

    @property
    def mean(self):
        return statistics.mean(self._values)

    @property
    def median(self):
        return statistics.median(self._values)

    def append(self, num):
        if isinstance(num, list):
            for each in num:
                self.add_num_to_list(each)
        else:
            self.add_num_to_list(num)

    def __add__(self, num):
        self.append(num)

    def __iadd__(self, num):
        self.append(num)
        return self

    def __getitem__(self, key):
        return super(IntList, self).__getitem__(key-1)

    #append helper
    def add_num_to_list(self, num):
        if isinstance(num, Decimal):
            num = float(num)
        NumberTypes = (int, float, complex)
        if isinstance(num, NumberTypes):
            super().append(num)
            self._values.append(num)
        else:
            raise TypeError
