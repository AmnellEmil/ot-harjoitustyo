#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:44:13 2021

@author: emil
"""
import unittest
import numpy as np
from Board import add_one

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board=[]
        
    def test_addone_works(self):
        board=np.zeros((5,5),dtype=int)
        #board=[[0]*5]*5
        add_one(1,1,board)
        self.assertEqual(board[1][1],1)
        board[0][0]=-1
        self.assertEqual(add_one(0,0,board),False)
        self.assertEqual(add_one(-1,-1,board),False)
        self.assertEqual(add_one(5,5,board),False)
        self.assertEqual(add_one(2,5,board),False)
        self.assertEqual(add_one(2,-1,board),False)