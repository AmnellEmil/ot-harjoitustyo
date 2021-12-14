#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 06:05:11 2021

@author: emil
"""
import numpy as np
import pygame as pg
from minefield import Minefield
from square import Square

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
