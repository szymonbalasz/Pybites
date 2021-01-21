IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    result = []
    for name in names:
        if len(result) >= MAX_NAMES or name[0] == QUIT_CHAR:
            break
        if name[0] == IGNORE_CHAR:
            continue
        valid = True
        for char in name:
            if char.isdigit():
                valid = False
                break
        if valid:
            result.append(name)

    return result

