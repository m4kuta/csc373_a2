from queue import PriorityQueue
from heapq import *
import sys


def vanilla_dijkstra(cities: list[int], roads: list[list[tuple]], start_city: int):
    # Initialize list containing immediate predecessor of each city
    parents = [-1 for city in cities]

    # Initialize list of best_distances from start_city to all other cities as infinity
    best_distances = [sys.maxsize for city in cities]
    best_distances[start_city] = 0

    # Initialize min heap of roads to cities neighbouring start_city where key: length of road and value: city
    # Update distance from start_city to each of its neighbouring cities in best_distances list
    pq = PriorityQueue()
    for road in roads[start_city]:
        dest = road[0]
        dist = road[1]

        pq.put((dist, dest))
        best_distances[dest] = dist
        parents[dest] = start_city

    # While not all the cities have been visited
    while not pq.empty():
        # Get the head of the priority queue (neighbouring city with the least distance to start_city)
        (curr_dist, curr_city) = pq.get()

        # Add it to the set of visited cities
        # visited.add(curr_city)

        # Iterate over each road from the curr_city to its neighbouring cities
        for curr_road in roads[curr_city]:
            curr_dest = curr_road[0]
            curr_dist = curr_road[1]

            # If the dist from start_city to curr_city to dest_city is less than dist from start_city to dest_city,
            if best_distances[curr_city] + curr_dist < best_distances[curr_dest]:
                # update distance from start_city to dest_city in best_distances
                best_distances[curr_dest] = best_distances[curr_city] + curr_dist
                parents[curr_dest] = curr_city

                # change dest_city's key in the priority queue by removing and re-adding
                # pq.change_key((best_distances[curr_dest], curr_dest))
                new_pq = PriorityQueue()
                while not pq.empty():
                    (dist, city) = pq.get()
                    if city != curr_dest:
                        new_pq.put((dist, city))
                pq = new_pq
                pq.put((best_distances[curr_dest], curr_dest))

    for city in cities:
        itineraries = 'Itinerary to city {0}:\n    Distance: {1}\n    Path: {2}'.format(
            city, best_distances[city], get_path(city, parents))
        print(itineraries)


def truck_dijkstra(cities: list[int], roads: list[list[tuple]], start_city: int):
        print("Start city:", start_city)

        # Initialize list containing immediate predecessor of each city
        parents = [-1 for city in cities]

        # Initialize list of the best height itineraries from start_city to all other cities as 0
        best_heights = [0 for city in cities]
        best_heights[start_city] = sys.maxsize

        # Initialize max heap to hold cities where key is the current best height to that city
        max_heap = []
        # For each road from start_city to its neighbours
        for road in roads[start_city]:
            (next_city, height_to_next_city) = road
            # Push start_city neighbours to max heap
            heappush(max_heap, (height_to_next_city, next_city))
            # Update the best height from start_city to each neighbour
            best_heights[next_city] = height_to_next_city
            # Set start_city as predecessor to its neighbours
            parents[next_city] = start_city

        # While not all the cities have been visited
        while len(max_heap) > 0:
            # Get and set next city with the best height as curr_city
            (best_height_to_curr_city, curr_city) = heappop(max_heap)

            # Iterate over each road from the curr_city to its neighbours
            for road in roads[curr_city]:
                (next_city, height_to_next_city) = road
                best_height_to_next_city = best_heights[next_city]
                # Declare the min height of new path from start_city to next_city
                new_height_to_next_city = min(best_height_to_curr_city, height_to_next_city)

                if new_height_to_next_city > best_height_to_next_city:
                    # Update the best height from start_city to next_city
                    best_heights[next_city] = new_height_to_next_city
                    # Set curr_city as predecessor of next_city
                    parents[next_city] = curr_city
                    # Update next_city's key in the max_heap with its new best height
                    max_heap = update_heap(max_heap, next_city, best_heights[next_city])

        for city in cities:
            itineraries = 'Itinerary to city {0}:\n    Best height: {1}\n    Path: {2}'.format(
                city, best_heights[city], get_path(city, parents))
            print(itineraries)


def update_heap(max_heap, target, new_key):
    new_heap = []
    while len(max_heap) > 0:
        (height_to_next_city, city) = heappop(max_heap)
        if city != target:
            heappush(new_heap, (height_to_next_city, city))
    heappush(new_heap, (new_key, target))
    return new_heap


def get_path(curr_city: int, parents: list):
    path = [curr_city]
    parent = parents[curr_city]
    while parent != -1:
        path.insert(0, parent)
        parent = parents[parent]
    return path
