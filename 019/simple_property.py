from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime):
        self.expires = expires
        self.name = name

    @property
    def expired(self):
        return NOW > self.expires
