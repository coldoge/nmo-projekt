import math
import random
from itertools import chain


class Population:
    def __init__(self, generation, distance_array):
        self.generation = generation
        self.distance_array = distance_array
        self.lengths_list = []
        self.best_route_distance = math.inf
        self.best_route = None
        self.roulette_wheel = None
        self.best_result_list = []
        self.best_route_locations = None
        self.number_of_generation = 1
        self.tries_since_last_best = 0

    def calculate_lengths_of_routes(self):
        self.lengths_list = []
        for route in self.generation:
            distance = 0
            for i in range(len(route)-1):
                distance = distance + self.distance_array[route[i]][route[i+1]]
            self.lengths_list.append(distance)

    def get_best_results(self):
        if self.best_route_distance > min(self.lengths_list):
            self.best_route_distance = min(self.lengths_list)
            self.best_route = self.lengths_list.index(self.best_route_distance)
            self.best_result_list.append(self.best_route_distance)
            self.best_route_locations = self.generation[self.best_route]
            self.tries_since_last_best = 0
        else:
            self.tries_since_last_best += 1

    def get_roulette_wheel(self):
        reverse_list = [min(self.lengths_list)/x for x in self.lengths_list]
        distance_divided = [x * (100/sum(reverse_list)) for x in reverse_list]
        roulette_wheel = [distance_divided[0]]
        for i in range(1, len(distance_divided)-1):
            roulette_wheel.append(distance_divided[i] + roulette_wheel[i-1])
        self.roulette_wheel = roulette_wheel

    def draw_parent(self):
        """
        SELECTION OPERATOR
        :return:
        """
        number = random.uniform(0, 100)
        index = 0
        for element in self.roulette_wheel:
            if number < element:
                break
            index = index + 1
        return index

    def crossover(self):
        """
        CROSSOVER OPERATOR
        :return:
        """
        border = random.randint(1, len(self.generation[0])-3)
        route1 = self.generation[self.draw_parent()]
        route2 = self.generation[self.draw_parent()]
        new_route1 = [0]
        new_route2 = [0]
        for i in range(1, len(route1[:-1])):
            if i <= border:
                if route1[i] not in new_route1:
                    new_route1.append(route1[i])
                if route2[i] not in new_route2:
                    new_route2.append(route2[i])
            else:
                if route2[i] not in new_route1:
                    new_route1.append(route2[i])
                if route1[i] not in new_route2:
                    new_route2.append(route1[i])
        for element in route1[1:-1]:
            if element not in new_route1:
                new_route1.append(element)
            if element not in new_route2:
                new_route2.append(element)
        new_route1.append(0)
        new_route2.append(0)
        return new_route1, new_route2

    def update_population(self):
        new_generation = []
        for _ in range(int(len(self.generation)/2)):
            children = self.crossover()
            new_generation = list(chain(new_generation, [children[0]], [children[1]]))
        self.generation = new_generation
        self.number_of_generation += 1

    def mutation_v1(self, mutation_rate):
        for route in self.generation:
            if random.random() <= mutation_rate:
                city1 = random.randint(1, len(route)-2)
                city2 = random.randint(1, len(route)-2)
                route[city1], route[city2] = route[city2], route[city1]

# TODO it needs to be refactored
    def mutation_v2(self, mutation_rate):
        for i in range(0, len(self.generation)):
            new_route = []
            if random.random() <= mutation_rate:
                index = random.randint(1, len(self.generation[i])-2)
                for n in range(0, index):
                    new_route.append(self.generation[i][n])
                for j in range(len(self.generation[i])-2, index-1, -1):
                    new_route.append(self.generation[i][j])
                new_route.append(0)
                self.generation[i] = new_route

    def elitism(self):
        if self.best_route_locations not in self.generation:
            worst_route_index = self.lengths_list.index(max(self.lengths_list))
            self.generation[worst_route_index] = self.best_route_locations
            self.lengths_list[worst_route_index] = self.best_route_distance
            self.best_route = worst_route_index

    def get_route(self, locations):
        route = []
        for element in self.best_route_locations:
            route.append(locations[element])
        return route
