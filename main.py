import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1000,759))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('picture/background.png').convert()
char_surface = pygame.image.load("picture/character.png").convert_alpha()
char_rect = char_surface.get_rect(center = (500, 380))
pygame.draw.rect(bg_surface, (255,0,0), char_rect, 2)
mon_surface = pygame.image.load("picture/monster.png").convert_alpha()

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_surface,(0,0))
    screen.blit(char_surface,(0,0))
    pygame.display.update()
    clock.tick(120)






# WHITE = (255, 255, 255)
# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 760
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# clock = pygame.time.Clock()
# pygame.display.set_caption("Inflation_RPG")

# bg = pygame.image.load("picture/background.png")
# char = pygame.image.load("picture/character.png")
# char = pygame.transform.scale(char, (70, 100))
# char_rect = char.get_rect()
# mon = pygame.image.load("picture/monster.png")
# mon = pygame.transform.scale(mon, (100, 100))
# mon_rect = mon.get_rect()

# x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT //2
# x_mon, y_mon = SCREEN_WIDTH // 2, SCREEN_HEIGHT //2
# dx, dy = random.randint(-1, 1), random.randint(-1, 1)

# speed = 2
# #kiểm tra tình trạng phím
# left_pressed = False
# right_pressed = False
# up_pressed = False
# down_pressed = False

# monster_mover_time = 0
# move_interval = 150



# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 left_pressed = True
#             elif event.key == pygame.K_RIGHT:
#                 right_pressed = True
#             elif event.key == pygame.K_UP:
#                 up_pressed = True
#             elif event.key == pygame.K_DOWN:
#                 down_pressed = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 left_pressed = False
#             elif event.key == pygame.K_RIGHT:
#                 right_pressed = False
#             elif event.key == pygame.K_UP:
#                 up_pressed = False
#             elif event.key == pygame.K_DOWN:
#                 down_pressed = False

#     # if char_rect.colliderect(mon_rect):
#     #     print("va chạm xãy ra!!")


#     monster_mover_time += clock.get_time()

#     if monster_mover_time >= move_interval:
#         x_mon += dx
#         y_mon += dy

#         if x_mon <= 0 or x_mon >= SCREEN_WIDTH - mon_rect.width:
#             dx = -dx
#         if y_mon <= 0 or y_mon >= SCREEN_HEIGHT - mon_rect.height:
#             dy = -dy
#         monster_mover_time = 0

#     if left_pressed and x > 35:            
#         x -= speed
#     if right_pressed and x < SCREEN_WIDTH - 35:
#         x += speed
#     if up_pressed and y > 50:
#         y -= speed
#     if down_pressed and y < SCREEN_HEIGHT - 50:
#         y += speed
            

#     screen.fill(WHITE)
#     screen.blit(bg, (0, 0))
#     screen.blit(char, (x - char.get_width() // 2, y - char.get_height() // 2))
#     screen.blit(mon, (x_mon, y_mon))
#     pygame.display.update()
#     clock.tick(120)