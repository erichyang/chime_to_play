import pygame

from chime import Chime

WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chime to Play!")

WHITE = (255, 255, 255)
FPS = 30


def draw_window(chimes):
    screen.fill(WHITE)

    for chime in chimes:
        screen.blit(chime.surf, chime.rect)
    pygame.display.flip()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    chimes = [Chime()]
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(chimes)
        for chime in chimes:
            

    pygame.quit()


if __name__ == '__main__':
    main()
