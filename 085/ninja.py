scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None
        self._belt_earned = False

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for k, v in reversed(sorted(BELTS.items())):
            if new_score >= k:
                return v
        return None

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError("Score takes an int")

        if new_score > self._score:
            self._score = new_score
            self.new_belt = self._get_belt(new_score)

            if self.new_belt != self._last_earned_belt:
                self._last_earned_belt = self.new_belt
                print(
                    f"Congrats, you earned {self.score} points obtaining the PyBites Ninja {self._last_earned_belt.title()} Belt")
            else:
                print(f"Set new score to {self.score}")
        else:
            raise ValueError("Cannot lower score")

    score = property(_get_score, _set_score)
