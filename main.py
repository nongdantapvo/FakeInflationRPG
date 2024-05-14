import pygame, sys, random
#khởi tạo pygame
pygame.init()
# Thiết lập kích thước của sổ trò chơi
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Inflation RPG")
sub_screen = pygame.Surface((550, 400))
sub_screen_rect = sub_screen.get_rect(center = screen.get_rect().center)
# Tải hình ảnh
background = pygame.image.load('picture/background.png').convert()
background = pygame.transform.scale(background, (800, 600))
player_image = pygame.image.load("picture/character.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.image.load("picture/monster.png").convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
battle_image = pygame.image.load("picture/background-battle.jfif")
battle_image = pygame.transform.scale(battle_image, (550, 400))
# Kiểm tra va chạm nhân vật và kẻ thù
def check_Collision(player, enemy):
    return player.rect.colliderect(enemy.rect)

# Lớp Player
class Player:
    def __init__(self, x, y):
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
    
    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        
# Lớp Enemy
class Enemy:
    def __init__(self, x, y):
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 1
        
    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Khởi tạo nhân vật và kẻ thù
player = Player(100, 100)
enemy = Enemy(300, 300)

# Tham số cho kẻ thù di chuyển ngẫu nhiên
y = random.choice([-1, 1])
x = random.choice([-1, 1])

# Vòng lặp chính của trò chơi
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()      
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.left > 0:
        player.move(-1, 0)
    if keys[pygame.K_RIGHT] and player.rect.right < 800:
        player.move(1, 0)
    if keys[pygame.K_UP] and player.rect.top > 0:
        player.move(0, -1)
    if keys[pygame.K_DOWN] and player.rect.bottom < 600:
        player.move(0, 1)

    # Kẻ thù di chuyển
    if enemy.rect.left < 0 or enemy.rect.right > 800:
        enemy.rect.x += -x * 10
        x = random.choice([-1, 1])
        y = random.choice([-1, 1])
    if enemy.rect.top < 0 or enemy.rect.bottom > 600:
        enemy.rect.y += -y * 10
        y = random.choice([-1, 1])
        x = random.choice([-1, 1])
    enemy.move(x, y)
    if check_Collision(player, enemy):
        print("chạm")
    # Vẽ hình nền, nhân vật và kẻ thù
    screen.blit(background, (0,0))
    sub_screen.blit(battle_image, (0,0))
    screen.blit(sub_screen, sub_screen_rect)
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.flip()
    
    # Giới hạn FPS
    clock.tick(120)

# pygame.init()
# screen = pygame.display.set_mode((1000,759))
# pygame.display.set_caption("Fake Inflation RPG")

# #test draw health bar
# RED = (255,0,0)
# GREEN = (0,255,0)
# def draw_health_bar(surface, x, y, width, height, health):
#     pygame.draw.rect(surface, RED, (x, y, width, height))
#     health_width = int(width*health)
#     pygame.draw.rect(surface, GREEN, (x, y, health_width, height))
# current_health = 0.7  # Giả sử 70% máu còn lại
# max_health = 1.0  # Giả sử máu tối đa là 100%

# sub_screen = pygame.Surface((735, 466))
# sub_rect = sub_screen.get_rect(center=screen.get_rect().center)
# sub_screen.fill((255,255,255))

# clock = pygame.time.Clock()

# char_speed = 2

# bg_surface = pygame.image.load('picture/background.png').convert()
# battle_surface = pygame.image.load('picture/background-battle.jfif').convert()
# # battle_surface = pygame.transform.scale(battle_surface, (500,500))

# char_surface = pygame.image.load("picture/character.png").convert_alpha()
# char_surface = pygame.transform.scale(char_surface, (50, 50))
# char_rect = char_surface.get_rect(center = (500, 380))

# mon_surface = pygame.image.load("picture/monster.png").convert_alpha()
# mon_surface = pygame.transform.scale(mon_surface, (50, 50))
# mon_rect = mon_surface.get_rect(center = (200, 200))
# mon_flip = pygame.transform.flip(mon_surface, True, False)
# mon_flip_rect = mon_flip.get_rect(center=mon_rect.center)
# x_mov_mon = random.choice([-1, 1])
# y_mov_mon = random.choice([-1, 1])
# #time skip collution screen for monster
# pause_time = 0
# pause_duration = 500
# #check key press
# left_press = False
# up_press = False
# right_press = False
# down_press = False

# is_battle = False
# active = True
# while active:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.blit(bg_surface,(0,0))
    
#     # sub_screen.blit(battle_surface, (0,0))
#     # screen.blit(sub_screen, sub_rect)
    
#     keys = pygame.key.get_pressed()
#     if not is_battle:
#         #character
#         if keys[pygame.K_LEFT] and char_rect.left > 0:
#             char_rect.centerx -= char_speed
#         if keys[pygame.K_RIGHT] and char_rect.right < 1000:
#             char_rect.centerx  += char_speed
#         if keys[pygame.K_UP] and char_rect.top > 0:
#             char_rect.centery -= char_speed
#         if keys[pygame.K_DOWN] and char_rect.bottom < 759:
#             char_rect.centery += char_speed
#         screen.blit(char_surface,char_rect)
#         #monster
#         if pause_time > 0:
#             pause_time -= clock.get_time()
#         else:
#             mon_rect.centerx += x_mov_mon
#             mon_rect.centery += y_mov_mon
#             if mon_rect.left < 0 or mon_rect.right > 1000 or mon_rect.top < 0 or mon_rect.bottom > 759:
#                 x_mov_mon = -x_mov_mon
#                 y_mov_mon = -y_mov_mon
#                 mon_rect.move_ip(x_mov_mon * 10, y_mov_mon * 10) # lùi một đoạn 10 pixel
#                 pause_time = pause_duration
#                 x_mov_mon = random.choice([-1, 1])
#                 y_mov_mon = random.randint(-1, 1)
#         screen.blit(mon_surface, mon_rect)
#         if char_rect.colliderect(mon_rect):
#             is_battle = True
#     else:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 pass
#         char_rect.x = 200
#         char_rect.y = 200
#         mon_flip_rect.x = 535-mon_flip_rect.width
#         mon_flip_rect.y = 200
#         current_health -= 0.001
#         current_health = max(0, current_health)
#         draw_health_bar(sub_screen, 0,0,200,10, current_health)
#         pygame.time.delay(10)
#         sub_screen.blit(battle_surface, (0,0))
#         sub_screen.blit(char_surface, char_rect)
#         sub_screen.blit(mon_flip, mon_flip_rect)
#         screen.blit(sub_screen, sub_rect)
#         # #hide monster
#         # x_mov_mon += 1000
#         # y_mov_mon += 1000
#     pygame.display.update()
#     clock.tick(120)