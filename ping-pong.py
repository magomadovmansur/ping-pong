from pygame import *
colour = (255, 145, 0)
window = display.set_mode((700, 500))
display.set_caption("ping-pong")
game = True
finish = False
font.init()
font1 = font.SysFont("Arial", 35)
win = font1.render('PLAYER1 LOSE!', True, (215, 215, 0))
lose = font1.render('PLAYER2 LOSE!', True, (255, 0, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_widht, wall_height, speed):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.widht = wall_widht
        self.height = wall_height
        self.image = Surface((self.widht, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.speed = speed
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
        if keys[K_s] and self.rect.y < 320:
            self.rect.y = self.rect.y + self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
        if keys[K_DOWN] and self.rect.y < 320:
            self.rect.y = self.rect.y + self.speed
player1 = Wall(28, 238, 150, 0, 300, 40, 180, 5)
player2 = Wall(28, 238, 150, 660, 300, 40, 180, 5)
x = 350
y = 250
speed_x = 6
speed_y = 6
time = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.fill(colour)
        player1.draw_wall()
        player2.draw_wall()
        player1.update_l()
        player2.update_r()
        draw.circle(window, (150, 150, 0), (x, y), 50)
        x += speed_x
        y += speed_y
        if y >= 450 or y <= 50:
            speed_y *= -1
        if player1.rect.y <= y <= player1.rect.y + 230 and 40 >= x - 50 >= 0 or player2.rect.y <= y + 50 <= player2.rect.y + 230 and 660 <= x + 50 <= 700:
            speed_x *= -1
        if x < -50:
            finish = True
            window.blit(win, (200, 200))
        if x > 700:
            finish = True
            window.blit(lose, (200, 200))
    display.update()
    time.tick(FPS)
