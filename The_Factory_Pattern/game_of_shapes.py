import pygame


class Shape(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def draw():
        raise NotImplementedError()

    def move(self, direction):
        if direction == "up":
            self.y -= 4
        if direction == "down":
            self.y += 4
        if direction == "left":
            self.x -= 4
        if direction == "right":
            self.x += 4

    @staticmethod
    def create(shape):
        if shape == "rect":
            print("here")
            return Rectangle(100, 100)
        if shape == "circle":
            return Circle(x, y)


class Rectangle(Shape):
    def draw(self):
        print("here", self.x, self.y)
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            pygame.Rect(self.x, self.y, 20, 20)
        )
        


class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 10)


if __name__ == "__main__":
    window_dimensions = 800, 600
    screen = pygame.display.set_mode(window_dimensions)
    x = 100
    y = 100
    player_quits = False
    obj = Shape.create("rect")
    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                obj.move("up")
            if pressed[pygame.K_DOWN]:
                obj.move("down")
            if pressed[pygame.K_LEFT]:
                obj.move("left")
            if pressed[pygame.K_RIGHT]:
                obj.move("right")

            screen.fill((0, 0, 0))
            obj.draw()

        pygame.display.flip()
