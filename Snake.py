import pygame


class Snake:
    def __init__(self):
        self.head = [148, 148]
        self.body = [[148, 148], [127, 148], [106, 148]]

    def move(self, control):
        """ Движение змеи в зависимости от направления """
        if control.flag_direction == "RIGHT":
            self.head[0] += 21
        elif control.flag_direction == "LEFT":
            self.head[0] -= 21
        elif control.flag_direction == "UP":
            self.head[1] -= 21
        elif control.flag_direction == "DOWN":
            self.head[1] += 21

    def animation(self):
        """ Прибавляем в начало списка голову, а хвост удаляем """
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        """ Отрисовка змеи на экране """
        for segment in self.body:
            pygame.draw.rect(window, pygame.Color("DarkGoldenRod"), pygame.Rect(segment[0], segment[1], 20, 20))

    def check_end_window(self):
        """ Отслеживает достижение змеей края экрана """
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    def eat(self, food, gui):
        """ Змея есть еду """
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(gui, self.body)
            gui.get_new_indicate()

    def check_barrier(self, gui):
        """ Проверяет не врезалась ли змея куда-то """
        if self.head in gui.barrier:
            gui.game = "LOSE"
        if self.head in self.body[1:]:
            gui.game = "LOSE"


if __name__ == "__main__":
    snake = Snake()
    print(snake.body)
    print(snake.body[1:])
