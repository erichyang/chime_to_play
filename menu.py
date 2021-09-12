import pygame
import sys
from pygame.locals import *

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Chime Noises')
width = 1200
height = 900
screen = pygame.display.set_mode((width, height), 0, 32)

pygame.font.init()


def gen_font(size: int):
    font = pygame.font.Font("./assets/KitNoms-Regular.ttf", size)
    return font


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:
        bg = pygame.image.load("./assets/main_menu_bg.png")
        screen.fill((0, 0, 0))
        screen.blit(bg, bg.get_rect())

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(width / 2 - 150, height / 2 - 75, 300, 100)
        button_2 = pygame.Rect(width / 2 - 150, height / 2 + 75, 300, 100)
        button_3 = pygame.Rect(width / 2 - 75, height / 2 + 225, 150, 75)
        if button_1.collidepoint((mx, my)):
            if click:
                challenge()
        if button_2.collidepoint((mx, my)):
            if click:
                free_play()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()

        # pygame.draw.rect(screen, (186, 121, 125), button_1)
        # pygame.draw.rect(surface, color, location, thickness, roundness)

        # pygame.draw.rect(screen, (186, 121, 125), button_1, 50, 20)
        # pygame.draw.rect(screen, (186, 121, 125), button_2, 50, 20)
        # pygame.draw.rect(screen, (186, 121, 125), button_3, 50, 20)
        #
        # draw_text('Challenge', gen_font(60), (255, 255, 255), screen, width / 2 - 85, height / 2 - 50)
        # draw_text('Free Play', gen_font(60), (255, 255, 255), screen, width / 2 - 85, height / 2 + 100)
        # draw_text('Quit', gen_font(50), (255, 255, 255), screen, width / 2 - 38, height / 2 + 240)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def challenge():
    is_running = True
    while is_running:
        screen.fill((0, 0, 0))
        bg = pygame.image.load("./assets/game_bg.png")
        screen.blit(bg, bg.get_rect())

        mx, my = pygame.mouse.get_pos()

        button_4 = pygame.Rect(20, height - 70, 150, 50)
        if button_4.collidepoint((mx, my)):
            if click:
                main_menu()

        # pygame.draw.rect(screen, (186, 121, 125), button_4, 25, 10)
        draw_text('challenge', gen_font(30), (0, 0, 0), screen, 20, 20)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    is_running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def free_play():
    running = True
    while running:
        screen.fill((0, 0, 0))
        bg = pygame.image.load("./assets/game_bg.png")
        screen.blit(bg, bg.get_rect())

        mx, my = pygame.mouse.get_pos()

        button_5 = pygame.Rect(20, height - 70, 150, 50)
        if button_5.collidepoint((mx, my)):
            if click:
                main_menu()

        # pygame.draw.rect(screen, (186, 121, 125), button_5, 25, 10)
        draw_text('free play', gen_font(30), (0, 0, 0), screen, 20, 20)
        # draw_text('back', gen_font(30), (0, 0, 0), screen, 30, 20)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    main_menu()

