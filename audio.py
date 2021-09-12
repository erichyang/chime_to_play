import asyncio
import threading
import time

import pygame

pygame.mixer.init(44100, -16, 2, 2048)


def c6():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(r"./assets/audio/C6.mp3"))


def d6():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(r"./assets/audio/D6.mp3"))


def e6():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound(r"./assets/audio/E6.mp3"))


def g6():
    pygame.mixer.Channel(3).play(pygame.mixer.Sound(r"./assets/audio/G6.mp3"))


def a6():
    pygame.mixer.Channel(4).play(pygame.mixer.Sound(r"./assets/audio/A6.mp3"))


# section 3 is faster
song_note = [(e6, e6, e6, d6, e6, g6, e6, d6, d6, d6, c6, d6, g6),
             (c6, d6, g6, e6, g6, a6, g6, a6, e6, d6, e6, d6, c6),
             (e6, e6, g6, e6, g6, e6, g6, d6, d6, e6, d6, e6, d6,
              e6, d6, g6, d6, e6, g6, e6, e6, g6, d6, c6),
             (c6, d6, g6, e6, g6, a6, g6, a6, e6, d6, e6, d6, c6)]


class Challenge:
    def __init__(self):
        self.score = 0
        self.track = 0
        self.index = 0

    def add_point(self):
        self.score += 1
        if len(song_note[self.track]) == self.index:
            self.track += 1
            self.index = 0
        else:
            self.index += 1

    def play_next(self):
        event = threading.Event()
        thread = threading.Thread(target=loop, args=(event, self.track, self.index))
        thread.start()


def loop(event, track, index):
    song = song_note[track]
    wait = 0.9
    if index == 3:
        wait = 0.45
    for note in range(0, index):
        song[note]()
        event.wait(wait)


def main():
    event = threading.Event()
    thread = threading.Thread(target=loop, args=(event, 0))
    thread.start()


if __name__ == '__main__':
    ch = Challenge()
    ch.play_next()
    ch.add_point()
    ch.play_next()
    time.sleep(10)

