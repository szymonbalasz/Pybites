IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    best_sum = (0, 0, 0)
    for i in range(len(village)):
        e = 1
        while e <= len(village):
            current_sum = sum(village[i:e])
            if current_sum > best_sum[0]:
                best_sum = (current_sum, i+1, e)
            e += 1
    if best_sum[0] == 0:
        print(IMPOSSIBLE)
    return best_sum
