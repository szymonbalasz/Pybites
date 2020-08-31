# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


def get_edges(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)
    """
    edges = 0
    directions = {
        "up" : [-1, 0],
        "down" : [1, 0],
        "left" : [0, -1],
        "right" : [0, 1]}

    for direction in directions.values():
        try:
            destination = (r+direction[0], c+direction[1])
            edge_row, edge_col = destination[0] >= 0, destination[1] >= 0
            if not edge_row:
                edges += 1
            elif not edge_col:
                edges += 1
            elif map_[destination[0]][destination[1]] == 0:
                edges += 1
        except:
            edges += 1

    return edges


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    for r in range(len(map_)):
        for c in range(len(map_[r])):
            if map_[r][c] == 1:
                perimeter += get_edges(map_, r, c)

    return perimeter
