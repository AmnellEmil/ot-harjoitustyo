#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 06:38:52 2021

@author: emil
"""

import random
import numpy as np


class Minefield():
    """ Luokka, jolla generoidaan miinaharavakenttä

    Attributes:
        board: kentän arvojen representaatio np.array:na
    """

    def __init__(self):
        """
        Konstruktori

        Returns
        -------
        None.

        """
        self.board = []

    def add_one(self, i, j):
        """
        Kasvattaa jonkun ruudun arvoa yhdellä

        Parameters
        ----------
        i :
            rivi indeksi.
        j :
            sarake indeksi.

        Returns
        -------
        bool
            palauttaa True jos kasvattaminen onnistui.

        """
        if i < 0 or j < 0 or i == self.board.shape[0] or j == self.board.shape[1]:
            return False
        if self.board[i][j] == -1:
            return False
        self.board[i][j] += 1
        return True

    def generate_minefield(self, rows, columns, nbombs):
        """
        Generoi satunnaisen miinaharavakentän

        -1 Viittaa pommiin

        Parameters
        ----------
        rows :
            rivien määrä.
        columns :
            sarakkeiden määrä.
        nbombs :
            pommien määrä.

        Returns
        -------
        np.array
            generoitu kenttä.

        """
        self.board = np.zeros((rows, columns), dtype=int)
        list_of_locations = [(i, j) for i in range(self.board.shape[0])
                             for j in range(self.board.shape[1])]
        bomb_locations = random.sample(list_of_locations, nbombs)
        for place in bomb_locations:
            aaa, bbb = place
            self.board[aaa][bbb] = -1
            for i in [aaa-1, aaa, aaa+1]:
                for j in [bbb-1, bbb, bbb+1]:
                    self.add_one(i, j)
        return self.board
