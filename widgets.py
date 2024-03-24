import pygame
import os
from options import *
from math import pi, atan2
from random import uniform
vec = pygame.math.Vector2


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


class ImageButton:
    def __init__(self, image, pos, size, text, hover_image=None):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.text = text
        self.image = pygame.transform.scale(image, (self.width, self.height))
        if hover_image:
            self.hover_image = hover_image
            self.hover_image = pygame.transform.scale(image, (self.width + 10, self.height + 10))
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.is_hovered = False

    def draw(self, screen):
        cur_image = self.hover_image if self.is_hovered else self.image
        screen.blit(cur_image, self.rect.topleft)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def chek_hover(self, mouse):
        self.is_hovered = self.rect.collidepoint(mouse)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.width -= 5
        self.rect.height -= 5
        self.vx, self.vy = 0, 0
        self.x = x * CELL
        self.y = y * CELL
        self.pos = vec(x, y) * CELL
        self.last_shot = 0
        self.health = PLAYER_HEALTH
        self.hit_rect = pg.Rect(0, 0, 30, 30)
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.rot = 90

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        # стрелять пока зажата мышь (True, False, False)
        if pygame.mouse.get_pressed()[0]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > 150:
                self.last_shot = now
                direction = vec(1, 0).rotate(-self.rot)
                posit = [self.x, self.y]
                pos = posit + vec(30, 10).rotate(-self.rot)
                Bullet(self.game, pos, direction)
                self.vel = vec(-0, 0).rotate(-self.rot)

    def update(self):
        self.get_keys()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.rot = (180 / pi) * -atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.game.player_img, self.rot)
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.pos += self.vel * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.rect.x = self.x
        self.rect.y = self.y
        self.hit_rect.centerx = self.rect.x
        self.collide_walls('x')
        self.hit_rect.centery = self.rect.y
        self.collide_walls('y')

    def collide_walls(self, direction):
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.enemy_img
        self.rect = self.image.get_rect()
        self.hit_rect = pygame.Rect(0, 0, 30, 30)
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * CELL
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = 90
        self.vx, self.vy = 0, 0
        self.x = x * CELL
        self.y = y * CELL

    def update(self):
        pos = [self.game.player.x + CELL, self.game.player.y + CELL]
        self.rot = (pos - self.pos).angle_to(vec(1, 0))
        # self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pygame.transform.rotate(self.game.enemy_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(250, 0).rotate(-self.rot)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        self.collide_walls('x')
        self.hit_rect.centery = self.pos.y
        self.collide_walls('y')
        self.rect.center = self.hit_rect.center
        if self.health <= 0:
            self.game.score += 15
            self.game.count_enemies -= 1
            self.kill()

    def collide_walls(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centerx > self.hit_rect.centerx:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if hits[0].rect.centerx < self.hit_rect.centerx:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centery > self.hit_rect.centery:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                if hits[0].rect.centery < self.hit_rect.centery:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, pos, direction):
        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-5, 5)
        self.vel = direction.rotate(spread) * BULLET_SPEED
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > 1000:
            self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * CELL
        self.rect.y = y * CELL


def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    fill = pct * 200
    outline_rect = pygame.Rect(x, y, 200, 20)
    fill_rect = pygame.Rect(x, y, fill, 20)
    if pct > 0.6:
        col = (0, 255, 0)
    elif pct > 0.3:
        col = (255, 255, 0)
    else:
        col = (255, 0, 0)
    pygame.draw.rect(surf, col, fill_rect)
    pygame.draw.rect(surf, (255, 255, 255), outline_rect, 2)


def draw_player_score(surf, x, y, score):
    font = pygame.font.Font(None, 46)
    color = (255, 0, 0)
    if 0 < score <= 25:
        color = (255, 255, 255)
    elif 25 < score <= 50:
        color = (255, 255, 0)
    elif 50 < score <= 75:
        color = (0, 255, 0)
    elif score >= 75:
        color = (128, 0, 128)
    text_surface_choose = font.render(str(score), True, color)
    text_rect_choose = text_surface_choose.get_rect(center=(x, y))
    surf.blit(text_surface_choose, text_rect_choose)

