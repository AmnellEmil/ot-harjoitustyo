#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:52:34 2021

@author: emil
"""
from board import Board
import pygame as pg
from sys import exit
from time import perf_counter
import webbrowser
from sheets import send_result_to_sheets

leaderboard_url="https://docs.google.com/spreadsheets/d/10xBRJxn7BcR-Dr718IB09TF8ZQYVEOnhs_iYh6t2Wzo/edit#gid=0"

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((1024, 720), pg.RESIZABLE)
screen.fill("Grey")
pixels = 48
font = pg.font.SysFont("Arial", pixels-15)
pg.display.set_caption("Minesweeper")

def draw_text(text, font, color, x, y,topleft):
    text_surface = font.render(text, True, color)
    if not topleft:
        text_rect = text_surface.get_rect(center=(x, y))
    else:
        text_rect = text_surface.get_rect(topleft=(x, y))
    return text_surface, text_rect

def draw_popup_box(screen,color_box,w,h,x,y,alpha):
    popup_surf=pg.Surface((w,h))
    popup_surf.fill(color_box)
    popup_surf.set_alpha(alpha)
    popup_rect=popup_surf.get_rect(center=(x,y))
    screen.blit(popup_surf,popup_rect)

def draw_text_on_screen(screen, text, font, color, x, y,topleft):
    surf, rect = draw_text(text, font, color, x, y,topleft)
    screen.blit(surf, rect)


class Button():
    def __init__(self, screen, text, font, width, height, x, y):
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.text_surf, self.text_rect = draw_text(text, font, "White", x, y,False)
        self.rect = pg.Rect(x, y, width, height)
        self.rect.center = (x, y)
        self.screen = screen
        self.hover = False

    def draw(self):
        if self.hover:
            pg.draw.rect(screen, "Red", self.rect)
            self.text_surf, self.text_rect = draw_text(
                self.text, self.font, "Black", self.x, self.y,False)
            self.screen.blit(self.text_surf, self.text_rect)
        else:
            pg.draw.rect(screen, "Black", self.rect)
            self.text_surf, self.text_rect = draw_text(
                self.text, self.font, "White", self.x, self.y,False)
            self.screen.blit(self.text_surf, self.text_rect)

    def check_collision(self):
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True

    def check_hover(self):
        if self.check_collision():
            self.hover = True
        else:
            self.hover = False


def main_menu(screen):
    disp_w, disp_h = 1024, 720
    example_surf = pg.image.load("images/example.png")
    example_surf = pg.transform.scale(example_surf, (disp_w, disp_h))
    example_surf.set_alpha(150)
    control_interface = False
    options_interface = False
    main_menu = True
    rows, columns, nbombs = 9, 9, 10
    play_button = Button(screen, "Play", font, 250, 100, disp_w/2, disp_h/2)
    controls_button = Button(screen, "Controls", font,
                             250, 100, disp_w/2, disp_h/2+110)
    leaderboard_button=Button(screen,"Leaderboards",font,250,100,disp_w/2,disp_h/2+220)
    escape_button = Button(screen, "Escape: go back",
                           font, 500, 100, disp_w/2, 100)
    r_button = Button(screen, "R: restart game", font, 500, 100, disp_w/2, 250)
    m1_button = Button(screen, "Mouse 1: reveal square",
                       font, 500, 100, disp_w/2, 400)
    m2_button = Button(screen, "Mouse 2: flag square",
                       font, 500, 100, disp_w/2, 550)
    easy_button = Button(screen, "Easy", font, 200, 100, disp_w*(1/6), 200)
    medium_button = Button(screen, "Medium", font, 200, 100, disp_w*(1/6), 325)
    hard_button = Button(screen, "Hard", font, 200, 100, disp_w*(1/6), 450)
    start_button = Button(screen, "Start", font, 200, 100, disp_w*(6/7), 650)
    rows_plus=Button(screen,"+",font,100,50,disp_w*(4/6),200)
    rows_minus=Button(screen,"-",font,100,50,disp_w*(5/6),200)
    cols_plus=Button(screen,"+",font,100,50,disp_w*(4/6),325)
    cols_minus=Button(screen,"-",font,100,50,disp_w*(5/6),325)
    bomb_plus=Button(screen,"+",font,100,50,disp_w*(4/6),450)
    bomb_minus=Button(screen,"-",font,100,50,disp_w*(5/6),450)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    main_menu = True
                    control_interface = False
                    options_interface = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if main_menu:
                    if play_button.check_collision():
                        options_interface = True
                        main_menu = False
                    if controls_button.check_collision():
                        control_interface = True
                        main_menu = False
                    if leaderboard_button.check_collision():
                        webbrowser.open(leaderboard_url,new=1)
                if options_interface:
                    if start_button.check_collision():
                        playing = True
                        while playing:
                            playing = minesweeper(screen, rows, columns, nbombs)
                    if easy_button.check_collision():
                        rows, columns, nbombs = 9, 9, 10
                    if medium_button.check_collision():
                        rows, columns, nbombs = 16, 16, 40
                    if hard_button.check_collision():
                        rows, columns, nbombs = 16, 30, 99                 
                    if rows_plus.check_collision():
                        rows+=1
                    if rows_minus.check_collision():
                        rows-=1
                    if cols_plus.check_collision():
                        columns+=1
                    if cols_minus.check_collision():
                        columns-=1
                    if bomb_plus.check_collision():
                        nbombs+=1
                    if bomb_minus.check_collision():
                        nbombs-=1

        rows,columns,nbombs=max(1,rows),max(1,columns),max(0,min(rows*columns,nbombs))
        screen.fill("Grey")
        if main_menu:
            screen.blit(example_surf, (0, 0))
            play_button.check_hover()
            play_button.draw()
            controls_button.check_hover()
            controls_button.draw()
            leaderboard_button.check_hover()
            leaderboard_button.draw()
        if control_interface:
            escape_button.draw()
            r_button.draw()
            m1_button.draw()
            m2_button.draw()
        if options_interface:
            start_button.draw()
            start_button.check_hover()
            easy_button.draw()
            easy_button.check_hover()
            medium_button.draw()
            medium_button.check_hover()
            hard_button.draw()
            hard_button.check_hover()
            rows_plus.draw()
            rows_plus.check_hover()
            rows_minus.draw()
            rows_minus.check_hover()
            cols_plus.draw()
            cols_plus.check_hover()
            cols_minus.draw()
            cols_minus.check_hover()
            bomb_plus.draw()
            bomb_plus.check_hover()
            bomb_minus.draw()
            bomb_minus.check_hover()         
            draw_text_on_screen(screen, "Manual:", font,
                                "Black", disp_w*(3/4), 100,False)
            draw_text_on_screen(screen, "Presets:", font,
                                "Black", disp_w*(1/6), 100,False)
            draw_text_on_screen(screen, f"Rows: {rows}", font, "Black", disp_w*(3/6)-50, 200,False)
            draw_text_on_screen(screen, f"Columns: {columns}", font, "Black", disp_w*(3/6)-50, 325,False)
            draw_text_on_screen(screen, f"Bombs: {nbombs}", font, "Black", disp_w*(3/6)-50, 450,False)

        pg.display.update()
        clock.tick(30)

def minesweeper(screen, rows, columns, nbombs):
    running = True
    lose = False
    win = False
    player_name=""
    enter_name=False
    sent_results=False
    mine_field = Board(rows, columns, pixels, nbombs)
    mine_field.generate_board()
    time_start=perf_counter()
    time_on=False
    time=0
    screen = pg.display.set_mode(
        ((columns)*(pixels+1), (rows)*(pixels+1)+pixels), pg.RESIZABLE)
    disp_w,disp_h=screen.get_size()
    if disp_w<441 or disp_h<489:
        screen=pg.display.set_mode((max(disp_w,441),max(disp_h,489)))
        disp_w,disp_h=screen.get_size()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    playing = False
                    screen = pg.display.set_mode((1024, 720), pg.RESIZABLE)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    running = False
                    playing = True

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                for i in range(mine_field.board.shape[0]):
                    for j in range(mine_field.board.shape[1]):
                        if mine_field.board[i][j].rect.collidepoint(pg.mouse.get_pos()):
                            revealed_value = mine_field.reveal(i, j)
                            if not time_on:
                                time_on=True
                                time_start=perf_counter()
                            if revealed_value != None:
                                if revealed_value == -1:
                                    mine_field.lose(i, j)
                                    lose = True

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                for r in mine_field.board:
                    for x in r:
                        if x.rect.collidepoint(pg.mouse.get_pos()):
                            x.flag()
            
            if enter_name:
                if event.type == pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        enter_name=False
                        sent_results=True
                        send_result_to_sheets(player_name,time,rows,columns,nbombs)
                    else:
                        if event.key==pg.K_BACKSPACE:
                            player_name=player_name[:-1]
                        else:
                            player_name+=event.unicode

        screen.fill("Black")
        for i in range(mine_field.board.shape[0]):
            for j in range(mine_field.board.shape[1]):
                screen.blit(mine_field.board[i][j].surf,
                            mine_field.board[i][j].rect)
                if mine_field.board[i][j].visible:
                    val = mine_field.board[i][j].value
                    if val > 0:
                        t_surf, t_rect = draw_text(
                            f"{val}", font, "Black", j*pixels+j+pixels/2, i*pixels+i+pixels/2+pixels,False)
                        screen.blit(t_surf, t_rect)
        if time_on:
            if not lose and not win:
                time=round(perf_counter()-time_start,1)
            draw_text_on_screen(screen, f"Time: {time}", font, "White", 10, 10,True)

        if mine_field.check_win() and not lose and not win:
            win = True
            mine_field.win()
            enter_name=True
            
        if lose:
            draw_popup_box(screen, "Black", 400,300,disp_w/2, disp_h/2,150)
            draw_text_on_screen(screen, "Press R to retry", font, "White", disp_w/2, disp_h/2, False)
            draw_text_on_screen(screen, "You lose!", font, "White", disp_w/2, disp_h/2-100, False)

        if enter_name:
            draw_popup_box(screen, "Black", 400,300,disp_w/2, disp_h/2,150)
            draw_text_on_screen(screen,player_name,font,"White",disp_w/2,disp_h/2+100,False)
            draw_text_on_screen(screen, "(Press enter to confirm)", font, "White", disp_w/2, disp_h/2, False)
            draw_text_on_screen(screen, "Enter your player name", font, "White", disp_w/2, disp_h/2-50, False)
            draw_text_on_screen(screen, "You won!", font, "White", disp_w/2, disp_h/2-100, False)
      
        if sent_results:
            draw_popup_box(screen, "Black", 400,300,disp_w/2, disp_h/2,150)
            draw_text_on_screen(screen,"Results sent",font,"White",disp_w/2,disp_h/2-50,False)
            draw_text_on_screen(screen,"to leaderboards",font,"White",disp_w/2,disp_h/2-10,False)
            draw_text_on_screen(screen,"Thank you for playing",font,"White",disp_w/2,disp_h/2+75,False)

        pg.display.update()
        clock.tick(30)

    return playing

main_menu(screen)


