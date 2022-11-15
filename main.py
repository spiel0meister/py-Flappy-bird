import pygame
import Pipe
import Bird
from random import random

pygame.init()
WIDTH, HEIGHT = 474, 355
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bg = pygame.image.load("assets/background.bmp")
pipe_img = pygame.image.load("assets/pipe.bmp")
rotated_pipe_img = pygame.transform.rotate(pipe_img, 180)
bird_img = pygame.image.load("assets/bird.bmp")


pipes = []


def draw(WIN):
    WIN.blit(bg, bg.get_rect())
    for pipe in pipes:
        pipe.draw(WIN)


def main():
    frame_count = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        peace = random()
        while peace <= 0.1 or peace >= 0.9:
            peace = random()

        for pipe in pipes:
            pipe.update()
        draw(WIN)
        if frame_count % (pipe_img.get_width() * 3) == 0:
            pipes.append(Pipe.Pipe(WIDTH, -rotated_pipe_img.get_height() * (1 - peace), HEIGHT/4,
                                   rotated_pipe_img,  pipe_img))
        pygame.display.update()
        frame_count += 1
        clock.tick(30)


if __name__ == "__main__":
    main()
