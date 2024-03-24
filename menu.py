import pygame
import sys
import os
from widgets import *
from enrty_db import change_user_model
from options import *
import game

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rush and Shoot")
main_background = load_image('Background.png')

pointer = load_image('crosshair193.png', color_key=-1)
pygame.transform.scale(pointer, (5, 5))
pygame.mouse.set_visible(False)


def start_main_menu():
    start_btn = ImageButton(load_image('play.png'), (WIDTH / 2 - (252 / 2), 200), (250, 50), '',
                            hover_image=load_image('play.png'))
    options_btn = ImageButton(load_image('options.png'), (WIDTH / 2 - (252 / 2), 300), (250, 50), '',
                              hover_image=load_image('options.png'))
    lead_btn = ImageButton(load_image('lead.png'), (WIDTH / 2 - (252 / 2), 400), (250, 50), '',
                           hover_image=load_image('exit.png'))
    exit_btn = ImageButton(load_image('exit.png'), (WIDTH / 2 - (252 / 2), 500), (250, 50), '',
                           hover_image=load_image('exit.png'))

    btn_lst = [start_btn, options_btn, exit_btn, lead_btn]

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        font = pygame.font.Font(FONT, 46)
        text_surface = font.render("SHOOT AND RUSH", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.USEREVENT and event.button == exit_btn):
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.button == options_btn:
                    options_menu()
                if event.button == start_btn:
                    level_menu()
                    running = False
                if event.button == lead_btn:
                    leader_menu()

            for btn in btn_lst:
                btn.handle_event(event)
        for btn in btn_lst:
            btn.chek_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        x, y = pygame.mouse.get_pos()
        screen.blit(pointer, (x - 5, y - 5))
        pygame.display.flip()


def options_menu():
    getback_btn = ImageButton(load_image('back.png'), (WIDTH/2-(252/2), 600), (250, 50), '',  hover_image=load_image('back.png'))
    player1_btn = ImageButton(load_image('player1_start.png'), (100, 310), (150, 150), '',  hover_image=load_image('player1_start.png'))
    player2_btn = ImageButton(load_image('player2_start.png'), (350, 310), (150, 150), '',  hover_image=load_image('player2_start.png'))
    player3_btn = ImageButton(load_image('player3_start.png'), (600, 310), (150, 150), '',  hover_image=load_image('player3_start.png'))
    player4_btn = ImageButton(load_image('player4_start.png'), (900, 310), (150, 150), '',  hover_image=load_image('player4_start.png'))
    btn_lst = [getback_btn, player1_btn, player2_btn, player3_btn, player4_btn]
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        font = pygame.font.Font(FONT, 46)
        text_surface = font.render("ОПЦИИ", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)
        text_surface_choose = font.render("ВЫБЕРИТЕ ИГРОКА", True, (255, 255, 255))
        text_rect_choose = text_surface_choose.get_rect(center=(WIDTH / 2, 160))
        screen.blit(text_surface_choose, text_rect_choose)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT:
                if event.button == getback_btn:
                    running = False
                if event.button == player1_btn:
                    change_user_model(1, PLAYER_ID)
                if event.button == player2_btn:
                    change_user_model(2, PLAYER_ID)
                if event.button == player3_btn:
                    change_user_model(3, PLAYER_ID)
                if event.button == player4_btn:
                    change_user_model(4, PLAYER_ID)
            for btn in btn_lst:
                btn.handle_event(event)
        for btn in btn_lst:
            btn.chek_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        x, y = pygame.mouse.get_pos()
        screen.blit(pointer, (x - 5, y - 5))
        pygame.display.flip()


def level_menu():
    getback_btn = ImageButton(load_image('back.png'), (WIDTH/2-(252/2), 600), (250, 50), '',  hover_image=load_image('back.png'))
    lvl1_btn = ImageButton(load_image('lvl1.jpg'), (250, 270), (250, 250), '',  hover_image=load_image('player2_start.png'))
    lvl2_btn = ImageButton(load_image('lvl2.jpg'), (600, 270), (250, 250), '',  hover_image=load_image('player3_start.png'))
    btn_lst = [getback_btn, lvl1_btn, lvl2_btn]
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        font = pygame.font.Font(FONT, 46)
        text_surface_choose = font.render("ВЫБЕРИТЕ УРОВЕНЬ", True, (255, 255, 255))
        text_rect_choose = text_surface_choose.get_rect(center=(WIDTH / 2, 160))
        screen.blit(text_surface_choose, text_rect_choose)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT:
                if event.button == getback_btn:
                    running = False
                if event.button == lvl1_btn:
                    init_game(0)
                    running = False
                if event.button == lvl2_btn:
                    init_game(1)
            for btn in btn_lst:
                btn.handle_event(event)
        for btn in btn_lst:
            btn.chek_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        x, y = pygame.mouse.get_pos()
        screen.blit(pointer, (x - 5, y - 5))
        pygame.display.flip()


def leader_menu():
    getback_btn = ImageButton(load_image('back.png'), (WIDTH/2-(252/2), 600), (250, 50), '',  hover_image=load_image('back.png'))
    leader_lst = get_all_score()
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        font1 = pygame.font.Font(None, 72)
        text_surface_choose = font1.render('Таблица результатов', True, (255, 255, 255))
        text_rect_choose = text_surface_choose.get_rect(center=(WIDTH / 2, 50))
        screen.blit(text_surface_choose, text_rect_choose)
        font = pygame.font.Font(None, 32)
        coord_y = 120
        for row in leader_lst:
            text_surface_choose = font.render(row, True, (255, 255, 255))
            text_rect_choose = text_surface_choose.get_rect(center=(WIDTH / 2, coord_y))
            screen.blit(text_surface_choose, text_rect_choose)
            coord_y += 50

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT:
                if event.button == getback_btn:
                    running = False
            getback_btn.handle_event(event)
        getback_btn.chek_hover(pygame.mouse.get_pos())
        getback_btn.draw(screen)
        x, y = pygame.mouse.get_pos()
        screen.blit(pointer, (x - 5, y - 5))
        pygame.display.flip()


def init_game(lvl):
    rush_and_shoot = game.Game(lvl)
    rush_and_shoot.new()
    rush_and_shoot.run()
    rush_and_shoot.game_over()


while True:
    start_main_menu()