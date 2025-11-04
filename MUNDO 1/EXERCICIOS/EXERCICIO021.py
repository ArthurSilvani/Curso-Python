# faça um programa em python que abra e reproduza o audio de
#um arquivo MP3

import pygame

pygame.mixer.init()
pygame.mixer.music.load("helipa.mp3.mp3")
pygame.mixer.music.play()

input()
pygame.event.wait()