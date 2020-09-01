def binary_search(sequence, target):
    l = 0
    u = len(sequence)
    mid = (l + u) // 2

    for x in range(100):
        if sequence[mid] == target:
            return mid
        elif sequence[mid] > target:
            u = mid
            mid = (l + u) // 2
        else:
            l = mid
            mid = (l + u) // 2
