import pygame
from pygame.locals import *
import subprocess
output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
resolution_x, resolution_y = output.decode("utf-8").split("x")[0], output.decode("utf-8").split("x")[1]
pygame_y = int(resolution_y) - 200.0
pygame_x = int(pygame_y) / 12.0 * 16.0

class Leaf:
    def __init__(self, img, x, y, num):
        self.img = img
        self.x = x * int(pygame_x / 16.0)
        self.y = y * int(pygame_y / 12.0)
        self.num = num
        pygame.init()

    def get_image(self):
        img_surface = pygame.Surface((int(pygame_x / 16.0)-2, int(pygame_y / 12.0)-2), pygame.SRCALPHA, 32)
        img_surface = img_surface.convert_alpha()
        font = pygame.font.SysFont('Sans', int(pygame_y / 12.0 / 3))
        text = font.render(str(self.num), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (int(pygame_y / 12.0 / 2), int(pygame_y / 12.0 / 2.5))
        img_surface.blit(self.img, (0, 0))
        img_surface.blit(text, text_rect)
        return img_surface
