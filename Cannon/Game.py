import pygame
from pygame.draw import *
import numpy as np
from random import randint


pygame.init()
# задание размера экрана
xsc = 600
ysc = 600
FPS = 30
SCREEN_SIZE = [xsc, ysc]
screen = pygame.display.set_mode((xsc, ysc))
pygame.mixer.init()
pygame.display.set_caption('Cannon')
# заливка экрана цветом
screen.fill((76, 84, 71))
clock = pygame.time.Clock()
finished = False


def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Cannon(pygame.sprite.Sprite):
    def __init__(self, xg, yg, angle=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 40))
        self.rect = self.image.get_rect()
        self.image.fill((83, 114, 63))
        self.rect.bottom = yg*0.95
        self.rect.centerx = xg/2
        self.healf = 5
        self.speedx = 0
        self.angle = angle
        self.up_gun = [self.rect.centerx, self.rect.bottom-50]

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx

    def set_angle(self, target_pos):
        """
        Sets gun's direction to target position.
        """
        self.angle = np.arctan2(target_pos[1] - self.rect.bottom, target_pos[0] - self.rect.centerx)

    def strike(self):

        bullet = Shell(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Shell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(rand_color())
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -30

    def update(self):

        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Target(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(rand_color())
        self.rect = self.image.get_rect()
        self.rect.x = randint(20, 580)
        self.rect.y = randint(20, 480)
        self.speedy = randint(5, 15)
        self.healf = 4
        self.flag_x = 0
        self.flag_y = 0

    def update(self):
        if self.flag_x == 0:
            self.rect.x += self.speedy
        else:
            self.rect.x -= self.speedy
        if self.flag_y == 1:
            self.rect.y += self.speedy
        else:
            self.rect.y -= self.speedy

        if self.rect.x > xsc - 15:
            self.flag_x = 1
            self.speedy = randint(5, 15)
        elif self.rect.x < 15:
            self.flag_x = 0
            self.speedy = randint(5, 15)
        if self.rect.y > ysc  - 15:
            self.flag_y = 0
            self.speedy = randint(5, 15)
        elif self.rect.y < 15:
            self.flag_y = 1
            self.speedy = randint(5, 15)


# Цикл игры
all_sprites = pygame.sprite.Group()
gun = Cannon(xsc, ysc)
all_sprites.add(gun)
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
for i in range(6):
    m = Target()
    all_sprites.add(m)
    mobs.add(m)
runGame = True

while runGame:
    clock.tick(FPS)

    pygame.display.update()
    # Отслеживание событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gun.strike()
            if event.key == pygame.K_a:
                gun.speedx = -8
            if event.key == pygame.K_d:
                gun.speedx = 8
        if pygame.mouse.get_focused():
            mouse_pos = pygame.mouse.get_pos()
            gun.set_angle(mouse_pos)

    all_sprites.update()
    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(gun, mobs, False)
    if hits:
        runGame = False
    # Проверка столкновения пули с мишенью
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Target()
        all_sprites.add(m)
        mobs.add(m)
    # Рендеринг
    screen.fill((76, 84, 71))
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


# Выход из игры:
pygame.quit()
