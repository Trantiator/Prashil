# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:48:44 2020

@author: Prashil
"""

import pandas as pd


data = pd.read_csv("WorldCupMatches.csv")
print("1:Total number of Goals scored in the city called Montevideo")

df = pd.DataFrame(data)
print(df.head())
Totalgoal = data['Home Team Goals'] + data['Away Team Goals']
df['totalgoal']= Totalgoal
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(data.head())
datas = data.groupby("City")
datas.agg({"totalgoal" : ["sum"]})


print("2:Total number of referee assigned in Argentena")
print(data.groupby('Home Team Name')['Referee'].nunique())

print("3:Maximum number of Goals scored by hometeam")
data.groupby(['Home Team Goals']).max()




