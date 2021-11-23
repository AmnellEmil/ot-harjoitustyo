#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:42:40 2021

@author: emil
"""
import numpy as np
import random

print("Olen toteuttanut nyt kentän generoinnin miinaharavapelilleni, mutta en saa toimimaan generointia poetryn coverage-report komennolla, koska poetry antaa vaan virheilmoituksia kun yritän lisätä numpyn ja random paketit poetryyn, joita tarvitsen genrointiin. Kuitenkin 'pytest src' toimii kyllä virtuaaliympäristön ulkopuolella.")

def add_one(i,j,board):
    if i<0 or j<0 or i==len(board) or j==len(board[0]):
        return False
    if board[i][j]==-1:
        return False
    board[i][j]+=1 
    return True

def generate_board(rows,columns,nbombs):
    board=np.zeros((rows,columns),dtype=int)
#    board=[[0]*columns]*rows
    list_of_locations=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            list_of_locations.append((i,j))
    bomb_locations=random.sample(list_of_locations,nbombs)
    for x in bomb_locations:
        board[x[0]][x[1]]=-1
        for i in [x[0]-1,x[0],x[0]+1]:
            for j in [x[1]-1,x[1],x[1]+1]:
               add_one(i,j,board)
    return board

print("Generoidaan esimerkiksi kenttä, joka on 8x8 ja olkoon kentässä 12 pommia")
print(generate_board(8,8,12))
print("(-1 on pommi)")
    