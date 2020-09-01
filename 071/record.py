class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.max_score = None

    def __call__(self, num):
        if not self.max_score:
            self.max_score = num

        elif num > self.max_score:
            self.max_score = num

        return self.max_score
