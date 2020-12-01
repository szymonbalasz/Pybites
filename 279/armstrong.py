def is_armstrong(n: int) -> bool:
    total = 0
    for each in str(n):
        total += int(each)**len(str(n))
    
    return total == n
