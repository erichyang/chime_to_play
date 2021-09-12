import pygame

from audio import c6, Challenge
from chime import Chime

WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chime to Play!")

WHITE = (255, 255, 255)
FPS = 30

pygame.font.init()


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


def main():
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
        pygame.display.flip()
        pygame.display.update()

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
                        score = 0
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

                    button_4 = pygame.Rect(20, HEIGHT - 70, 150, 50)
                    if button_4.collidepoint((mx, my)):
                        game_state = 'main'
                        # background music in main_menu
                        pygame.mixer.stop()
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
                print(num)
                score = challenge.score
                if not challenge.played_note(num):
                    challenge = None
                    pygame.display.flip()
            elif game_state == 'free' and not cursor_on:
                cursor_on = True
                num = collisions[0].id
                pygame.mixer.Channel(num).play(pygame.mixer.Sound(collisions[0].sound))
        else:
            cursor_on = False

    pygame.quit()


if __name__ == '__main__':
    main()
