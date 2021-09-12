import pygame

from audio import c6, Challenge
from chime import Chime
import math
import os

# VARIABLES
WIDTH, HEIGHT = 1200, 900  # set the width and height of the window
# (you can increase or decrease if you want to, just remind to keep even numbers)
Out = False  # if True,out of while loop, and close pygame
acceleration = False  # when true it allow us to find the acceleration and damping for the pendulum
length = 1  # the length between the ball and the support
angle = 0  # the angle that you begin when click in window
vel = 0  # velocity that angle is increased and damped
Aacc = 0  # acceleration
img = pygame.image.load(os.path.join('assets', f'chime{1}.png'))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chime to Play!")
WHITE = (255, 255, 255)
FPS = 30

pygame.font.init()

# BEFORE START
pygame.init()
clock = pygame.time.Clock()

# COLORS
white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)

class ball(object):

    def __init__(self, XY, radius):  # Set ball coordenates and radius
        self.x = XY[0]
        self.y = XY[1]
        self.radius = radius

    def draw(self, bg, ang, num):  # Draw circle and line based on XY coordinates
        img = pygame.image.load(os.path.join('assets', f'chime{1}.png'))
        pygame.draw.lines(bg, black, False, [(1100-(img.get_size()[0]+100)*(5-0), 250), (self.x, self.y)], 2)
        height = img.get_size()[1]
        rotated_image = pygame.transform.rotate(img, angle * 180 / math.pi)
        new_rect = rotated_image.get_rect(center=(1100-(img.get_size()[0]+100)*(5-num) + (math.sin(angle) * (height / 2)), (math.cos(angle) * (height / 2)) + 300))
        screen.blit(rotated_image, new_rect)

def angle_Length():  # Send back the length and angle at the first click on screen
    length = math.sqrt(math.pow(pendulum.x - 1100-(img.get_size()[0]+100)*(5-0), 2) + math.pow(pendulum.y - 250, 2))
    angle = math.asin((pendulum.x - 250) / length)
    return angle, length


def get_path(first_angle, length):  # with angle and length calculate x and y position
    pendulum.x = round(WIDTH / 2 + length * math.sin(angle))
    pendulum.y = round(50 + length * math.cos(angle))


def redraw():  # Clean up the screen and start a new grid and new frame of pendulum with new coordinates
    pendulum.draw(screen, angle,0)
    pygame.display.update()
    pendulum1.draw(screen, angle, 1)
    pendulum2.draw(screen, angle, 2)
    pendulum3.draw(screen, angle, 3)
    pendulum4.draw(screen, angle, 4)


pendulum = ball((int(WIDTH / 2), -300), 200)  # I start the class with some random coordinates
pendulum1 = ball((int(WIDTH / 2), -200), 250)
pendulum2 = ball((int(WIDTH / 2), -100), 250)
pendulum3 = ball((int(WIDTH / 2), 0), 250)
pendulum4= ball((int(WIDTH / 2), 100), 250)
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

