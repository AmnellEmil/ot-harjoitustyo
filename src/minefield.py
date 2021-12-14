#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 06:38:52 2021

@author: emil
"""

import random
import numpy as np


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