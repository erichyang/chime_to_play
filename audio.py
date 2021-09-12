import pygame

pygame.mixer.init(44100, -16, 2, 2048)

# section 3 is faster
song_note = [('e6', 'e6', 'e6', 'd6', 'e6', 'g6', 'e6', 'd6', 'd6', 'd6', 'c6', 'd6', 'g6'),
             ('c6', 'd6', 'g6', 'e6', 'g6', 'a6', 'g6', 'a6', 'e6', 'd6', 'e6', 'd6', 'c6'),
             ('e6', 'e6', 'g6', 'e6', 'g6', 'e6', 'g6', 'd6', 'd6', 'e6', 'd6', 'e6', 'd6',
              'e6', 'd6', 'g6', 'd6', 'e6', 'g6', 'e6', 'e6', 'ge', 'd6', 'c6'),
             ('c6', 'd6', 'g6', 'e6', 'g6', 'a6', 'g6', 'a6', 'e6', 'd6', 'e6', 'd6', 'c6')]

def c6():
    pygame.mixer.music.load("./assets/audio/C6.mp3")
    pygame.mixer.music.play(-1)


def d6():
    pygame.mixer.music.load(r"./assets/audio/D6.mp3")
    pygame.mixer.music.play(-1)


def e6():
    pygame.mixer.music.load(r"./assets/audio/E6.mp3")
    pygame.mixer.music.play(-1)


def g6():
    pygame.mixer.music.load(r"./assets/audio/g6.mp3")
    pygame.mixer.music.play(-1)


def a6():
    pygame.mixer.music.load(r"./assets/audio/a6.mp3")
    pygame.mixer.music.play(-1)


# from playsound import playsound
#
#
# def c6():
#     playsound('/assets/audio/c6.mp3')
#
#
# def d6():
#     playsound('/assets/audio/d6.mp3')
#
#
# def e6():
#     playsound('/assets/audio/e6.mp3')
#
#
# def g6():
#     playsound('/assets/audio/g6.mp3')
#
#
# def a6():
#     playsound('/assets/audio/a6.mp3')


def main():
    c6()


if __name__ == '__main__':
    main()
