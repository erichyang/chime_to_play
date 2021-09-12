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
flattened = [item for sublist in song_note for item in sublist]

num_to_note = [a6, c6, d6, e6, g6]


class Challenge:
    def __init__(self):
        self.score = 0
        self.track = 0
        self.index = 0
        self.length = 0
        self.current = []
        self.playing = False
        self.play_next()

    def played_note(self, chime_num):
        self.current.append(num_to_note[chime_num])
        if len(self.current) < self.length:
            return True
        for index, note in enumerate(self.current):
            if flattened[index] is not note:
                self.current = []
                return False
        self.score += 1
        if len(song_note[self.track]) == self.index:
            self.track += 1
            self.index = 0
        else:
            self.index += 1
        self.current = []
        self.play_next()
        return True

    def play_next(self):
        event = threading.Event()
        thread = threading.Thread(target=self.loop, args=(event, self.track, self.index))
        thread.start()

    def loop(self, event, track, index):
        self.playing = True
        event.wait(1.5)
        song = song_note[track]
        wait = 0.9
        if track == 2:
            wait = 0.45
        self.length = 0
        if track > 0:
            for m in range(0, track):
                for note in song_note[m]:
                    print(note.__name__)
                    note()
                    event.wait(0.9)
                    self.length += 1
        for note in range(0, index+1):
            print(song[note].__name__)
            song[note]()
            event.wait(wait)
            self.length += 1
        self.playing = False


def main():
    # ch = Challenge()
    # ch.play_next()
    # print(ch.score, ch.track, ch.index)
    # time.sleep(10)
    pygame.mixer.Channel(7).play(pygame.mixer.Sound('./assets/audio/wind_and_pad.mp3'), loops=-1)
    time.sleep(10)


if __name__ == '__main__':
    main()
