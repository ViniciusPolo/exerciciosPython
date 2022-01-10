#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('trilha.mp3')
#não executou a musica mas não deu erro
pygame.mixer.music.play()
pygame.event.wait()