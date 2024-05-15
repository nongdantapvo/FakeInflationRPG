import pygame, sys, random
#khởi tạo pygame
pygame.init()
# Thiết lập kích thước của sổ trò chơi
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Inflation RPG")
sub_screen = pygame.Surface((600, 400))
sub_screen_rect = sub_screen.get_rect(center = screen.get_rect().center)
# Tải hình ảnh
background = pygame.image.load('picture/background.png').convert()
background = pygame.transform.scale(background, (800, 600))
# Player_images
player_images = {
    'right': pygame.image.load("picture/character_right.png").convert_alpha(),
    'left': pygame.image.load("picture/character_left.png").convert_alpha()
}
for director in player_images:
    player_images[director] = pygame.transform.scale(player_images[director], (50, 50))
# Enemy_images
enemy_images = {
    'right': pygame.image.load("picture/monster_right.png").convert_alpha(),
    'left': pygame.image.load("picture/monster_left.png").convert_alpha()
}
for director in enemy_images:
    enemy_images[director] = pygame.transform.scale(enemy_images[director], (50, 50))

battle_image = pygame.image.load("picture/background-battle.jfif")
battle_image = pygame.transform.scale(battle_image, (600, 400))
# Kiểm tra va chạm nhân vật và kẻ thù
def check_Collision(player, enemy):
    return player.rect.colliderect(enemy.rect)

# Lớp Player
class Player:
    def __init__(self, x, y):
        self.images = player_images
        self.image = self.images['right']
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
    
    def move(self, dx, dy):
        if dx > 0:
            self.image = self.images['right']
        elif dx < 0:
            self.image = self.images['left']
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
    def draw_battle(self, x, y):
        self.image = self.images['right']
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        
# Lớp Enemy
class Enemy:
    def __init__(self, x, y):
        self.images = enemy_images
        self.image = self.images['right']
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 1
        
    def move(self, dx, dy):
        if dx > 0:
            self.image = self.images['right']
        elif dx < 0:
            self.image = self.images['left']
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
    def draw_battle(self, x, y):
        self.image = self.images['left']
        self.rect.x = x
        self.rect.y = y
        
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Khởi tạo nhân vật và kẻ thù
player = Player(100, 100)
enemy = Enemy(300, 300)

# Tham số cho kẻ thù di chuyển ngẫu nhiên
y = random.choice([-1, 1])
x = random.choice([-1, 1])

# Trạng thái của trò chơi
game_state = 'play'

# Vòng lặp chính của trò chơi
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()      
    if game_state == "play":
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
            game_state = "battle"
    # Vẽ hình nền, nhân vật và kẻ thù
    screen.blit(background, (0,0))        
    if game_state == "play":
        player.draw(screen)
        enemy.draw(screen)
    elif game_state == "battle":
        sub_screen.fill((0,0,0))
        player.draw_battle(125, 175)
        enemy.draw_battle(450, 175)
        sub_screen.blit(battle_image, (0,0))
        player.draw(sub_screen)
        enemy.draw(sub_screen)
        screen.blit(sub_screen, sub_screen_rect)
    pygame.display.flip()
    
    # Giới hạn FPS
    clock.tick(120)
