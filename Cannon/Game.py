import pygame
from pygame.draw import *
import numpy as np
from random import randint


pygame.init()
# задание размера экрана
xsc = 600
ysc = 600
FPS = 30
screen = pygame.display.set_mode((xsc, ysc))
pygame.display.set_caption('Cannon')
# заливка экрана цветом
screen.fill((76, 84, 71))
pygame.display.update()
clock = pygame.time.Clock()
finished = False


class Cannon:
    def __init__(self, xg, yg):
        self.gun_x = xg/2
        self.gun_y = yg*0.95
        self.healf = 5
        self.color_down = (83, 114, 63)
        self.color_up = (242, 186, 53)
        self.color_gan = (240, 50, 20)
        self.angle = 90

    def draw(self):
        screen_gun = pygame.Surface((30, 10))
        screen_gun.set_colorkey((76, 84, 71))
        rect(screen_gun, self.color_gan, (0, 0, 30, 10))
        surf2 = pygame.transform.rotate(screen_gun, self.angle)
        screen.blit(surf2, [self.gun_x-4, self.gun_y-35])
        rect(screen, self.color_down, [self.gun_x-30, self.gun_y-5, 60, 20])
        polygon(screen, self.color_up, ([self.gun_x-25, self.gun_y-5],
                                               [self.gun_x-18, self.gun_y-18],
                                               [self.gun_x+18, self.gun_y-18],
                                               [self.gun_x+25, self.gun_y-5]))


class Shell:
    pass


class Target:
    def __init__(self):
        self.xg = randint(20, 580)
        self.yg = randint(20, 480)
        self.rg = randint(10, 30)
        self.sx = randint(1, 3)
        self.sy = randint(1,3)
        self.healf = 4
        self.color = (randint(20, 250), randint(20, 250), randint(20, 250))
        self.flag_x = 0
        self.flag_y = 0

    def draw(self):
        circle(screen, self.color, [self.xg, self.yg], self.rg)

    def get_x_y(self):
        if self.flag_x == 0:
            self.xg += self.sx
        else:
            self.xg -= self.sx
        if self.flag_y == 0:
            self.yg += self.sy
        else:
            self.yg -= self.sy

        if self.xg > xsc - self.rg:
            self.flag_x = 1
            self.sx = randint(5, 15)
        elif self.xg < self.rg:
            self.flag_x = 0
            self.sx = randint(5, 15)
        if self.yg > ysc - 100 - self.rg:
            self.flag_y = 1
            self.sy = randint(5, 15)
        elif self.yg < self.rg:
            self.flag_y = 0
            self.sy = randint(5, 15)









# Цикл игры
Gun = Cannon(xsc, ysc)
Target_list = []
target_A = Target()
target_B = Target()
target_C = Target()
target_D = Target()
Target_list.append(target_A)
Target_list.append(target_B)
Target_list.append(target_C)
Target_list.append(target_D)

runGame = True
while runGame:
    clock.tick(FPS)
    Gun.draw()
    for i in Target_list:
        i.draw()
        i.get_x_y()
    pygame.display.update()
    # Отслеживание событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                Gun.angle += 5
            elif event.key == pygame.K_e:
                Gun.angle -= 5
    screen.fill((76, 84, 71))

# Выход из игры:
pygame.quit()
