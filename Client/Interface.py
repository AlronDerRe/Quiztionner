import pygame
from GameLoop import GameLoop
#Importation des différents fichiers utile


pygame.init() #Initialisation de pygame

pygame.display.set_caption("Quiz") #Nom de la fenêtre

GL = GameLoop() #Création de la boucle de jeu et de ses éléments
GL.run() #On lance le jeu.
