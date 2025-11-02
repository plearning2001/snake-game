import time
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.surface = pygame.display.set_mode((800,500))
        pygame.init()
        self.snake = Snake(self.surface,2)
        self.snake.draw()
    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                
                elif event.type == KEYDOWN:
                    # print(f"block_x -- {block_x}")
                    # print(f"block_y -- {block_y}\n")

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

            time.sleep(0.02)
            self.snake.walk()



class Snake:

    def __init__(self,paarent_screen,length):
        self.parent_screen = paarent_screen
        # self.x = 100
        self.x = [40]*length
        # self.y = 100
        self.y = [40]*length

        screen_width = 500
        screen_height = 500
        surface = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Move the block")
        block_x = 10
        block_y = 10
        self.block = pygame.Surface((block_x, block_y))
        self.block.fill((255, 0, 0))

        self.direction = "up"

    def draw(self):
        self.parent_screen.fill((0, 0, 0))  # Clear screen
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()        

    def move_up(self):
        # self.y = self.y - 10
        # self.draw()
        self.direction = "up"

    def move_down(self):
        # self.y = self.y + 10
        # self.draw()
        self.direction = "down"

    def move_right(self):
        # self.x = self.x + 10
        # self.draw()
        self.direction = "right"

    def move_left(self):
        # self.x = self.x - 10
        # self.draw()
        self.direction = "left"
    
    def walk(self):
        if self.direction == "left":
            self.x -= 10

        elif self.direction == "right":
            self.x += 10

        elif self.direction == "up":
            self.y -= 10

        elif self.direction == "down":
            self.y += 10
        self.draw()

def draw_block(surface,block,block_x,block_y):
    surface.fill((0, 0, 0))  # Clear screen
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    game = Game()
    game.run()
