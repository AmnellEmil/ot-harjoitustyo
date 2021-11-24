#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:44:13 2021

@author: emil
"""
import unittest
import numpy as np
from Board import add_one,generate_board

def check_surrounding_bombs(board,i,j):
    number=board[i][j]
    counter=0
    if number==-1:
        return 1
    for x in [i-1,i,i+1]:
        for y in [j-1,j,j+1]:
            if x<0 or y<0 or x==len(board) or y==len(board[0]):
                continue
            if board[x][y]==-1:
                counter+=1
    if counter==number:
        return 1
    return 0
            

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board=[]
        
    def test_add_one_works(self):
        board=np.zeros((5,5),dtype=int)
        add_one(1,1,board)
        self.assertEqual(board[1][1],1)
        board[0][0]=-1
        self.assertEqual(add_one(0,0,board),False)
        self.assertEqual(add_one(-1,-1,board),False)
        self.assertEqual(add_one(5,5,board),False)
        self.assertEqual(add_one(2,5,board),False)
        self.assertEqual(add_one(2,-1,board),False)
        
    def test_count_bombs_works(self):
        board_false=np.array([[-1,-1],[-1,2]])
        board_true=np.array([[1,1],[1,-1]])
        self.assertEqual(check_surrounding_bombs(board_false,1,1),0)
        self.assertEqual(check_surrounding_bombs(board_true,1,1),1)
        self.assertEqual(check_surrounding_bombs(board_true,0,1),1)
        
    def test_generate_board_works(self):
        board=generate_board(6,6,10)
        valid_squares=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                valid_squares+=check_surrounding_bombs(board,i,j)
        self.assertEqual(valid_squares,6*6)