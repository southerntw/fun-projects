import pygame
import sys
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 500
WIDTH = 500
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BING CHILING")

player_dir = "assets/Colour2/Outline/120x80_gifs/__Run.gif"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.surf = pygame.Surface((30, 30))
        player_img = pygame.image.load(player_dir)
        self.surf = player_img
        #self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 420))

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0.5)
        player_img = pygame.image.load(player_dir)
        player_img_rot = pygame.transform.flip(player_img, True, False)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.surf = player_img_rot
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.surf = player_img
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def jump(self):
        self.vel.y = -15

    def update(self):
        hits = pygame.sprite.spritecollide(P1 , platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()

    displaysurface.fill((0,0,0))
    P1.move()
    P1.update()

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
