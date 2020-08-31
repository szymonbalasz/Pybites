from collections import deque
def num_ops(n):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    x = 1
    path = {x : [[]]}
    frontier = []

    while True:

        #create new nodes in exploration graph
        
        if (x*2) not in path:            
            frontier.append(x*2)
            path[x*2] = [[]]
            path[x*2][0].append(x*2)
            for node in path[x][0]:
                path[x*2][0].append(node)

        else:
            path[x*2].append([])
            i = len(path[x*2])-1
            path[x*2][i].append(x*2)
            for node in path[x][0]:                
                path[x*2][i].append(node)
        
        
        if (x//3) not in path:            
            frontier.append(x//3)
            path[x//3] = [[]]
            path[x//3][0].append(x//3)
            for node in path[x][0]:
                path[x//3][0].append(node)

        else:
            path[x//3].append([])
            i = len(path[x//3])-1
            path[x//3][i].append(x//3)
            for node in path[x][0]:                
                path[x//3][i].append(node)


        #remove nodes not worth exploring based on how complex search should be.
        #higher number = more nodes explored

        COMPLEXITY_MAGNITUDE = 10000
        frontier = [node for node in frontier if node < (COMPLEXITY_MAGNITUDE)]

        if frontier:
            x = frontier.pop(0)
        else:
            break

    return min([len(ls) for ls in path[n]])

print(num_ops(3012))

#SOLUTION


# def num_ops(n):
#     q = deque([(1, 0)])
#     seen = set()

#     while q:
#         res, ops = q.popleft()

#         # found the answer
#         if res == n:
#             return ops

#         if res//3 not in seen:
#             q.append((res//3, ops+1))
#             seen.add(res//3)

#         if res * 2 not in seen:
#             q.append((res*2, ops+1))
#             seen.add(res*2)
