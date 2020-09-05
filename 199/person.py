# see __mro__ output in Bite description

class Person(object):
    def __str__(self):
        return f"I am a person"


class Father(Person):
    def __str__(self):
        return f"{super().__str__()} and cool daddy"


class Mother(Person):
    def __str__(self):
        return f"{super().__str__()} and awesome mom"


class Child(Father, Mother):
    def __str__(self):
        return f"I am the coolest kid"
