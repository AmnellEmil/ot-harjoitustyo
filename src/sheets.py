#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:39:45 2021

@author: emil
"""

import pandas as pd
import pygsheets

def send_result_to_sheets(name,time,rows,columns,bombs):
    gc=pygsheets.authorize(service_file="ot-harjoitustyo-035eb11cf15a.json")
    sh=gc.open("Ot-harjoitustyo High Scores")
    wks=sh[0]
    sheet=wks.get_as_df()
    preset="Custom"
    if rows==9 and columns==9 and bombs==10:
        preset="Easy"
    if rows==16 and columns==16 and bombs==40:
        preset="Medium"
    if rows==16 and columns==30 and bombs==99:
        preset="Hard"
    if name=="":
        name="Anonymous"
    entry=pd.Series([name,time,rows,columns,bombs,preset],index=sheet.columns)
    sheet=sheet.append(entry,ignore_index=True)
    wks.set_dataframe(sheet,(1,1))
