# -*- coding: utf-8 -*-

""" IMPORTS """

import pygame

""" SOUND MANAGEMENT """

pygame.mixer.init()

#while pygame.mixer.music.get_busy() == True:
#    pass

def sound_management(state):
    print("Voice state: {}".format(state))
    if state==-1:
        pygame.mixer.music.load("/home/pi/Documents/Gaja/sounds/bad.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

    if state==1:
        pygame.mixer.music.load("/home/pi/Documents/Gaja/sounds/normal.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

    if state==2:
        pygame.mixer.music.load("/home/pi/Documents/Gaja/sounds/good.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()