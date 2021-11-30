#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:44:13 2021

@author: emil
"""
import unittest
import numpy as np
from board import Minefield,Square,Board


def check_surrounding_bombs(board, i, j):
    number = board[i][j]
    counter = 0
    if number == -1:
        return 1
    for x in [i-1, i, i+1]:
        for y in [j-1, j, j+1]:
            if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
                continue
            if board[x][y] == -1:
                counter += 1
    if counter == number:
        return 1
    return 0


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.minefield = Minefield()
        
    def test_minefield_init(self):
        m=Minefield()
        self.assertEqual(m.board,[])

    def test_add_one_works(self):
        self.minefield.board = np.zeros((5, 5), dtype=int)
        self.minefield.add_one(1,1)
        self.assertEqual(self.minefield.board[1][1], 1)
        self.minefield.board[0][0] = -1
        self.assertEqual(self.minefield.add_one(0, 0), False)
        self.assertEqual(self.minefield.add_one(-1, -1), False)
        self.assertEqual(self.minefield.add_one(5, 5), False)
        self.assertEqual(self.minefield.add_one(2, 5), False)
        self.assertEqual(self.minefield.add_one(2, -1), False)

    def test_check_surrounding_bombs_works(self):
        board_false = np.array([[-1, -1], [-1, 2]])
        board_true = np.array([[1, 1], [1, -1]])
        self.assertEqual(check_surrounding_bombs(board_false, 1, 1), 0)
        self.assertEqual(check_surrounding_bombs(board_true, 1, 1), 1)
        self.assertEqual(check_surrounding_bombs(board_true, 0, 1), 1)

    def test_generate_board_works(self):
        self.minefield.generate_minefield(6,6,10)
        valid_squares = 0
        for i in range(self.minefield.board.shape[0]):
            for j in range(self.minefield.board.shape[1]):
                valid_squares += check_surrounding_bombs(self.minefield.board, i, j)
        self.assertEqual(valid_squares, 6*6)
        
    def test_Square_init(self):
        square=Square(0,0,50)
        
    def test_Square_update_rect(self):
        square=Square(0,0,50)
        square.update_rect("Red")
        self.assertEqual(square.surf.get_size(),(50,50))
        























