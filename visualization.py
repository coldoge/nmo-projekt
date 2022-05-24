import pygame


def draw_text(my_font, screen, actual_generation):
    text_surface = my_font.render("best route distance: " + str(actual_generation.best_route_distance), False,
                                  (0, 0, 0))
    screen.blit(text_surface, (0, 500))

    text_surface = my_font.render("Population number: " + str(actual_generation.number_of_generation), False, (0, 0, 0))
    screen.blit(text_surface, (0, 520))


def draw_dots(route, screen):
    for element in route:
        pygame.draw.circle(screen, (250, 0, 0), (element[0], element[1]), 3)


def draw_lines(route, screen):
    for i in range(len(route)-1):
        pygame.draw.line(screen, (0, 0, 0), (route[i][0], route[i][1]), (route[i+1][0], route[i+1][1]))
