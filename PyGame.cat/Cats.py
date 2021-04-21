import pygame
from pygame.draw import *

pygame.init()
FPS = 15
xs = 700
ys = 950
screen = pygame.display.set_mode((xs, ys))
color_pol = [128, 128, 0]
color_wall = [184, 134, 11]
color_win1 = [176, 224, 230]
color_win2 = [0, 191, 255]
black = [0, 0, 0]
color_boll = [211, 211, 211]
color_cat = [254, 144, 43]
color_cat2 = [122, 122, 122]
color_moustache = [159, 159, 150]
color_eye = [117, 152, 81]
color_eye2 = [74, 201, 239]
white = [255, 255, 255]
color_ear = [245, 222, 179]


def main():
    room(xs, ys)
    # рисуем окна
    i = 460
    for j in range(3):
        window(i, 50, 230, 1.334 * 230)
        i -= 270
    # рисуем шары
    surfacebol = pygame.Surface((280, 180))
    surfacebol.fill(color_pol)
    surfacebol.set_colorkey(color_pol)
    boll(190, 80, 80, surfacebol)
    screen.blit(surfacebol, [100, 750])
    surfacebol.fill(color_pol)
    boll(70, 30, 30, surfacebol)
    screen.blit(surfacebol, [80, 750])
    surfacebol.fill(color_pol)
    boll(70, 30, 30, surfacebol)
    screen.blit(surfacebol, [450, 850])
    surfacebol.fill(color_pol)
    boll(70, 30, 30, surfacebol)
    screen.blit(surfacebol, [60, 450])
    surfacebol.fill(color_pol)
    boll(70, 30, 30, surfacebol)
    surfacebol2 = pygame.transform.flip(surfacebol, True, False)
    screen.blit(surfacebol2, [380, 600])
    surfacebol.fill(color_pol)
    boll(100, 60, 60, surfacebol)
    surfacebol2 = pygame.transform.flip(surfacebol, True, False)
    screen.blit(surfacebol2, [430, 750])
    surfacebol.fill(color_pol)
    boll(100, 60, 60, surfacebol)
    surfacebol2 = pygame.transform.flip(surfacebol, True, False)
    screen.blit(surfacebol2, [250, 650])
# рисуем котов
    cat(300, 450, 150, color_cat, color_eye, screen)
    cat(380, 800, 60, color_cat, color_eye, screen)
    cat(580, 880, 40, color_cat2, color_eye2, screen)
    surfacecat = pygame.Surface((400, 160))
    surfacecat.fill(color_pol)
    surfacecat.set_colorkey(color_pol)
    cat(10, 10, 150, color_cat2, color_eye2, surfacecat)
    surfacecat2 = pygame.transform.flip(surfacecat, True, False)
    screen.blit(surfacecat2, [10, 560])
    surfacecat.fill(color_pol)
    cat(10, 10, 40, color_cat2, color_eye2, surfacecat)
    surfacecat2 = pygame.transform.flip(surfacecat, True, False)
    screen.blit(surfacecat2, [-200, 860])
    surfacecat.fill(color_pol)
    cat(10, 10, 60, color_cat, color_eye, surfacecat)
    surfacecat2 = pygame.transform.flip(surfacecat, True, False)
    screen.blit(surfacecat2, [280, 680])
    screen.blit(surfacecat2, [-150, 500])


def room(xd, yd):
    """
    Рисует стену и пол
    :param xd: параметр х экрана
    :param yd: параметр у экрана
    :return: None
    """
    screen.fill(color_pol)
    rect(screen, color_wall, (0, 0, xd, yd/2.2))


def window(xo, yo, weiht, heg):
    """
    Рисует окно на стене, где х и у координаты верхнего левого угла
    высотой weiht и шириной heg
    :param xo: координата х
    :param yo: координата у
    :return: None
    """
    rect(screen, color_win1, (xo, yo, weiht, heg), )
    r = (weiht-(weiht/5))/2
    rect(screen, color_win2, (xo+int(weiht*0.066), yo+int(heg*0.025), int(r), int(heg*0.33)))
    rect(screen, color_win2, (xo+int(weiht*0.066*2)+int(r), yo+int(heg*0.025), int(r), int(heg*0.33)))
    rect(screen, color_win2, (xo+int(weiht*0.066), yo+int(heg*0.025*3)+int(heg*0.33), int(r), int(heg*0.33*1.7)))
    rect(screen, color_win2, (xo+int(weiht*0.066)*2+int(r), yo+int(heg*0.025*3) +
                              int(heg*0.33), int(r), int(heg*0.33*1.7)))


