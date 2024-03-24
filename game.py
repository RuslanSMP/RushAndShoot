import random
import pygame
import sys
import os
from options import *
from widgets import *
from random import choice, randint


class Game:
    def __init__(self, lvl):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_level(lvl)
        self.score = 0
        self.user_id = get_selected_user()
        self.count_enemies = 0
        self.difficult_wave = 5
        self.pointer = load_image('crosshair193.png', color_key=-1)
        pygame.transform.scale(self.pointer, (5, 5))
        pygame.mouse.set_visible(False)
        self.end = False

    def load_level(self, lvl):
        # загружаем карту уровня
        filename = 'data/' + MAP_LVL[lvl]
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, level_map))
        self.map_lvl = list(map(lambda x: list(x.ljust(max_width, '.')), level_map))
        # загружаем картинки юнитов из модуля options
        # картинку игрока обновляем из БД (вдруг поменялась)
        self.player_img = load_image(get_user_model(PLAYER_ID))
        self.wall_img = load_image(WALL_IMG)
        self.wall_img = pygame.transform.scale(self.wall_img, (CELL, CELL))
        self.enemy_img = load_image(choice(ENEMY_IMG))
        self.bullet_img = load_image(BULLET_IMG)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        for y, tiles in enumerate(self.map_lvl):
            for x, tile in enumerate(tiles):
                if tile == '#':
                    Wall(self, x, y)
                if tile == '@':
                    self.player = Player(self, x, y)
                if tile == 'X':
                    Enemy(self, x, y)
                    self.count_enemies += 1

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= 10
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
                new_score(self.user_id, self.score)
                self.end = True
        if hits:
            self.player.pos += vec(5, 0).rotate(-hits[0].rot)
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0, 0)

    def draw(self):
        fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))
        self.all_sprites.draw(self.screen)
        draw_player_health(self.screen, (WIDTH // 4) - 200, 5, self.player.health / PLAYER_HEALTH)
        draw_player_score(self.screen, WIDTH / 2, 18, self.score)
        x, y = pygame.mouse.get_pos()
        self.screen.blit(self.pointer, (x - 5, y - 5))
        pygame.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(60) / 1000
            self.events()
            self.update()
            self.draw()
            if self.count_enemies == 0:
                self.difficult_wave += 1
                self.generate_next_wave()

    def generate_next_wave(self):
        self.enemy_img = load_image(choice(ENEMY_IMG))
        # делать отступы от стен и делать проверку на стену если враг в ней заспавнится будет плохо
        for i in range(self.difficult_wave):
            collide_wall = False
            while not collide_wall:
                x = randint(5, len(self.map_lvl[0]) - 5)
                y = randint(5, len(self.map_lvl) - 5)
                if self.map_lvl[y][x] != '#':
                    collide_wall = True
            Enemy(self, x, y)
            self.count_enemies += 1

    def quit(self):
        pygame.quit()
        sys.exit()


    def game_over(self):
        end_screen = True
        game_over_bg = load_image('game_over.jpg')
        while end_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_screen = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE\
                            or event.key == pygame.K_RETURN:
                        end_screen = False
            self.screen.blit(game_over_bg, (0, 0))
            pygame.display.flip()
            pygame.display.update()
            game_over_bg = pygame.transform.smoothscale(game_over_bg, (WIDTH, HEIGHT))


# def init_start():
#     g = Game()
#     g.show_start_screen()
#     while not g.end:
#         # g.show_start_screen()
#         g.new()
#         g.run()
#         g.game_over()
#
# init_start()