import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill([125, 103, 60])


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
    ellipse(screen, (193, 113, 39), (350, 450, 240, 80))
    ellipse(screen, (0, 0, 0), (350, 450, 240, 80), 1)
    # core
    ellipse(screen, (193, 113, 39), (75, 375, 350, 200))
    ellipse(screen, (0, 0, 0), (75, 375, 350, 200), 1)
    # back leg
    circle(screen, (193, 113, 39), (370, 535), 60)
    circle(screen, (0, 0, 0), (370, 535), 60, 1)
    ellipse(screen, (193, 113, 39), (400, 550, 40, 85))
    ellipse(screen, (0, 0, 0), (400, 550, 40, 85), 1)
    # front legs
    ellipse(screen, (193, 113, 39), (100, 525, 95, 60))
    ellipse(screen, (0, 0, 0), (100, 525, 95, 60), 1)
    ellipse(screen, (193, 113, 39), (55, 450, 50, 105))
    ellipse(screen, (0, 0, 0), (55, 450, 50, 105), 1)
    # head
    circle(screen, (193, 113, 39), (105, 460), 80)
    circle(screen, (0, 0, 0), (105, 460), 80, 1)
    # eyes
    ellipse(screen, (123, 123, 39), (57, 445, 40, 45))
    ellipse(screen, (0, 0, 0), (57, 445, 40, 45), 1)
    ellipse(screen, (123, 123, 39), (118, 445, 40, 45))
    ellipse(screen, (0, 0, 0), (118, 445, 40, 45), 1)
    ellipse(screen, (0, 0, 0), (82, 447, 5, 40))
    ellipse(screen, (0, 0, 0), (142, 447, 5, 40))
    # ears
    polygon(screen, (193, 113, 39), ([25, 390], [62, 410], [35, 440]))
    polygon(screen, (0, 0, 0), ([25, 390], [62, 410], [35, 440]), 1)
    # mustache
    '''pygame.draw.arc(screen, (0, 0, 0), (10, 50, 280, 100), 0, 3)'''


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
