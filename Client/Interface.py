import pygame
from GameLoop import GameLoop
#Importation des différents fichiers utile


pygame.init() #Initialisation de pygame

pygame.display.set_caption("Quiz") #Nom de la fenêtre

GL = GameLoop()
GL.run()
