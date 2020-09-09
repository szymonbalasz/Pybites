import json
import re


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    result = []
    for file in files:
        with open(file) as f:
            x = json.loads(f.read())
            result.append(x)
    return result

def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]
    pass


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    most = (0, '')
    for movie in movies:
        nominations = 0
        total = re.findall(r'Nominated for (\d+)|(\d+) nominations', movie["Awards"])
        for each in total:
            nominations += sum(list(map(lambda x: 0 if x ==
                                        '' else int(x), each)))
        
        if nominations > most[0]:
            most = (nominations, movie['Title'])
    return most[1]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    longest = (0, '')
    for movie in movies:
        runtime = int(re.findall(r'(\d+) min', movie["Runtime"])[0])
        if runtime > longest[0]:
            longest = (runtime, movie["Title"])
    return longest[1]
