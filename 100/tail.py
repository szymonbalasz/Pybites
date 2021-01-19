def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath) as file:
        data = file.read()
        result = data.splitlines()
        for each in result:
            each.strip()
        return result[-n:]

