import pygame
from random import randint, choice, random
from os import path

# Настройки экрана
pygame.init()
xsc = 600
ysc = 700
FPS = 35
SCREEN_SIZE = [xsc, ysc]
screen = pygame.display.set_mode((xsc, ysc))
pygame.mixer.init()
POWERUP_TIME = 5000

# Загрузка всех изображений
img_dir = path.join(path.dirname(__file__), 'C:\\Users\\User\\Proba-2021\\img')
snd_dir = path.join(path.dirname(__file__), 'snd')
Enemy = []
Enemy_ufo = []
background = pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\back.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\playerShip1_orange.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey((0, 0, 0))
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\"
                                                  "Enemies\\enemyRed1.png")).convert())
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\"
                                                  "Enemies\\enemyRed2.png")).convert())
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\"
                                                  "Enemies\\enemyRed5.png")).convert())
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\"
                                                "Proba-2021\\img\\Enemies\\enemyBlack1.png")).convert())
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\"
                                                "img\\Enemies\\enemyBlack2.png")).convert())
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\"
                                                "Enemies\\enemyBlack4.png")).convert())
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\"
                                                  "Enemies\\enemyBlue1.png")).convert())
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\"
                                                  "Enemies\\enemyBlue2.png")).convert())
Enemy.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\"
                                                  "Enemies\\enemyBlue3.png")).convert())
Enemy_ufo.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\ufoBlue.png")).convert())
Enemy_ufo.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\ufoGreen.png")).convert())
Enemy_ufo.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\ufoRed.png")).convert())
Enemy_ufo.append(pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\ufoYellow.png")).convert())
bullet_img = pygame.image.load(path.join(img_dir,
                                         "C:\\Users\\User\\Proba-2021\\img\\Lasers\\laserGreen10.png")).convert()
bomb_img = pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\img\\Lasers\\laserBlue12.png")).convert()
shoot_gun_sound = pygame.mixer.Sound(path.join(snd_dir, "C:\\Users\\User\\Proba-2021\\snd\\Laser_Shoot_gun.wav"))
shoot_bomb_sound = pygame.mixer.Sound(path.join(snd_dir, "C:\\Users\\User\\Proba-2021\\snd\\Laser_Shoot_bomb.wav"))
exp_sound = pygame.mixer.Sound(path.join(snd_dir, "C:\\Users\\User\\Proba-2021\\snd\\Explosion.wav"))
exp2_sound = pygame.mixer.Sound(path.join(snd_dir, "C:\\Users\\User\\Proba-2021\\snd\\Explosion2.wav"))
healf_snd = pygame.mixer.Sound(path.join(snd_dir, "C:\\Users\\User\\Proba-2021\\snd\\Explosion5.wav"))
explos_snd = [exp_sound, exp2_sound]
pygame.mixer.music.load(path.join(snd_dir, "C:\\Users\\User\\Proba-2021\\snd\\POL-fortress-short.wav"))

powerup_images = {}
powerup_images['live'] = pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\"
                                                              "img\\UI\\playerLife1_red.png")).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir, "C:\\Users\\User\\Proba-2021\\"
                                                             "img\\Power-ups\\powerupYellow_bolt.png")).convert()
live_sound = pygame.mixer.Sound(path.join(snd_dir, "C:\\Users\\User\\Proba-2021\\snd\\Powerup2.wav"))
power_sound = pygame.mixer.Sound(path.join(snd_dir, "C:\\Users\\User\\Proba-2021\\snd\\Powerup3.wav"))

pygame.mixer.music.set_volume(0.6)
explosion_anim = dict()
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['gun'] = []
for i in range(9):
    filename = "C:\\Users\\User\\Proba-2021\\img\\Explosive\\regularExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey((0, 0, 0))
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = "C:\\Users\\User\\Proba-2021\\img\\Explosive\\sonicExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey((0, 0, 0))
    explosion_anim['gun'].append(img)


