import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill([125, 103, 60])

# colors
BLACK = (0, 0, 0)
GREEN_CAT = (60, 180, 60)


def window():
    # main color
    rect(screen, (49, 72, 33), (0, 0, 600, 350))
    # window
    rect(screen, (220, 220, 220), (350, 30, 240, 300))
    rect(screen, (66, 145, 255), (370, 50, 90, 80))
    rect(screen, (66, 145, 255), (480, 50, 90, 80))
    rect(screen, (66, 145, 255), (480, 150, 90, 165))
    rect(screen, (66, 145, 255), (370, 150, 90, 165))


def cat():
    # tail
    ellipse(screen, (60, 180, 60), (350, 450, 240, 80))
    ellipse(screen, BLACK, (350, 450, 240, 80), 1)
    # core
    ellipse(screen, GREEN_CAT, (75, 375, 350, 200))
    ellipse(screen, BLACK, (75, 375, 350, 200), 1)
    # back leg
    circle(screen, GREEN_CAT, (370, 535), 60)
    circle(screen, BLACK, (370, 535), 60, 1)
    ellipse(screen, GREEN_CAT, (400, 550, 40, 85))
    ellipse(screen, BLACK, (400, 550, 40, 85), 1)
    # front legs
    ellipse(screen, GREEN_CAT, (100, 525, 95, 60))
    ellipse(screen, BLACK, (100, 525, 95, 60), 1)
    ellipse(screen, GREEN_CAT, (55, 450, 50, 105))
    ellipse(screen, BLACK, (55, 450, 50, 105), 1)
    # head
    circle(screen, GREEN_CAT, (105, 460), 80)
    circle(screen, BLACK, (105, 460), 80, 1)
    # eyes
    ellipse(screen, (150, 255, 150), (57, 445, 40, 45))
    ellipse(screen, BLACK, (57, 445, 40, 45), 1)
    ellipse(screen, (150, 150, 250), (118, 445, 40, 45))
    ellipse(screen, BLACK, (118, 445, 40, 45), 1)
    ellipse(screen, BLACK, (82, 447, 5, 40))
    ellipse(screen, BLACK, (142, 447, 5, 40))
    # left ear
    polygon(screen, GREEN_CAT, ([25, 390], [62, 410], [35, 440]))
    polygon(screen, BLACK, ([25, 390], [62, 410], [35, 440]), 1)
    polygon(screen, (200, 220, 200), ([30, 395], [54, 412], [39, 430]))
    polygon(screen, BLACK, ([30, 395], [54, 412], [39, 430]), 1)
    # right ear
    polygon(screen, GREEN_CAT, ([225-50, 390-10], [185-50, 410-10], [210-50, 440-10]))
    polygon(screen, BLACK, ([225-50, 390-10], [185-50, 410-10], [210-50, 440-10]), 1)
    polygon(screen, (200, 220, 200), ([220-50, 395-10], [192-50, 412-10], [208-50, 430-10]))
    polygon(screen, BLACK, ([220-50, 395-10], [192-50, 412-10], [208-50, 430-10]), 1)
    # mustache left side
    line(screen, BLACK, [85, 500], [10, 490])
    line(screen, BLACK, [85, 503], [10, 500])
    line(screen, BLACK, [85, 506], [10, 510])
    # mustache right side
    line(screen, BLACK, [125, 500], [200, 490])
    line(screen, BLACK, [125, 503], [200, 500])
    line(screen, BLACK, [125, 506], [200, 510])
    # nose
    polygon(screen, (230, 230, 230), ([155 - 55, 430 + 60],
                                      [165 - 55, 430 + 60], [160 - 55, 435 + 60]))
    polygon(screen, BLACK, ([155 - 55, 430 + 60],
                            [165 - 55, 430 + 60], [160 - 55, 435 + 60]), 1)
    # mouth
    line(screen, BLACK, [105, 495], [105, 510])
    line(screen, BLACK, [105, 510], [100, 515])
    line(screen, BLACK, [100, 515], [98, 512])
    line(screen, BLACK, [105, 510], [110, 515])
    line(screen, BLACK, [110, 515], [112, 512])


if __name__ == '__main__':
    window()
    cat()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
