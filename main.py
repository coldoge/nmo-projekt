import pygame
from locations_generator import *
from config import *
from visualization import draw_text, draw_dots, draw_lines

# pygame initialization
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.font.init()
my_font = pygame.font.SysFont(font, font_size)

# generation of the first generation in the genetic algorithm
locations, locations_numbers = generate_locations_list(number_of_locations - 1, minmaxCoordinates)[0],\
                               generate_locations_list(number_of_locations - 1, minmaxCoordinates)[1]
actual_generation = generate_population(solutions_in_generation, locations_numbers,
                                        np.array(get_distance_array(locations)))

# visualization and generating generation loop
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    screen.fill(white)
    actual_generation.calculate_lengths_of_routes()
    actual_generation.get_best_results()
    actual_generation.get_roulette_wheel()
    route = actual_generation.get_route(locations)
    draw_dots(route, screen)
    draw_lines(route, screen)
    draw_text(my_font, screen, actual_generation)
    actual_generation.update_population()
    actual_generation.mutation(mutation_rate)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
