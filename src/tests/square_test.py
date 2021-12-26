#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 06:42:45 2021

@author: emil
"""
import unittest
from square import Square


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.square = Square(0, 0, 48)

    def test_Square_init(self):
        s = Square(0, 0, 50)

    def test_Square_update_rect(self):
        self.square.update_rect("Red")
        self.assertEqual(self.square.surf.get_size(), (48, 48))

    def test_Square_flag(self):
        self.assertEqual(self.square.flagged, False)
        self.square.flag()
        self.assertEqual(self.square.flagged, True)
        self.square.flag()
        self.assertEqual(self.square.flagged, False)
        self.square.visible = True
        self.assertEqual(self.square.flag(), None)
