import math
import random
import numpy as np
from modules import Population


def generate_locations_list(_number_of_locations, _minmax_coordinates):
    _locations = []
    _locations_numbers = list(range(0, _number_of_locations+1))
    for _ in range(_number_of_locations + 1):
        _locations.append([random.randint(_minmax_coordinates[0], _minmax_coordinates[1]) for _ in range(2)])
    return _locations, _locations_numbers


def get_distance_array(_locations):
    _distance_array = []
    for location1 in _locations:
        row = []
        for location2 in _locations:
            row.append(math.dist(location1, location2))
        _distance_array.append(row)
    return _distance_array


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


def generate_population(_population_size, _locations_numbers, _distance_array):
    return Population(generate_first_generation(_population_size, _locations_numbers), _distance_array)
