WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for row in range(0, size):
        div = 0 if row % 2 == 0 else 1
        line = ""
        for block in range(0, size):
            if block % 2 == div:
                line += WHITE
            else:
                line += BLACK
        print(line)
