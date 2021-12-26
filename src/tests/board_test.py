#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 06:44:20 2021

@author: emil
"""
import unittest
import random
from board import Minefield, Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(10, 10, 48, 9)

    def test_Board_generate_board(self):
        random.seed(1)
        self.board.generate_board()
        m = Minefield()
        random.seed(1)
        m.generate_minefield(10, 10, 9)
        for i in range(m.board.shape[0]):
            for j in range(m.board.shape[1]):
                self.assertEqual(self.board.board[i][j].value, m.board[i][j])

    def test_reveal(self):
        random.seed(1)
        board2 = Board(3, 3, 48, 2)
        board2.generate_board()
        board2.reveal(3, 3)
        for x in board2.board:
            for y in x:
                self.assertEqual(y.visible, False)
        board2.reveal(0, 0)
        for i in range(3):
            for j in range(3):
                if i == 0 and j == 0:
                    self.assertEqual(board2.board[i][j].visible, True)
                else:
                    self.assertEqual(board2.board[i][j].visible, False)
        board2.reveal(2, 2)
        for i in range(3):
            for j in range(3):
                if i == 0 and (j == 1 or j == 2):
                    self.assertEqual(board2.board[i][j].visible, False)
                else:
                    self.assertEqual(board2.board[i][j].visible, True)
        board2.reveal(0, 0)
        for i in range(3):
            for j in range(3):
                if i == 0 and (j == 1 or j == 2):
                    self.assertEqual(board2.board[i][j].visible, False)
                else:
                    self.assertEqual(board2.board[i][j].visible, True)
        self.assertEqual(board2.reveal(0, 1), -1)

    def test_lose(self):
        board3 = Board(6, 6, 48, 8)
        board3.generate_board()
        board3.lose(0, 0)
        for x in board3.board:
            for y in x:
                self.assertEqual(y.visible, True)

    def test_win(self):
        board4 = Board(6, 6, 48, 8)
        board4.generate_board()
        board4.win()
        for x in board4.board:
            for y in x:
                self.assertEqual(y.visible, True)

    def test_check_win(self):
        board5 = Board(3, 3, 48, 3)
        random.seed(1)
        board5.generate_board()
        self.assertEqual(board5.check_win(), False)
        board5.reveal(0, 0)
        self.assertEqual(board5.check_win(), False)
        board5.reveal(2, 0)
        self.assertEqual(board5.check_win(), False)
        board5.reveal(1, 2)
        self.assertEqual(board5.check_win(), True)
