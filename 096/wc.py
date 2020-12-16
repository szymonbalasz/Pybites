def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        contents = f.read()

    lines_count = len(contents.splitlines())
    word_count = len(contents.split())
    char_count = len(list(contents))

    return f"{lines_count} {word_count} {char_count} {file_}"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
