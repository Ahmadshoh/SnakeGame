import pygame
import random


class Food:
    def __init__(self):
        self.food_position = []
        self.mouse_image = pygame.image.load("images/mouse.png")

    def get_food_position(self, gui, snake_body):
        """ Выдаёт рандомную значения координат для еды"""
        self.food_position = random.choice(gui.field)
        while self.food_position in snake_body:
            self.food_position = random.choice(gui.field)

    def draw_food(self, window):
        """ Рисовывает еду """
        # field = pygame.draw.rect(window, pygame.Color('OrangeRed'), pygame.Rect(self.food_position[0], self.food_position[1], 20, 20))
        window.blit(self.mouse_image, [self.food_position[0]-5, self.food_position[1]-5])
