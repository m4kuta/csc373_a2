from dijkstra import *


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[] for i in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))


def main():
    print('Truck Graph')
    truck_graph = Graph(7)
    truck_graph.add_edge(0, 1, 2)
    truck_graph.add_edge(0, 2, 7)
    truck_graph.add_edge(0, 3, 8)
    truck_graph.add_edge(1, 4, 9)
    truck_graph.add_edge(2, 5, 4)
    truck_graph.add_edge(3, 5, 1)
    truck_graph.add_edge(4, 5, 5)
    truck_graph.add_edge(4, 6, 7)
    truck_graph.add_edge(5, 6, 3)

    truck_cities = [0, 1, 2, 3, 4, 5, 6]
    roads = truck_graph.edges
    start_city = 0
    truck_dijkstra(truck_cities, roads, start_city)

    print()
    print('Vanilla Graph')
    vanilla_graph = Graph(9)
    vanilla_graph.add_edge(0, 1, 4)
    vanilla_graph.add_edge(0, 6, 7)
    vanilla_graph.add_edge(1, 6, 11)
    vanilla_graph.add_edge(1, 7, 20)
    vanilla_graph.add_edge(1, 2, 9)
    vanilla_graph.add_edge(2, 3, 6)
    vanilla_graph.add_edge(2, 4, 2)
    vanilla_graph.add_edge(3, 4, 10)
    vanilla_graph.add_edge(3, 5, 5)
    vanilla_graph.add_edge(4, 5, 15)
    vanilla_graph.add_edge(4, 7, 1)
    vanilla_graph.add_edge(4, 8, 5)
    vanilla_graph.add_edge(5, 8, 12)
    vanilla_graph.add_edge(6, 7, 1)
    vanilla_graph.add_edge(7, 8, 3)

    # vanilla_graph = Graph(9)
    # vanilla_graph.add_edge(0, 1, 4)
    # vanilla_graph.add_edge(0, 7, 8)
    # vanilla_graph.add_edge(1, 2, 8)
    # vanilla_graph.add_edge(1, 7, 11)
    # vanilla_graph.add_edge(2, 3, 7)
    # vanilla_graph.add_edge(2, 8, 2)
    # vanilla_graph.add_edge(2, 5, 4)
    # vanilla_graph.add_edge(3, 4, 9)
    # vanilla_graph.add_edge(3, 5, 14)
    # vanilla_graph.add_edge(4, 5, 10)
    # vanilla_graph.add_edge(5, 6, 2)
    # vanilla_graph.add_edge(6, 7, 1)
    # vanilla_graph.add_edge(6, 8, 6)
    # vanilla_graph.add_edge(7, 8, 7)

    cities = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    roads = vanilla_graph.edges
    start_city = 0
    vanilla_dijkstra(cities, roads, start_city)


if __name__ == "__main__":
    main()