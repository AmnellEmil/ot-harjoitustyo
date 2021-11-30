#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 06:05:11 2021

@author: emil
"""
import random
import numpy as np
import pygame as pg


class Minefield():
    def __init__(self):
        self.board = []

    def add_one(self, i, j):
        if i < 0 or j < 0 or i == self.board.shape[0] or j == self.board.shape[1]:
            return False
        if self.board[i][j] == -1:
            return False
        self.board[i][j] += 1
        return True

    def generate_minefield(self, rows, columns, nbombs):
        self.board = np.zeros((rows, columns), dtype=int)
        list_of_locations = [(i, j) for i in range(self.board.shape[0])
                             for j in range(self.board.shape[1])]
        bomb_locations = random.sample(list_of_locations, nbombs)
        for x in bomb_locations:
            a, b = x
            self.board[a][b] = -1
            for i in [a-1, a, a+1]:
                for j in [b-1, b, b+1]:
                    self.add_one(i, j)
        return self.board


class Square():
    def __init__(self, i, j, pixels):
        self.i = i
        self.j = j
        self.pixels = pixels
        self.surf = pg.Surface((pixels, pixels))
        self.surf.fill("Grey")
        self.rect = self.surf.get_rect(topleft=(j*pixels+j, i*pixels+i))
        self.flagged = False
        self.visible = False
        self.value = 0

    def update_rect(self, color):
        self.surf.fill(color)
        self.rect = self.surf.get_rect(
            topleft=(self.j*self.pixels+self.j, self.i*self.pixels+self.i))

    def flag(self):
        if self.visible:
            return
        if self.flagged:
            self.flagged = False
            self.update_rect("Grey")
        else:
            self.flagged = True
            self.surf.blit(pg.image.load("images/flag48.png"), (0, 0))
            self.rect = self.surf.get_rect(
                topleft=(self.j*self.pixels+self.j, self.i*self.pixels+self.i))


class Board():
    def __init__(self, rows, columns, pixels, nbombs):
        self.rows = rows
        self.columns = columns
        self.pixels = pixels
        self.board = np.empty((rows, columns), dtype=object)
        self.field = []
        self.nbombs = nbombs
        self.minefield = Minefield()

    def generate_board(self):
        self.minefield = Minefield()
        self.minefield.generate_minefield(self.rows, self.columns, self.nbombs)
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i][j] = Square(i, j, self.pixels)
                self.board[i][j].value = self.minefield.board[i][j]

    def reveal(self, i, j):
        if i < 0 or j < 0 or i == self.board.shape[0] or j == self.board.shape[1]:
            return
        if self.board[i][j].visible or self.board[i][j].flagged:
            return
        if self.board[i][j].value == -1:
            return -1
        if self.board[i][j].value == 0:
            self.board[i][j].visible = True
            self.board[i][j].update_rect("White")
            for a in [i-1, i, i+1]:
                for b in [j-1, j, j+1]:
                    self.reveal(a, b)
        else:
            self.board[i][j].visible = True
            self.board[i][j].update_rect("White")
        return self.board[i][j].value

    def lose(self, i, j):
        for row in self.board:
            for s in row:
                s.visible = True
                s.update_rect("White")
                if s.value == -1:
                    s.surf.blit(pg.image.load("images/mine48.png"), (0, 0))
        self.board[i][j].update_rect("Red")
        self.board[i][j].surf.blit(pg.image.load("images/mine48.png"), (0, 0))

    def win(self):
        for row in self.board:
            for s in row:
                s.visible = True
                s.update_rect("White")
                if s.value == -1:
                    s.surf.blit(pg.image.load(
                        "images/mine_defused48.png"), (0, 0))

    def check_win(self):
        counter = 0
        for row in self.board:
            for s in row:
                if not s.visible and s.value != -1:
                    counter += 1
        if counter == 0:
            return True
        else:
            return False
