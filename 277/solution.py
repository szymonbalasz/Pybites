# OFFICIAL SOLUTION

from typing import List


def make_changes(n: int, coins: List[int]) -> int:
    coins.sort()
    ways = [1] + [0] * n

    for coin in coins:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]

    return ways[n]


print(make_changes(20, [1, 2, 5, 10, 20, 50]))
