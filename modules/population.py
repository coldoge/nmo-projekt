import math
class Population():
    def __init__(self, generation, distance_array):
        self.generation = generation
        self.distance_array = distance_array
        self.lengths_list = []
        self.best_route_distance = math.inf
        self.best_route = None

    def calculate_lengths_of_routes(self):
        for route in self.generation:
            distance = 0
            for i in range(len(route)-1):
                distance = distance + self.distance_array[route[i]][route[i+1]]
            self.lengths_list.append(distance)

    def get_best_results(self):
        if self.best_route_distance > min(self.lengths_list):
            self.best_route_distance = min(self.lengths_list)
            self.best_route = self.lengths_list.index(self.best_route_distance)
            print(self.best_route)



