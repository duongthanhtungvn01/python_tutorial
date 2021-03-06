import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

radius = 40
x = screenX/2
y = radius
vy = 1

clock = pygame.time.Clock()

while True:
    clock.tick(100)

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(x), int(y)), radius)
    pygame.display.flip()

    y += vy
    
    if (y < radius) or (y + radius > screenY):
        vy = -vy

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
