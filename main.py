import math
import random
import numpy as np
from modules import Population

number_of_locations = 5


def generate_locations_list(_number_of_locations):
    _locations = []
    _locations_numbers = list(range(0,_number_of_locations+1))
    for _ in range(_number_of_locations + 1):
        _locations.append([random.randint(1, 10) for _ in range(2)])
    return _locations, _locations_numbers


def get_distance_array(_locations):
    _distance_array = []
    for location1 in _locations:
        row = []
        for location2 in _locations:
            row.append(math.dist(location1, location2))
        _distance_array.append(row)
    return _distance_array


#TODO change way of creating an array
def generate_first_generation(_population_size, _locations_numbers):
    first = np.asarray([np.random.permutation(_locations_numbers) for _ in range(_population_size)])
    generation = []
    for route in first:
        route1 = list(route)
        index_1 = route1.index(0)
        route1[0], route1[index_1] = 0, route1[0]
        route1.append(0)
        generation.append(route1)
    return generation


#TODO change way of creating Population
def generate_population(_population_size, _locations_numbers, _distance_array):
    return Population(generate_first_generation(_population_size, _locations_numbers), _distance_array)


locations, locations_numbers = generate_locations_list(number_of_locations - 1)[0], generate_locations_list(number_of_locations - 1)[1]

generacja = generate_population(10, locations_numbers, np.array(get_distance_array(locations)))

print(locations)
print(generacja.generation)
print(generacja.distance_array)
generacja.calculate_lengths_of_routes()
generacja.get_best_results()
print(generacja.lengths_list)
print(generacja.best_route_distance, generacja.best_route)
