from random import randint
from time import sleep
from asciimatics.screen import Screen

locX = 5
locY = 5
dx = 1
dy = 1

def demo(screen):
    while True:
        update_pos()
        update_screen(screen)
        update_input(screen)
        screen.refresh()

def update_pos():
    global locX
    locX = locX + dx
    global locY 
    locY = locY + dy

def update_input(screen):
    ev = screen.get_key()
    if ev in (ord('Q'), ord('q')):
        return
    if ev in (ord('a'), ord('A')):
        dx = -1
    if ev in (ord('d'), ord('D')):
        dx = 1
    if ev in (ord('w'), ord('W')):
        dy = -1
    if ev in (ord('S'), ord('s')):
        dy = 1


def update_screen(screen):
    screen.move(0, 0)
    screen.draw(10, 10)
    screen.print_at('○',
                        locX, locY,
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
Screen.wrapper(demo)