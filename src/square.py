#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 06:39:34 2021

@author: emil
"""
import pygame as pg


class Square():
    """
    Luokka, joka sisältää kaiken tärkeän tiedon pelin kentän ruudusta

    Attributes
    ----------
    i :
        ruudun riviindeksi.
    j :
        ruudun sarakeindeksi.
    pixels :
        ruudun sivun pituus pixeleissä.
    surf :
        pg.Surface olio, sisältää tiedon ruudun graaffisesta esittelystä.
    rect :
        pg.Rect olio, sisältää tiedon ruudun paikasta tietokoneruudulla
    visible :
        totuusarvo joka kertoo onko ruutu paljastettu.
    flagged :
        totuusarvo joka kertoo onko ruutu liputettu.
    value :
        ruudun arvo, vieressä olevien pommien määrä
    """

    def __init__(self, i, j, pixels):
        """
        Konstruktori

        Parameters
        ----------
        i :
            ruudun riviindeksi.
        j :
            ruudun sarakeindeksi.
        pixels :
            ruudun sivun pituus pixeleissä.

        Returns
        -------
        None.

        """
        self.i = i
        self.j = j
        self.pixels = pixels
        self.surf = pg.Surface((pixels, pixels))
        self.surf.fill("Grey")
        self.rect = self.surf.get_rect(topleft=(j*pixels+j, i*pixels+i+pixels))
        self.flagged = False
        self.visible = False
        self.value = 0

    def update_rect(self, color):
        """
        Värittää ruudun jollain värillä

        Parameters
        ----------
        color :
            väri, jolla ruutu väritetään.

        Returns
        -------
        None.

        """
        self.surf.fill(color)
        self.rect = self.surf.get_rect(
            topleft=(self.j*self.pixels+self.j, self.i*self.pixels+self.i+self.pixels))

    def flag(self):
        """
        Antaa/poistaa liputetun statuksen ruudulta

        Returns
        -------
        None.

        """
        if self.visible:
            return
        if self.flagged:
            self.flagged = False
            self.update_rect("Grey")
        else:
            self.flagged = True
            self.surf.blit(pg.image.load("images/flag48.png"), (0, 0))
            self.rect = self.surf.get_rect(
                topleft=(self.j*self.pixels+self.j, self.i*self.pixels+self.i+self.pixels))
