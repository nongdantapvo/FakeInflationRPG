import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1000,759))
pygame.display.set_caption("Fake Inflation RPG")

sub_screen = pygame.Surface((735, 466))
sub_rect = sub_screen.get_rect(center=screen.get_rect().center)
sub_screen.fill((255,255,255))

clock = pygame.time.Clock()

char_speed = 2

bg_surface = pygame.image.load('picture/background.png').convert()
battle_surface = pygame.image.load('picture/background-battle.jfif').convert()
# battle_surface = pygame.transform.scale(battle_surface, (500,500))

char_surface = pygame.image.load("picture/character.png").convert_alpha()
char_surface = pygame.transform.scale(char_surface, (50, 50))
char_rect = char_surface.get_rect(center = (500, 380))

mon_surface = pygame.image.load("picture/monster.png").convert_alpha()
mon_surface = pygame.transform.scale(mon_surface, (50, 50))
mon_rect = mon_surface.get_rect(center = (200, 200))
mon_flip = pygame.transform.flip(mon_surface, True, False)
mon_flip_rect = mon_flip.get_rect(center=mon_rect.center)
x_mov_mon = random.choice([-1, 1])
y_mov_mon = random.choice([-1, 1])
#time skip collution screen for monster
pause_time = 0
pause_duration = 500
#check key press
left_press = False
up_press = False
right_press = False
down_press = False

is_battle = False
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_press = True
            elif event.key == pygame.K_RIGHT:
                right_press = True
            elif event.key == pygame.K_UP:
                up_press = True
            elif event.key == pygame.K_DOWN:
                down_press = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_press = False
            elif event.key == pygame.K_RIGHT:
                right_press = False
            elif event.key == pygame.K_UP:
                up_press = False
            elif event.key == pygame.K_DOWN:
                down_press = False

    screen.blit(bg_surface,(0,0))
    
    # sub_screen.blit(battle_surface, (0,0))
    # screen.blit(sub_screen, sub_rect)
    
    
    if not is_battle:
        #character
        if left_press and char_rect.left > 0:
            char_rect.centerx -= char_speed
        if right_press and char_rect.right < 1000:
            char_rect.centerx  += char_speed
        if up_press and char_rect.top > 0:
            char_rect.centery -= char_speed
        if down_press and char_rect.bottom < 759:
            char_rect.centery += char_speed
        screen.blit(char_surface,char_rect)
        #monster
        if pause_time > 0:
            pause_time -= clock.get_time()
        else:
            mon_rect.centerx += x_mov_mon
            mon_rect.centery += y_mov_mon
            if mon_rect.left < 0 or mon_rect.right > 1000 or mon_rect.top < 0 or mon_rect.bottom > 759:
                x_mov_mon = -x_mov_mon
                y_mov_mon = -y_mov_mon
                mon_rect.move_ip(x_mov_mon * 10, y_mov_mon * 10) # lùi một đoạn 10 pixel
                pause_time = pause_duration
                x_mov_mon = random.choice([-1, 1])
                y_mov_mon = random.randint(-1, 1)
        screen.blit(mon_surface, mon_rect)
        if char_rect.colliderect(mon_rect):
            is_battle = True
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pass
        char_rect.x = 200
        char_rect.y = 200
        mon_flip_rect.x = 535-mon_flip_rect.width
        mon_flip_rect.y = 200

        sub_screen.blit(battle_surface, (0,0))
        sub_screen.blit(char_surface, char_rect)
        sub_screen.blit(mon_flip, mon_flip_rect)
        screen.blit(sub_screen, sub_rect)
        # #hide monster
        # x_mov_mon += 1000
        # y_mov_mon += 1000
    pygame.display.update()
    clock.tick(120)