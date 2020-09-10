from collections import namedtuple
from enum import Enum
from typing import Sequence

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError

        if not len(cards) == 13:
            raise ValueError

        for card in cards:
            if not isinstance(card, Card):
                raise ValueError

        self.cards = cards
        sorted_cards = sorted(sorted(self.cards, key=lambda card: card.rank.value),
                              key=lambda card: card.suit.name, reverse=True)
        self.cards = sorted_cards

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        result = []

        #sorted_cards = sorted(sorted(self.cards, key=lambda card: card.rank.value), key=lambda card: card.suit.name, reverse=True)
        for card in self.cards:
            if not card.suit.name in result:
                result.append(" ")
                result.append(card.suit.name)
                result.append(":")
            result.append(Rank(card.rank.value).name)

        return "".join(result).strip()

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        points = 0
        for card in self.cards:
            if card.rank in HCP:
                points += HCP[card.rank]

        return points

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        value = 0
        for x in range(1, 5):
            num = 0
            for card in self.cards:
                if card.suit == Suit(x):
                    num += 1
            if num == 2:
                value += 1
        return value

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        value = 0
        for x in range(1, 5):
            num = 0
            for card in self.cards:
                if card.suit == Suit(x):
                    num += 1
            if num == 1:
                value += 1
        return value

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        value = 0
        for x in range(1, 5):
            num = 0
            for card in self.cards:
                if card.suit == Suit(x):
                    num += 1
            if num == 0:
                value += 1
        return value

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        return (self.doubletons * 1) + (self.singletons * 2) + (self.voids * 3)

    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.ssp + self.hcp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        value = 0
        for x in range(1, 5):
            suited_cards = []
            for card in self.cards:
                if card.suit == Suit(x):
                    suited_cards.append(card.rank.value)

            if not suited_cards:
                continue

            suited_cards = suited_cards[0:3]
            #print(suited_cards)

            if len(suited_cards) == 1:
                if not 1 in suited_cards:
                    value += 1

            elif len(suited_cards) == 2:
                if suited_cards == [1, 2]:
                    pass
                elif suited_cards[0] in [1, 2]:
                    value += 1
                else:
                    value += 2
            else:
                if suited_cards == [1, 2, 3]:
                    pass
                elif suited_cards[0:2] in [[1, 2], [1, 3], [2, 3]]:
                    value += 1
                elif suited_cards[0] < 4:
                    value += 2
                else:
                    value += 3

        return value
