import copy


def min_path_sum(V, V_charger, E, s, t, d):
    """
    :param V: list of nodes (assume nodes are numbers in increasing order)
    :param E: adjacency matrix; value at row i and column j represents the distance between node i and node j
    :param V_charger: list of charging nodes
    :param s: start node
    :param t: terminal node
    :param d: max distance of sub-path without charging station node
    :return: total distance of the shortest path from s to t that contains a node from V_charge every d distance
    """
    n = len(V)
    distances = copy.deepcopy(E)
    charges = copy.deepcopy(E)

    for i in range(n):
        for j in range(n):
            charge = d - charges[i][j]
            charges[i][j] = charge

    # i -> k -> j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                shorter = distances[i][k] + distances[k][j] < distances[i][j]
                charged = charges[i][k] - distances[k][j] >= 0

                if shorter and charged:
                    distances[i][j] = distances[i][k] + distances[k][j]

                    if j in V_charger:
                        charges[i][j] = d
                    else:
                        charges[i][j] = charges[i][k] - distances[k][j]

    print("Optimal distances")
    for row in distances:
        print(row)
    print()

    print("Charge remaining")
    for row in charges:
        print(row)
    print()

    print("Min distance from s to t:", distances[s][t])
    return distances[s][t]

def get_path(curr_city: int, parents: list):
    path = [curr_city]
    parent = parents[curr_city]
    while parent != -1:
        path.insert(0, parent)
        parent = parents[parent]
    return path


### TEST ###
inf = float('inf')

V = [0, 1, 2, 3, 4, 5]
V_charge = [0, 3, 4, 5]
E = [[000, 200, 300, 400, inf, inf],
     [inf, 000, 200, 100, inf, inf],
     [inf, inf, 000, inf, inf, 250],
     [inf, inf, inf, 000, 200, inf],
     [inf, inf, 100, inf, 000, 400],
     [inf, inf, inf, inf, inf, 000]]
s = 0
t = 5
d = 400
min_path_sum(V, V_charge, E, s, t, d)
print()

V = [0, 1, 2, 3, 4, 5]
V_charge = [0, 1, 3, 4, 5]
E = [[000, 200, 300, 400, inf, inf],
     [inf, 000, 200, 100, inf, inf],
     [inf, inf, 000, inf, inf, 250],
     [inf, inf, inf, 000, 200, inf],
     [inf, inf, 100, inf, 000, 400],
     [inf, inf, inf, inf, inf, 000]]
s = 0
t = 5
d = 500

min_path_sum(V, V_charge, E, s, t, d)
