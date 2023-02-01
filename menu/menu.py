import pygame
from pygame.locals import *
pygame.init()


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def mainMenu():
    window = pygame.display.set_mode((0, 0), FULLSCREEN)
    BackGround = Background('sprites/background_menu.jpeg', [0, 0])

    runing = True
    while runing:
        mousePose = pygame.mouse.get_pos()

        window.fill((0, 0, 0))
        window.blit(pygame.transform.scale(
            BackGround.image, (window.get_width(), window.get_height())), (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                runing = False

        pygame.display.update()

    pygame.quit()


mainMenu()
