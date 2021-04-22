import pygame
import numpy as np
from random import randint
from os import path

img_dir = path.join(path.dirname(__file__), 'C:\\Users\\ВАНЯ\\Proba-2021\\img')

pygame.init()
# задание размера экрана
xsc = 600
ysc = 600
FPS = 35
SCREEN_SIZE = [xsc, ysc]
screen = pygame.display.set_mode((xsc, ysc))
pygame.mixer.init()
pygame.display.set_caption('Cannon')


background = pygame.image.load(path.join(img_dir, "C:\\Users\\ВАНЯ\\Proba-2021\\img\\back.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "C:\\Users\\ВАНЯ\\Proba-2021\\img\\playerShip1_orange.png")).convert()
bad_img = pygame.image.load(path.join(img_dir, "C:\\Users\\ВАНЯ\\Proba-2021\\img\\playerShip1_blue.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "C:\\Users\\ВАНЯ\\Proba-2021\\img\\Lasers\\laserGreen10.png")).convert()
bomb_img = pygame.image.load(path.join(img_dir, "C:\\Users\\ВАНЯ\\Proba-2021\\img\\Lasers\\laserBlue12.png")).convert()
# Рендеринг
screen.fill((0,  0, 0))
screen.blit(background, background_rect)


clock = pygame.time.Clock()
finished = False


def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Cannon(pygame.sprite.Sprite):
    def __init__(self, xg, yg, angle=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = 20
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

    def strike(self):

        bullet = Shell(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Shell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image = pygame.transform.scale(bullet_img, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -25

    def update(self):

        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Target(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.transform.rotate(bad_img, 180), (50, 35))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.centerx = randint(20, 580)
        self.rect.bottom = randint(-50, 0)
        self.speedy = randint(1, 12)
        self.healf = 4
        self.flag_x = randint(0, 2)
        self.flag_y = randint(0, 2)

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
        if self.rect.y > 0.75*ysc - 15:
            self.flag_y = 0
            self.speedy = randint(5, 15)
        elif self.rect.y < 15:
            self.flag_y = 1
            self.speedy = randint(5, 15)

        k = randint(0, 1000)
        if k < 10:
            bomb = Bomb(self.rect.x, self.rect.y)
            all_sprites.add(bomb)
            bombs.add(bomb)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bomb_img, (8, 15))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = randint(5, 10)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom > ysc:
            self.kill()


# Цикл игры
all_sprites = pygame.sprite.Group()
background = pygame.image.load(path.join(img_dir, "C:\\Users\\ВАНЯ\\Proba-2021\\img\\back.png")).convert()
background_rect = background.get_rect()
all_sprites.draw(screen)
gun = Cannon(xsc, ysc)
all_sprites.add(gun)
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bombs = pygame.sprite.Group()
for i in range(6):
    m = Target()
    all_sprites.add(m)
    mobs.add(m)
runGame = True

while runGame:
    clock.tick(FPS)

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

    all_sprites.update()
    screen.fill((0, 0, 0))
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.update()

    # Проверка, не ударил ли моб игрокa
    hits = pygame.sprite.spritecollide(gun, bombs, False)
    if hits:
        runGame = False
    # Проверка столкновения пули с мишенью
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Target()
        all_sprites.add(m)
        mobs.add(m)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


# Выход из игры:
pygame.quit()
