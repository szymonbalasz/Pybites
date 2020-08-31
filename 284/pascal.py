from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    
    rows = []

    if N == 0:
        return rows
    
    rows.append([1])

    for i in range(1, N):
        rows.append(add_row(rows[i-1]))

    return rows[N-1]

def add_row(row: List[int]) -> List[int]:

    new_row = []
    #pad pyramid with 0's
    row.insert(0, 0)
    row.append(0)
    for i in range(len(row)):
        try:
            new_row.append(row[i] + row[i+1])
        except IndexError:
            continue 
    #remove padding and return
    row.pop(0)
    row.pop()
    return new_row

print(pascal(7))
