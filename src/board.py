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
    """
    Luokka, joka hallitsee pelin sovelluslogiikkaa ja miinaharavakentän esitystä

    Attributes
    ----------
    rows :
        rivien määrä.
    columns :
        sarakkeiden määrä.
    pixels :
        ruudun sivun pituus pikseleissä.
    nbombs :
        pommien määrä.
    board :
        miinaharavakentän array
    minefield :
        miinaharavakentän arvojen array

    """

    def __init__(self, rows, columns, pixels, nbombs):
        """
        Konstruktori

        Parameters
        ----------
        rows :
            rivien määrä.
        columns :
            sarakkeiden määrä.
        pixels :
            ruudun sivun pituus pikseleissä.
        nbombs :
            pommien määrä.

        Returns
        -------
        None.

        """
        self.rows = rows
        self.columns = columns
        self.pixels = pixels
        self.board = np.empty((rows, columns), dtype=object)
        self.nbombs = nbombs
        self.minefield = Minefield()

    def generate_board(self):
        """
        Generoi kentän jossa jokainen ruutu on Square olio

        Returns
        -------
        None.

        """
        self.minefield = Minefield()
        self.minefield.generate_minefield(self.rows, self.columns, self.nbombs)
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i][j] = Square(i, j, self.pixels)
                self.board[i][j].value = self.minefield.board[i][j]

    def reveal(self, i, j):
        """
        Rekursiivinen funktio joka paljastaa kaikki ruudut,
        jotka tulee paljastaa riippuen siitä mikä ruudun numero on

        Parameters
        ----------
        i :
            rivin indeksi.
        j :
            sarakkeen indeksi.

        Returns
        -------
        int
            Palauttaa klikatun ruudun numeron.

        """
        if i < 0 or j < 0 or i == self.board.shape[0] or j == self.board.shape[1]:
            return 0
        if self.board[i][j].visible or self.board[i][j].flagged:
            return 0
        if self.board[i][j].value == -1:
            return -1
        if self.board[i][j].value == 0:
            self.board[i][j].visible = True
            self.board[i][j].update_rect("White")
            for row in [i-1, i, i+1]:
                for col in [j-1, j, j+1]:
                    self.reveal(row, col)
        else:
            self.board[i][j].visible = True
            self.board[i][j].update_rect("White")
        return self.board[i][j].value

    def lose(self, i, j):
        """
        Paljastaa koko kentän ja päivittää Square olioiden graaffisen esityksen

        Parameters
        ----------
        i :
            rivin indeksi.
        j :
            sarakkeen indeksi.

        Returns
        -------
        None.

        """
        for row in self.board:
            for square in row:
                square.visible = True
                square.update_rect("White")
                if square.value == -1:
                    square.surf.blit(pg.image.load("images/mine48.png"), (0, 0))
        self.board[i][j].update_rect("Red")
        self.board[i][j].surf.blit(pg.image.load("images/mine48.png"), (0, 0))

    def win(self):
        """
        Paljastaa koko kentän ja päivittää Square olioiden graaffisen esityksen

        Returns
        -------
        None.

        """
        for row in self.board:
            for square in row:
                square.visible = True
                square.update_rect("White")
                if square.value == -1:
                    square.surf.blit(pg.image.load(
                        "images/mine_defused48.png"), (0, 0))

    def check_win(self):
        """
        Tarkastaa jos kaikki ruudut joissa ei ole pommia ovat paljastettu.

        Returns
        -------
        bool
            True jos voiton ehdot täyttyvät.

        """
        counter = 0
        for row in self.board:
            for square in row:
                if not square.visible and square.value != -1:
                    counter += 1
        if counter == 0:
            return True
        return False
