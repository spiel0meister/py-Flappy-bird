import pygame

pygame.init()
WIDTH, HEIGHT = 474, 355
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bg = pygame.image.load("assets/background.bmp")


def draw():
    WIN.blit(bg, bg.get_rect())


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()
        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    main()