while not Out:
    clock = pygame.time.Clock()
    pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
    run = True
    chimes = [Chime(0), Chime(1), Chime(2), Chime(3), Chime(4)]

    interactables = pygame.sprite.Group()

    cursor = Cursor()
    score = 0

    for chime in chimes:
        interactables.add(chime)
        chime.init_chimes()

    def draw_window(state):
        if state != 'main':
            if state == 'challenge':
                draw_text(f'SCORE - {score}', gen_font(50), (0, 0, 0), screen, 0, 300)
                if challenge is not None:
                    for chime in chimes:
                        screen.blit(chime.img, chime.cords)
                        chime.update(pygame.key.get_pressed())
                        chime.run_sim(screen)
                    if challenge.playing:
                        draw_text(f'LISTEN', gen_font(50), (0, 0, 0), screen, 500, 200)
            else:
                for chime in chimes:
                    screen.blit(chime.img, chime.cords)
                    chime.update(pygame.key.get_pressed())
                    pygame.draw.rect(chime.surf, (0, 0, 0), chime.rect)
                    chime.run_sim(screen)
        screen.blit(cursor.surf, cursor.rect)

    # main, challenge, free
    game_state = 'main'
    pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/twinkle_song.mp3'), loops=-1)
    cursor_on = False
    main_bg = pygame.image.load("./assets/main_menu_bg.png")
    game_bg = pygame.image.load("./assets/game_bg.png")
    header = pygame.image.load('./assets/chime_header.png')
    challenge = None
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == 'main':
                    mx, my = pygame.mouse.get_pos()

                    button_1 = pygame.Rect(WIDTH / 2 - 150, HEIGHT / 2 - 75, 300, 100)
                    button_2 = pygame.Rect(WIDTH / 2 - 150, HEIGHT / 2 + 75, 300, 100)
                    button_3 = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 2 + 225, 150, 75)

                    if button_1.collidepoint((mx, my)):
                        game_state = 'challenge'
                        pygame.mixer.Channel(7).stop()
                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/wind_and_pad.mp3'), loops=-1)
                        challenge = Challenge()
                        continue
                    if button_2.collidepoint((mx, my)):
                        game_state = 'free'
                        pygame.mixer.Channel(7).stop()
                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/wind_and_pad.mp3'), loops=-1)
                        continue
                    if button_3.collidepoint((mx, my)):
                        run = False
                        pygame.quit()
                elif game_state in ['challenge', 'free']:
                    mx, my = pygame.mouse.get_pos()
                    pendulum = ball(pygame.mouse.get_pos(), 15)  # or
                    pendulum1 = ball(pygame.mouse.get_pos(), 5)
                    pendulum2 = ball(pygame.mouse.get_pos(), 5)
                    pendulum3 = ball(pygame.mouse.get_pos(), 5)
                    pendulum4 = ball(pygame.mouse.get_pos(), 5)
                    angle, length = angle_Length() # click the mouse button
                    # angle = math.sin(math.pi/10)
                    acceleration = True

                    button_4 = pygame.Rect(20, HEIGHT - 70, 150, 50)
                    if button_4.collidepoint((mx, my)):
                        game_state = 'main'
                        # background music in main_menu
                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/twinkle_song.mp3'), loops=-1)
                        continue

        if game_state == 'main':
            screen.blit(main_bg, main_bg.get_rect())
            draw_text('Brought to you by "TEAM SAME" (Sarah, Andrew, Mengting, Eric)', gen_font(30), (0, 0, 0),
                      screen, 20, HEIGHT - 35)

        elif game_state == 'challenge':
            screen.blit(game_bg, game_bg.get_rect())
            screen.blit(header, ((WIDTH-header.get_width())/2, 0))
            draw_text('challenge', gen_font(30), (0, 0, 0), screen, 20, 20)

        elif game_state == 'free':
            screen.blit(game_bg, game_bg.get_rect())
            screen.blit(header, ((WIDTH - header.get_width()) / 2, 0))
            draw_text('free play', gen_font(30), (0, 0, 0), screen, 20, 20)

        cursor.update(mouse_pos=pygame.mouse.get_pos())
        collisions = pygame.sprite.spritecollide(cursor, interactables, dokill=False)

        draw_window(game_state)

        if len(collisions) > 0:
            if game_state == 'challenge' and not cursor_on and challenge is not None and not challenge.playing:
                cursor_on = True
                num = collisions[0].id
                pygame.mixer.Channel(num).play(pygame.mixer.Sound(collisions[0].sound))
                if challenge.played_note(num):
                    challenge.play_next()
                    score = challenge.score
                else:
                    score = challenge.score
                    # challenge = None

            elif game_state == 'free' and not cursor_on:
                cursor_on = True
                num = collisions[0].id
                pygame.mixer.Channel(num).play(pygame.mixer.Sound(collisions[0].sound))
        else:
            cursor_on = False

        if acceleration:
            Aacc = -0.02 * math.sin(angle)
            vel += Aacc
            vel *= 0.99  # damping factor
            angle += vel
            get_path(angle, length)
        redraw()
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
