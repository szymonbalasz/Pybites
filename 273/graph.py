import heapq as hq
from collections import namedtuple


def shortest_path(graph, start, end):
    """
        Input: graph: a dictionary of dictionary
               start: starting city   Ex. a
               end:   target city     Ex. b

        Output: tuple of (distance, [path of cites])
        Ex.   (distance, ['a', 'c', 'd', 'b])
    """

    frontier = []
    Node = namedtuple('Node', 'cost path')
    current = Node(cost=0, path=[start])
    hq.heappush(frontier, current)
    explored = set()

    found = False

    while not found:
        current = hq.heappop(frontier)
        current_name = current.path[-1]
        if current_name in explored:
            continue
        explored.add(current_name)

        if current_name == end:
            break

        for node in graph[current_name]:
            new_node = Node(
                cost=current.cost + graph[current_name][node],
                path=(current.path + [node])
            )
            hq.heappush(frontier, new_node)

    return (current.cost, current.path)
