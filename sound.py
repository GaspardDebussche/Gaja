# -*- coding: utf-8 -*-

""" IMPORTS """

import pygame

""" SOUND MANAGEMENT """

pygame.mixer.init()


def sound_management(state):
    print("Voice state: {}".format(state))
    if state == -1:
        pygame.mixer.music.load("/home/pi/Documents/Gaja/sounds/bad1.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass

    if state == 1:
        pygame.mixer.music.load("/home/pi/Documents/Gaja/sounds/normal.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass

    if state == 2:
        pygame.mixer.music.load("/home/pi/Documents/Gaja/sounds/good.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass