from queue import PriorityQueue


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


def get_path(curr_city: int, parents: list):
     path = [curr_city]
     parent = parents[curr_city]
     while parent != -1:
          path.insert(0, parent)
          parent = parents[parent]
     return path