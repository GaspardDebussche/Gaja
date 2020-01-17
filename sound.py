import pygame

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Downloads/Cat_Meow_2-Cat_Stevens-2034822903.mp3")
print("faccela")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    pass