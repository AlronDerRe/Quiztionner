import pygame
from pygame.locals import *

def text():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    text = ""
    font = pygame.font.Font('MyriadPro.otf', 45)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    text += evt.unicode
                elif evt.unicode.isdigit():
                    text += evt.unicode
                elif evt.key == K_BACKSPACE:
                    text = text[:-1]
                elif evt.key == K_SPACE:
                    text += " "
                #elif evt.key == K_RETURN:
                    #text += "YOLO"
                elif evt.unicode.encode('utf-8'):
                    text += evt.unicode
            elif evt.type == QUIT:
                return
        screen.fill ((52,73,94))
        block = font.render(text, True, (236, 240, 241))
        rect = block.get_rect()
        rect.center = (400,300)
        screen.blit(block, rect)
        pygame.display.flip()

if __name__ == "__main__":
    text()
