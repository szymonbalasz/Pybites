from typing import List


def make_changes(n: int, coins: List[int]) -> int:
    """
    Input: n - the changes amount
          coins - the coin denominations
    Output: how many ways to make this changes
    """
    
    table = [[0 for x in range(len(coins))] for x in range(n+1)]
    for i in range(len(coins)):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(len(coins)):
            x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0

            table[i][j] = x + y
    
    return table[n][len(coins)-1]

