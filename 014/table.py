import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(names=None, aliases=None, points=None, awake=None):
    if awake is not None:
        for x in range(len(awake)):
            yield (names[x] + SEPARATOR + aliases[x] + SEPARATOR + str(points[x]) + SEPARATOR + str(awake[x]))
        return

    if points is not None:
        for x in range(len(points)):
            yield (names[x] + SEPARATOR + aliases[x] + SEPARATOR + str(points[x]))
        return

    if aliases is not None:
        for x in range(len(aliases)):
            yield (names[x] + SEPARATOR + aliases[x])
        return

    if names is not None:
        for name in names:
            yield name