def boll(xb, yb, rad, screen2):
    """
    Рисует клубок с координатами середины х и у
    и радиусом rad. На поверхности screen2
    :return: None
    """
    circle(screen2, color_boll, (xb, yb), rad,)
    circle(screen2, black, (xb, yb), rad, 1)
    arc(screen2, black, [int(xb-rad), int(yb-rad/2), int(rad*1.5), int(rad*1.8)], 0, 3.14/2.2, 1)
    arc(screen2, black, [int(xb-rad/1.2), int(yb-rad/1.6), int(rad*1.5), int(rad * 1.8)], 0, 3.14/2.2, 1)
    arc(screen2, black, [int(xb-rad/1.5), int(yb-rad/1.3), int(rad*1.5), int(rad*1.8)], 0, 3.14 / 2.2, 1)
    arc(screen2, black, [int(xb-rad/3), int(yb-rad/3), int(rad), int(rad*1.6)], 3.14/1.7, 3.14, 1)
    arc(screen2, black, [int(xb - rad / 5), int(yb - rad / 5), int(rad), int(rad * 1.6)], 3.14 / 1.7, 3.14, 1)
    arc(screen2, black, [int(xb - rad / 20), int(yb - rad / 20), int(rad), int(rad * 1.6)], 3.14 / 1.7, 3.14, 1)
    aalines(screen2, color_boll, False, [(xb-0.81*rad, yb+0.57*rad),
                                         (xb-rad*1.2, yb+rad), (xb-rad*2, yb+rad/1.5), (xb-rad*2.5, yb+rad)], blend=1)


