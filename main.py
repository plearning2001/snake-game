import pygame
from pygame.locals import *

def draw_block(surface,block,block_x,block_y):
    surface.fill((0, 0, 0))  # Clear screen
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    # Create a block (a simple red square)
    block = pygame.Surface((50, 50))
    block.fill((255, 0, 0))

    screen_width = 500
    screen_height = 500
    surface = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Move the block")
    block_x = 5
    block_y = 5
    block = pygame.Surface((block_x, block_y))
    block.fill((255, 0, 0))

    draw_block(surface,block,block_x,block_y)
    
    # pygame.display.flip()

    running = True


    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            elif event.type == KEYDOWN:
                print(f"block_x -- {block_x}")
                print(f"block_y -- {block_y}\n")

                if event.key == K_ESCAPE:
                    running = False
            
                elif event.key == K_DOWN:
                    block_y += 10

                elif event.key == K_UP:
                    block_y -= 10

                elif event.key == K_RIGHT:
                    block_x += 10

                elif event.key == K_LEFT:
                    block_x -= 10
                draw_block(surface,block,block_x,block_y)