# Игровые классы
class Cannon(pygame.sprite.Sprite):
    """
         Класс пушки. Отрисовка и движения игрока на экране.
         Вызов выстрела
    """
    def __init__(self, xg, yg, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.bottom = yg*0.98
        self.rect.centerx = xg/2
        self.healf = 3
        self.speedx = 0
        self.shoot_delay = 300
        self.last_shot = pygame.time.get_ticks()
        self.up_gun = [self.rect.centerx, self.rect.bottom-50]
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = xsc / 2
            self.rect.bottom = ysc * 0.98
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx
        if keystate[pygame.K_SPACE]:
            self.strike()
        # тайм-аут для бонусов
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

    def strike(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if not self.hidden:
                bullet = Shell(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_gun_sound.play()
            if self.power >= 2:
                bullets.remove(bullet)
                all_sprites.remove(bullet)
                bullet1 = Shell(self.rect.left, self.rect.centery)
                bullet2 = Shell(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_gun_sound.play()

    def hide(self):
        # временно скрыть игрока
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (xsc / 2, ysc + 200)


class Shell(pygame.sprite.Sprite):
    """
         Класс снаряда игрока
    """
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
    """
         Класс врагов. Перемещение, отрисовка и вызов бомбы
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Enemy[randint(0, len(Enemy) - 1)], (50, 35))
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
        if self.rect.y > 0.6*ysc:
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
            shoot_bomb_sound.play()


class TargetUfo(pygame.sprite.Sprite):
    """
         Класс врагов. Перемещение, отрисовка и вызов бомбы
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Enemy_ufo[randint(0, len(Enemy_ufo) - 1)], (50, 50))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.9 / 2)

        self.rect.bottom = randint(100, 400)
        self.speedy = randint(8, 18)
        self.healf = 4
        self.flag_x = randint(0, 2)
        self.flag_y = randint(0, 2)
        if self.flag_x == 0:
            self.rect.centerx = randint(-50, 0)
        else:
            self.rect.centerx = randint(xsc, xsc+50)

    def update(self):
        if self.flag_x == 0:
            self.rect.x += self.speedy
            if self.rect.x > xsc + 50:
                self.kill()
        else:
            self.rect.x -= self.speedy
            if self.rect.x < -50:
                self.kill()
        if self.flag_y == 0:
            self.rect.y += self.speedy/4
        else:
            self.rect.y -= self.speedy/4

        k = randint(0, 1000)
        if k < 100:
            bomb = Bomb(self.rect.x, self.rect.y)
            all_sprites.add(bomb)
            bombs.add(bomb)
            shoot_bomb_sound.play()


class Bomb(pygame.sprite.Sprite):
    """
        Класс бомбы. Отрисовка и перемещение
    """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bomb_img, (8, 15))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = randint(12, 20)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom > ysc:
            self.kill()


class PowerUp(pygame.sprite.Sprite):
    """
        Класс улучшений. Отрисовка и перемещение
    """
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self )
        self.type = choice(['live', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 8

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom > ysc:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    """
        Отрисовка взрывов
    """
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Функции вывода текста на экран
def draw_text(surf, text, size, x, y):
    """ Функция отрисовки  текста на экране
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (90, 203, 72))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_lives(surf, x, y, lives, img0):
    """Функция отрисовки жизней игрока на экране
    """
    for s in range(lives):
        img0_rect = img0.get_rect()
        img0_rect.x = x - 30 * s
        img0_rect.y = y
        surf.blit(img0, img0_rect)


def show_go_screen():
    """Функция, которая отрисовывает экран начала и окончания игры
    """
    screen.blit(background, background_rect)
    draw_text(screen, "NEW GAME!", 64, xsc / 2, ysc / 4)
    draw_text(screen, "Arrow keys move, Space to fire", 22,
              xsc / 2, ysc / 2)
    draw_text(screen, "Press a key to begin", 18, xsc / 2, ysc * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for ivent in pygame.event.get():
            if ivent.type == pygame.QUIT:
                pygame.quit()
            if ivent.type == pygame.KEYUP:
                waiting = False


# Первичные установки

score_max = open("C:\\Users\\User\\Proba-2021\\Cannon\\scroe.txt")
score_rec = int(score_max.read())
score_max.close()

pygame.display.set_caption('Cannon')
all_sprites = pygame.sprite.Group()
font_name = pygame.font.match_font('arial')
all_sprites.draw(screen)
gun = Cannon(xsc, ysc)
all_sprites.add(gun)
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bombs = pygame.sprite.Group()
powerups = pygame.sprite.Group()
score = 0
flag_mob = 0
wrag = 1
score_wall = 10
for i in range(2):
    m = Target()
    all_sprites.add(m)
    mobs.add(m)
    
clock = pygame.time.Clock()
pygame.mixer.music.play(loops=-1)
game_over = True
runGame = True

# главный цикл игры
while runGame:
    clock.tick(FPS)

    # Окно  Game Over  при окончании игры
    if game_over:
        score_max = open("C:\\Users\\User\\Proba-2021\\Cannon\\scroe.txt")
        score_rec = int(score_max.read())
        score_max.close()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        bombs = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        gun = Cannon(xsc, ysc)
        all_sprites.add(gun)
        for i in range(2):
            m = Target()
            all_sprites.add(m)
            mobs.add(m)
        score = 0
        flag_mob = 0
        wrag = 1
        score_wall = 10
        show_go_screen()
    # Вызов нло
    if score > score_wall:
        c = TargetUfo()
        all_sprites.add(c)
        mobs.add(c)
        score_wall += randint(60, 120)

    # добавление моба при наборе очков
    if score // 120 == wrag:
        flag_mob = 1
        score += 1
        wrag += 1
    if flag_mob == 1:
        m = Target()
        all_sprites.add(m)
        mobs.add(m)
        flag_mob = 0
    # Отслеживание событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                gun.speedx = -8
            if event.key == pygame.K_d:
                gun.speedx = 8
    # Рендеринг
    pygame.display.update()
    all_sprites.update()
    screen.fill((0, 0, 0))
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, xsc / 2, 10)
    draw_text(screen, "Record: "+str(score_rec), 20, 60, 10)
    draw_lives(screen, xsc - 30, 5, gun.healf,
               player_mini_img)
    # Проверка, не попала ли бомба в игрока
    hits = pygame.sprite.spritecollide(gun, bombs, True)
    for hit in hits:
        healf_snd.play()
        gun.healf -= 1
        death_explosion = Explosion(gun.rect.center, 'gun')
        all_sprites.add(death_explosion)
        gun.hide()
        gun.power = 1
    # Если игрок умер, игра окончена
    if gun.healf == 0 and not death_explosion.alive():
        game_over = True
        if score > score_rec:
            score_max = open("C:\\Users\\User\\Proba-2021\\Cannon\\scroe.txt", 'w')
            score_max.write(str(score))
            score_max.close()
    # Проверка столкновения пули с мишенью
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 10 if hit.__class__.__name__ == 'Target' else 20
        choice(explos_snd).play()
        exp = Explosion(hit.rect.center, 'lg')
        all_sprites.add(exp)
        if hit.__class__.__name__ == 'Target':
            m = Target()
            all_sprites.add(m)
            mobs.add(m)
        if hit.__class__.__name__ == 'TargetUfo':
            pow = PowerUp(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        if random() > 0.95:
            pow = PowerUp(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)

    hits = pygame.sprite.spritecollide(gun, powerups, True)
    for hit in hits:
        if hit.type == 'live':
            gun.healf += 1
            live_sound.play()
            if gun.healf >= 4:
                gun.healf = 4
        if hit.type == 'gun':
            gun.powerup()
            power_sound.play()

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

# Выход из игры:
pygame.quit()
