# Wesley Fernandes
# python simple pendulum with pygame

import pygame
import math
import os
from chime import Chime

# VARIABLES
width, height = 1200, 900  # set the width and height of the window
# (you can increase or decrease if you want to, just remind to keep even numbers)
Out = False  # if True,out of while loop, and close pygame
acceleration = False  # when true it allow us to find the acceleration and damping for the pendulum
length = 1  # the length between the ball and the support
angle = 0  # the angle that you begin when click in window
vel = 0  # velocity that angle is increased and damped
Aacc = 0  # acceleration

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chime to Play!")

WHITE = (255, 255, 255)
FPS = 30

pygame.font.init()

# COLORS
white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)

# BEFORE START
pygame.init()
clock = pygame.time.Clock()

class Cursor(pygame.sprite.Sprite):

    def __init__(self):
        super(Cursor, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((255, 0, 255))
        self.surf.set_colorkey((255, 0, 255))
        self.rect = pygame.draw.circle(self.surf, (0, 0, 255), (20, 20), 20, width=2)

    def update(self, mouse_pos):
        self.rect.move_ip(mouse_pos[0] - self.rect.centerx + 15, mouse_pos[1] - self.rect.centery + 15)

def gen_font(size: int):
    font = pygame.font.Font("./assets/KitNoms-Regular.ttf", size)
    return font


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class ball(object):

    def __init__(self, XY, radius):  # Set ball coordenates and radius
        self.x = XY[0]
        self.y = XY[1]
        self.radius = radius

    def draw(self, bg, ang):  # Draw circle and line based on XY coordinates
        pygame.draw.lines(bg, black, False, [(width / 2, 50), (self.x, self.y)], 2)
        pygame.draw.circle(bg, black, (self.x, self.y), self.radius)
        pygame.draw.circle(bg, Dark_red, (self.x, self.y), self.radius - 2)
        img = pygame.image.load(os.path.join('assets', f'chime{1}.png'))
        height = img.get_size()[1]
        rotated_image = pygame.transform.rotate(img, angle * 180 / math.pi)
        new_rect = rotated_image.get_rect(center=((width / 2) + (math.sin(angle) * (height / 2)), (math.cos(angle) * (height / 2)) + 100))
        screen.blit(rotated_image, new_rect)

def angle_Length():  # Send back the length and angle at the first click on screen
    length = math.sqrt(math.pow(pendulum.x - width / 2, 2) + math.pow(pendulum.y - 50, 2))
    angle = math.asin((pendulum.x - width / 2) / length)
    return angle, length


def get_path(first_angle, length):  # with angle and length calculate x and y position
    pendulum.x = round(width / 2 + length * math.sin(angle))
    pendulum.y = round(50 + length * math.cos(angle))


def redraw():  # Clean up the screen and start a new grid and new frame of pendulum with new coordinates
    pendulum.draw(screen, angle)
    pygame.display.update()


pendulum = ball((int(width / 2), -100), 5)  # I start the class with some random coordinates

while not Out:
    clock = pygame.time.Clock()
    pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
    run = True
    chimes = [Chime(0), Chime(1), Chime(2), Chime(3), Chime(4)]

    interactables = pygame.sprite.Group()

    cursor = Cursor()

    for chime in chimes:
        interactables.add(chime)
        chime.init_chimes()

    def draw_window(state):
        if state != 'main':
            for chime in chimes:
                screen.blit(chime.img, chime.cords)
                chime.update(pygame.key.get_pressed())
                chime.run_sim(screen)


    screen.blit(cursor.surf, cursor.rect)
    pygame.display.flip()
    pygame.display.update()

    # main, challenge, free
    game_state = 'main'
    pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/twinkle_song.mp3'), loops=-1)
    cursor_on = False
    main_bg = pygame.image.load("./assets/main_menu_bg.png")
    game_bg = pygame.image.load("./assets/game_bg.png")
    header = pygame.image.load('./assets/chime_header.png')
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == 'main':
                    mx, my = pygame.mouse.get_pos()

                    button_1 = pygame.Rect(width / 2 - 150, height / 2 - 75, 300, 100)
                    button_2 = pygame.Rect(width / 2 - 150, height / 2 + 75, 300, 100)
                    button_3 = pygame.Rect(width / 2 - 75, height / 2 + 225, 150, 75)

                    if button_1.collidepoint((mx, my)):
                        game_state = 'challenge'
                        pygame.mixer.stop()
                        continue
                    if button_2.collidepoint((mx, my)):
                        game_state = 'free'
                        pygame.mixer.stop()
                        continue
                    if button_3.collidepoint((mx, my)):
                        run = False
                        pygame.quit()
                elif game_state in ['challenge', 'free']:
                    mx, my = pygame.mouse.get_pos()
                    pendulum = ball(pygame.mouse.get_pos(), 15)  # or
                    angle, length = angle_Length()  # click the mouse button
                    acceleration = True  #

                    redraw()
                    button_4 = pygame.Rect(20, height - 70, 150, 50)
                    if button_4.collidepoint((mx, my)):
                        game_state = 'main'
                        # background music in main_menu
                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/twinkle_song.mp3'), loops=-1)
                        continue

        if game_state == 'main':
            screen.blit(main_bg, main_bg.get_rect())
            draw_text('Brought to you by "TEAM SAME" (Sarah, Andrew, Mengting, Eric)', gen_font(30), (0, 0, 0),
                      screen, 20, height - 35)

        elif game_state == 'challenge':
            screen.blit(game_bg, game_bg.get_rect())
            screen.blit(header, ((width-header.get_width())/2, 0))
            draw_text('challenge', gen_font(30), (0, 0, 0), screen, 20, 20)
            pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/wind_and_pad.mp3'), loops=-1)
        elif game_state == 'free':
            screen.blit(game_bg, game_bg.get_rect())
            screen.blit(header, ((width - header.get_width()) / 2, 0))
            draw_text('free play', gen_font(30), (0, 0, 0), screen, 20, 20)
            pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/wind_and_pad.mp3'), loops=-1)
        cursor.update(mouse_pos=pygame.mouse.get_pos())
        draw_window(game_state)
        collisions = pygame.sprite.spritecollide(cursor, interactables, dokill=False)
        if len(collisions) > 0:
            if game_state != 'main' and not cursor_on:
                cursor_on = True
                pygame.mixer.Channel(collisions[0].id).play(pygame.mixer.Sound(collisions[0].sound))
                num = collisions[0].id
                pygame.mixer.Channel(num).play(pygame.mixer.Sound(collisions[0].sound))

        else:
            cursor_on = False

        if acceleration:  # Increase acceleration and damping in the pendulum moviment
            Aacc = -0.02 * math.sin(angle)
            vel += Aacc
            vel *= 0.99  # damping factor
            angle += vel
            get_path(angle, length)
        redraw()

    pygame.quit()

    # If changed, maybe, could be a good idea change some values at acceleration

if __name__ == '__main__':
    main()
