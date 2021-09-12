import pygame

from chime import Chime

WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chime to Play!")

WHITE = (255, 255, 255)
FPS = 30


class Cursor(pygame.sprite.Sprite):

    def __init__(self):
        super(Cursor, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((255, 0, 255))
        self.surf.set_colorkey((255, 0, 255))
        self.rect = pygame.draw.circle(self.surf, (0, 0, 255), (20, 20), 20, width=2)

    def update(self, mouse_pos):
        self.rect.move_ip(mouse_pos[0] - self.rect.centerx+15, mouse_pos[1] - self.rect.centery+15)


def main():
    clock = pygame.time.Clock()
    pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
    run = True
    chimes = [Chime(), Chime(), Chime(), Chime(), Chime()]

    interactables = pygame.sprite.Group()

    cursor = Cursor()

    for chime in chimes:
        interactables.add(chime)
        chime.init_chimes()

    def draw_window():
        screen.fill(WHITE)

        for chime in chimes:
            screen.blit(chime.img, chime.cords)
            chime.update(pygame.key.get_pressed())
            chime.run_sim(screen)
        screen.blit(cursor.surf, cursor.rect)

        pygame.display.flip()
        pygame.display.update()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        cursor.update(mouse_pos=pygame.mouse.get_pos())
        draw_window()
        if pygame.sprite.spritecollideany(cursor, interactables):
            print('touching')

    pygame.quit()


if __name__ == '__main__':
    main()
