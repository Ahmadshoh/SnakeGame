import pygame
from Control import Control
from Snake import Snake
from Gui import Gui
from Food import Food
pygame.init()

# Настройки окна
windowHeight, windowWidth = 841, 841
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("SnakeGame")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

# Создаём объект классов
control = Control()
snake = Snake()
gui = Gui()
food = Food()

gui.init_field()
food.get_food_position(gui, snake.body)

var_speed = 0
while control.flag_game:
    gui.check_win_lose()
    control.control()
    window.fill(pygame.Color('DarkGrey'))
    gui.draw_indicator(window)
    gui.draw_level(window)

    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)

    if var_speed % 15 == 0 and control.flag_pause and gui.game == "GAME":
        snake.move(control)
        snake.check_barrier(gui)
        snake.eat(food, gui)
        snake.animation()

    var_speed += 1
    pygame.display.flip()
