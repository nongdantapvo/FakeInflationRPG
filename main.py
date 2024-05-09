import pygame, sys, random

pygame.init()

WHITE = (255, 255, 255)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Inflation_RPG")

bg = pygame.image.load("picture/background.png")
char = pygame.image.load("picture/character.png")
char = pygame.transform.scale(char, (200, 150))
char_rect = char.get_rect()
mon = pygame.image.load("picture/monster.png")
mon = pygame.transform.scale(mon, (100, 100))
mon_rect = mon.get_rect()

x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT //2
x_mon, y_mon = SCREEN_WIDTH // 2, SCREEN_HEIGHT //2
dx, dy = random.randint(-1, 1), random.randint(-1, 1)

speed = 2
#kiểm tra tình trạng phím
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False

    x_mon += dx
    y_mon += dy

    if x_mon <= 0 or x_mon >= SCREEN_WIDTH - mon_rect.width:
        dx = -dx
    if y_mon <= 0 or y_mon >= SCREEN_HEIGHT - mon_rect.height:
        dy = -dy

    if left_pressed:
        if x <= 0:
            x = -speed            
        x -= speed
    if right_pressed:
        if x >= SCREEN_WIDTH:
            x = SCREEN_WIDTH - speed
        x += speed
    if up_pressed:
        if y <= 0:
            y = 0
        y -= speed
    if down_pressed:
        if y >= SCREEN_HEIGHT:
            y = SCREEN_HEIGHT
        y += speed
            

    screen.fill(WHITE)
    screen.blit(bg, (0, 0))
    screen.blit(char, (x - char_rect.width // 2, y - char_rect.height // 2))
    screen.blit(mon, (x_mon, y_mon))
    pygame.display.update()
    clock.tick(120)