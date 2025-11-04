import random
import time
import pygame
from pygame.locals import *

# Size of each block (snake + apple)
SIZE = 40

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Snake Game")

        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)
        self.snake.draw()
        self.apple.draw()

    
    def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1<x2+SIZE:
            if y1>=y2 and y1<y2+SIZE:
                return True
        
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Apple colllision
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.length += 1
            self.snake.x.append(-1)
            self.snake.y.append(-1)

            self.apple.move()

        for i in range(2,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.x[i]):
                print("!!!Game Over!!!")
                exit(0)

            print("colision...........k")
        else:
            print("pass...........k")
        

    def display_score(self):
        font = pygame.font.SysFont('arial',15)
        score = font.render(f"Score : {self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(0,10))


    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    elif event.key == K_DOWN:
                        self.snake.move_down()

                    elif event.key == K_UP:
                        self.snake.move_up()

                    elif event.key == K_RIGHT:
                        self.snake.move_right()

                    elif event.key == K_LEFT:
                        self.snake.move_left()

            self.play()
            clock.tick(3) 





class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("images/snake_block.png").convert_alpha()
        self.block = pygame.transform.scale(self.block, (SIZE, SIZE))

        self.length = length
        self.x = [SIZE] * length
        self.y = [SIZE] * length

        self.direction = "right"

    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        if self.direction != 'down':
            self.direction = "up"

    def move_down(self):
        if self.direction != 'up':
            self.direction = "down"

    def move_right(self):
        if self.direction != 'left':
            self.direction = "right"

    def move_left(self):
        if self.direction != 'right':
            self.direction = "left"

    def walk(self):
        # move body
        print("Moving")
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        print(f"x - y : {self.x} - {self.y}")
        if self.x[0] >= 800 or self.x[0] <= 0 or self.y[0] >= 460 or self.y[0] <= 0:
            print("Game over!!!")
            exit(0)

        # move head
        if self.direction == "left":
            self.x[0] -= SIZE
        elif self.direction == "right":
            self.x[0] += SIZE
        elif self.direction == "up":
            self.y[0] -= SIZE
        elif self.direction == "down":
            self.y[0] += SIZE

        self.draw()


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("images/apple.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))
        self.x = SIZE * 5
        self.y = SIZE * 5

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
    
    def move(self):
        self.x = random.randint(1,5)*40
        self.y = random.randint(1,5)*40


if __name__ == "__main__":
    game = Game()
    game.run()
