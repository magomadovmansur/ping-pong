from pygame import *
colour = (255, 145, 0)
window = display.set_mode((700, 500))
display.set_caption("ping-pong")
game = True
finish = False
font.init()
font1 = font.SysFont("Arial", 70)
win = font1.render('YOU WIN', True, (215, 215, 0))
lose = font1.render('YOU LOSE', True, (255, 0, 0))
font2 = font.SysFont(None, 36)
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
class Player(GameSprite):
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
player1 = Player("nchart-39304__340.png", 0, 300, 40, 180, 5)
player2 = Player("nchart-39304__340.png", 660, 300, 40, 180, 5)
time = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.fill(colour)
        player1.reset()sssss
        player2.reset()
        player1.update_l()
        player2.update_r()
    display.update()
    time.tick(FPS)