def cat(xc, yc, wegh, colorcat, coloreye, screen1):
    """
    Рисует кота с координатами верхнего левого угла хс, ус
    размера  wegh(условный размер!(800, 320). цвет шерсти кота colorcat,
    цвет глаз кота coloreye
    :return: None
    """
    # хвост
    surf1 = pygame.Surface((1.167*wegh, 0.434*wegh))
    surf1.fill(color_pol)
    surf1.set_colorkey(color_pol)
    ellipse(surf1, colorcat, [0, 0, 1.167*wegh, 0.334*wegh])
    ellipse(surf1, black, [0, 0, 1.167*wegh, 0.334*wegh], 1)
    surf2 = pygame.transform.rotate(surf1, 160)
    screen1.blit(surf2, (xc+wegh*1.4, yc-wegh*0.0334))
    # тело кот
    ellipse(screen1, colorcat, [xc+wegh*0.37, yc, wegh*1.467, wegh*0.767])
    ellipse(screen1, black, [xc+wegh*0.37, yc, wegh*1.467, wegh*0.767], 1)
    # лапка за головой
    ellipse(screen1, colorcat,  [xc+wegh*0.1367, yc+wegh*0.334, wegh*0.1834, wegh*0.2667])
    ellipse(screen1, black, [xc+wegh*0.1367, yc+wegh*0.334, wegh*0.1834, wegh*0.2667], 1)
    # Голова
    ellipse(screen1, colorcat, (xc, yc, wegh*0.6, 0.533*wegh))
    ellipse(screen1, black, (xc, yc, wegh * 0.6, 0.533*wegh), 1)
    # Ухо левое
    polygon(screen1, colorcat, [(xc - 0.0067*wegh, yc - 0.033*wegh), (xc + 0.166*wegh, yc + 0.05*wegh),
                                (xc + 0.05*wegh, yc + 0.166*wegh)])
    polygon(screen1, black, [(xc - 0.0134*wegh, yc - 0.034*wegh), (xc + 0.167*wegh, yc + 0.05*wegh),
                             (xc + 0.05*wegh, yc + 0.167*wegh)], 1)
    polygon(screen1, color_ear, [(xc+0.0067*wegh, yc - 0.0067*wegh), (xc + 0.14*wegh, yc + 0.0567*wegh),
                                 (xc + 0.0567*wegh, yc + 0.14*wegh)])
    # Ухо правое
    polygon(screen1, colorcat, [(xc + wegh * 0.59, yc - 0.0334*wegh),
                                (xc + wegh * 0.44, yc + 0.05*wegh), (xc + wegh * 0.55, yc + 0.17*wegh)])
    polygon(screen1, black, [(xc + wegh * 0.594, yc - 0.0334*wegh),
                             (xc + wegh * 0.44, yc + 0.05*wegh), (xc + wegh * 0.55, yc + 0.17*wegh)], 1)
    polygon(screen1, color_ear, [(xc + wegh * 0.575, yc - 0.01*wegh), (xc + wegh * 0.46, yc + 0.0567*wegh),
                                 (xc + wegh * 0.54, yc + 0.137*wegh)])
    # глаза
    # Левый
    ellipse(screen1, coloreye, [xc+wegh*0.104, yc+wegh*0.2, 0.15*wegh, 0.167*wegh])
    ellipse(screen1, black, [xc+wegh*0.104, yc+wegh*0.2, 0.15*wegh, 0.167*wegh], 1)
    surface = pygame.Surface((0.0267*wegh, 0.0834*wegh))
    surface.fill(coloreye)
    surface.set_colorkey(coloreye)
    ellipse(surface, white, [0, 0, 0.0267*wegh, 0.0834*wegh])
    surface2 = pygame.transform.rotate(surface, 35)
    screen1.blit(surface2, (xc+0.134*wegh, yc+wegh*0.2167))
    ellipse(screen1, black, [xc+0.19*wegh, yc+0.21*wegh, 0.0234*wegh, 0.15*wegh])
    # правый
    ellipse(screen1, coloreye, [xc+0.37*wegh, yc+wegh*0.2, 0.15*wegh, 0.1767*wegh])
    ellipse(screen1, black, [xc+0.37*wegh, yc+wegh*0.2, 0.15*wegh, 0.1767*wegh], 1)
    surface3 = pygame.Surface((0.0267*wegh, 0.0834*wegh))
    surface3.fill(coloreye)
    surface3.set_colorkey(coloreye)
    ellipse(surface3, white, [0, 0, 0.0267*wegh, 0.0834*wegh])
    surface4 = pygame.transform.rotate(surface, 35)
    screen1.blit(surface4, (xc+0.4*wegh, yc+0.2234*wegh))
    ellipse(screen1, black, [xc+0.4567*wegh, yc+0.2167*wegh, 0.0234*wegh, 0.15*wegh])
    # нос и рот
    polygon(screen1, color_ear, [(xc+0.27*wegh, yc+0.367*wegh), (xc+0.3367*wegh, yc+0.367*wegh),
                                 (xc+0.3034*wegh, yc+0.4*wegh)])
    polygon(screen1, black, [(xc+0.27*wegh, yc+0.367*wegh), (xc+0.3367*wegh, yc+0.367*wegh),
                             (xc+0.3034*wegh, yc+0.4*wegh)], 1)
    line(screen1, black, (xc+0.3034*wegh, yc+0.4*wegh), (xc+0.3034*wegh, yc+0.434*wegh), 1)
    arc(screen1, black, [xc+0.24*wegh, yc+0.4*wegh, 0.067*wegh, 0.067*wegh], 3.14*2.5/2, 2*3.14, 1)
    arc(screen1, black, [xc+0.3034*wegh, yc+0.4*wegh, 0.067*wegh, 0.067*wegh], 3.14, 3.55 * 3.14/2, 1)
    # усы
    arc(screen1, color_moustache, [xc+0.2834*wegh, yc+0.3834*wegh, 0.834*wegh, 0.2*wegh], 0.4*3.14, 0.75*3.14, 1)
    arc(screen1, color_moustache, [xc+0.2834*wegh, yc+0.4167*wegh, 0.667*wegh, 0.2*wegh], 0.30 * 3.14, 0.70 * 3.14, 1)
    arc(screen1, color_moustache, [xc+0.2234*wegh, yc+0.45*wegh, 0.667*wegh, 0.2*wegh], 0.25 * 3.14, 0.65 * 3.14, 1)

    arc(screen1, color_moustache, [xc-0.55*wegh, yc+0.367*wegh, 0.834*wegh, 0.2*wegh], 0.20 * 3.14, 0.55 * 3.14, 1)
    arc(screen1, color_moustache, [xc-0.467*wegh, yc+0.407*wegh, 0.834*wegh, 0.2*wegh], 0.3 * 3.14, 0.59 * 3.14, 1)
    arc(screen1, color_moustache, [xc-0.3434*wegh, yc+0.4467*wegh, 0.834*wegh, 0.2*wegh], 0.4 * 3.14, 0.7 * 3.14, 1)
    # лапка передняя
    ellipse(screen1, colorcat, [xc+0.3*wegh, yc+0.5167*wegh, 0.3667*wegh, 0.2*wegh])
    ellipse(screen1, black, [xc+0.3*wegh, yc+0.5167*wegh, 0.3667*wegh, 0.2*wegh], 1)
    # лапка задняя
    ellipse(screen1, colorcat,  [xc+1.367*wegh, yc+0.334*wegh, 0.5*wegh, 0.467*wegh])
    ellipse(screen1, black, [xc+1.367*wegh, yc+0.334*wegh, 0.5*wegh, 0.467*wegh], 1)
    ellipse(screen1, colorcat, [xc+1.767*wegh, yc+0.6*wegh, 0.167*wegh, 0.3667*wegh])
    ellipse(screen1, black, [xc+1.767*wegh, yc+0.6*wegh, 0.167*wegh, 0.3667*wegh], 1)


main()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
