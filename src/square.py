#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 06:39:34 2021

@author: emil
"""
import pygame as pg

class Square():
    def __init__(self, i, j, pixels):
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
        self.surf.fill(color)
        self.rect = self.surf.get_rect(
            topleft=(self.j*self.pixels+self.j, self.i*self.pixels+self.i+self.pixels))

    def flag(self):
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