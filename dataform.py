# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 09:38:46 2020

@author: magnu
"""
from openpyxl import *
from tkinter import *
import pandas as pd



def submit_fields():
    path = 'https://d.docs.live.net/7b9f028d3d062d20/Documents/Book1.xls'
    df1 = pd.read_html('https://d.docs.live.net/7b9f028d3d062d20/Documents/Book1.xlsx')
    SeriesA = df1['id']
    SeriesB = df1['radius_mean']
    SeriesC = df1['texture_mean']
   # SeriesD = df1['radius_mean']
    SeriesE = df1['perimeter_mean']
    SeriesF = df1['area_mean']
    SeriesG = df1['smoothness_mean']
    SeriesH = df1['compactness_mean']
   # SeriesI = df1['texture_mean']
    SeriesJ = df1['concavity_mean']
    SeriesK = df1['concave points_mean']
    SeriesL = df1['symmetry_mean']
    SeriesM = df1['fractal_dimension_mean']
    SeriesN = df1['radius_se']
    SeriesO = df1['texture_se']
    SeriesP = df1['perimeter_se']
    SeriesQ = df1['area_se']
    SeriesR = df1['smoothness_se']
    SeriesS = df1['compactness_se']
    SeriesT = df1['concavity_se']
    SeriesU = df1['concave points_se']
    SeriesV = df1['symmetry_se']
    SeriesW = df1['fractal_dimension_se']
    SeriesX = df1['radius_worst']
    SeriesY = df1['texture_worst']
    SeriesZ = df1['perimeter_worst']
    SeriesA1 = df1['area_worst']
    SeriesB1= df1['smoothness_worst']
    SeriesC1= df1['compactness_worst']
    SeriesD1= df1['concavity_worst']
    SeriesE1= df1['concave points_worst']
    SeriesF1= df1['symmetry_worst']
    SeriesG1= df1['fractal_dimension_worst']
    
    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    C = pd.Series(entry3.get())
   # D = pd.Series(entry4.get())
    E = pd.Series(entry5.get())
    F = pd.Series(entry6.get())
    G = pd.Series(entry7.get())
    H = pd.Series(entry8.get())
    #I = pd.Series(entry9.get())
    J = pd.Series(entry10.get())
    K = pd.Series(entry11.get())
    L = pd.Series(entry12.get())
    M = pd.Series(entry13.get())
    N = pd.Series(entry14.get())
    O = pd.Series(entry15.get())
    P = pd.Series(entry16.get())
    Q = pd.Series(entry17.get())
    R = pd.Series(entry18.get())
    S = pd.Series(entry19.get())
    T = pd.Series(entry20.get())
    U = pd.Series(entry21.get())
    V = pd.Series(entry22.get())
    W = pd.Series(entry23.get())
    X = pd.Series(entry24.get())
    Y = pd.Series(entry25.get())
    Z = pd.Series(entry26.get())
    A1 = pd.Series(entry27.get())
    B1= pd.Series(entry28.get())
    C1= pd.Series(entry29.get())
    D1= pd.Series(entry30.get())
    E1 = pd.Series(entry31.get())
    F1= pd.Series(entry32.get())
    G1= pd.Series(entry33.get())
    
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    SeriesC = SeriesA.append(C)
   # SeriesD = SeriesB.append(D)
    SeriesE = SeriesA.append(E)
    SeriesF = SeriesB.append(F)
    SeriesG = SeriesA.append(G)
    SeriesH = SeriesB.append(H)
    #SeriesI = SeriesA.append(I)
    SeriesJ = SeriesB.append(J)
    SeriesK = SeriesA.append(K)
    SeriesL = SeriesB.append(L)
    SeriesM = SeriesA.append(M)
    SeriesN = SeriesB.append(N)
    SeriesO = SeriesA.append(O)
    SeriesP = SeriesB.append(P)
    SeriesQ = SeriesA.append(Q)
    SeriesR = SeriesB.append(R)
    SeriesS = SeriesA.append(S)
    SeriesT = SeriesB.append(T)
    SeriesU= SeriesA.append(U)
    SeriesV = SeriesB.append(V)
    SeriesW = SeriesA.append(W)
    SeriesX = SeriesB.append(X)
    SeriesY = SeriesA.append(Y)
    SeriesZ = SeriesB.append(Z)
    SeriesA1 = SeriesA.append(A1)
    SeriesB1 = SeriesB.append(B1)
    SeriesC1 = SeriesA.append(C1)
    SeriesD1 = SeriesB.append(D1)
    SeriesE1 = SeriesA.append(E1)
    SeriesF1 = SeriesB.append(F1)
    SeriesG1 = SeriesA.append(G1)

    df2 = pd.DataFrame({"id":SeriesA, "radius_mean":SeriesB, "texture_mean":SeriesC, "perimeter_mean":SeriesE, "area_mean":SeriesF, "smoothness_mean":SeriesG, "compactness_mean":SeriesH, "concativity_mean":SeriesJ, "concave points_mean":SeriesK, "symmetry_mean":SeriesL, "fractal_dimension_mean":SeriesM, "radius_se":SeriesN, "texture_se":SeriesO, "perimeter_se":SeriesP, "area_se":SeriesQ, "smoothness_se":SeriesR, "compactness_se":SeriesS, "concavity_se":SeriesT, "concave points_se":SeriesU, "symmetry_se":SeriesV, "fractal_dimension_se":SeriesW, "radius_worst":SeriesX, "texture_worst":SeriesY,"perimeter_worst":SeriesZ, "area_worst":SeriesA1, "smoothness_worst":SeriesB1, "compactness_worst":SeriesC1, "concavity_worst":SeriesD1, "concave points_worst":SeriesE1, "symmetry_worst":SeriesF1,"fractal_dimension_worst":SeriesG1})
    df2.to_excel(path, index=False)
    df2.save(path)
    entry1.delete(0, END)
    entry2.delete(0, END)

master = Tk()
master.title("Feature dimensions data entry")

master.configure(background='white') 

Label(master, text="id",).grid(row=0)
Label(master, text="radius_mean").grid(row=1)
Label(master, text="texture_mean").grid(row=2)
Label(master, text="perimeter_mean").grid(row=3)
Label(master, text="area_mean").grid(row=4)
Label(master, text="smoothness_mean").grid(row=5)
Label(master, text="compactness_mean").grid(row=6)
#Label(master, text="texture_mean").grid(row=1)
Label(master, text="concavity_mean").grid(row=7)
Label(master, text="concave points_mean").grid(row=8)
Label(master, text="symmetry_mean").grid(row=9)
Label(master, text="fractal_dimension_mean").grid(row=10)
Label(master, text="radius_se").grid(row=11)
Label(master, text="texture_se").grid(row=12)
Label(master, text="perimeter_se").grid(row=13)
Label(master, text="smoothness_se").grid(row=14)
Label(master, text="compactness_se").grid(row=15)
Label(master, text="concavity_se").grid(row=16)
Label(master, text="concave points_se").grid(row=17)
Label(master, text="symmetry_se").grid(row=18)
Label(master, text="fractal_dimension_se").grid(row=19)
Label(master, text="radius_worst").grid(row=20)
Label(master, text="texture_worst").grid(row=21)
Label(master, text="perimeter_worst").grid(row=22)
Label(master, text="smoothness_worst").grid(row=23)
Label(master, text="compactness_worst").grid(row=24)
Label(master, text="concavity_worst").grid(row=25)
Label(master, text="concave points_worst").grid(row=26)
Label(master, text="symmetry_worst").grid(row=27)
Label(master, text="fractal_dimension_worst").grid(row=28)


entry1 = Entry(master)
entry2 = Entry(master)
entry3 = Entry(master)
#entry4 = Entry(master)
entry5 = Entry(master)
entry6 = Entry(master)
entry7 = Entry(master)
entry8 = Entry(master)
#entry9 = Entry(master)
entry10 = Entry(master)
entry11= Entry(master)
entry12 = Entry(master)
entry13= Entry(master)
entry14= Entry(master)
entry15= Entry(master)
entry16= Entry(master)
entry17= Entry(master)
entry18= Entry(master)
entry19= Entry(master)
entry20= Entry(master)
entry21= Entry(master)
entry22= Entry(master)
entry23= Entry(master)
entry24= Entry(master)
entry25= Entry(master)
entry26= Entry(master)
entry27= Entry(master)
entry28= Entry(master)
entry29= Entry(master)
entry30= Entry(master)
entry31= Entry(master)
entry32= Entry(master)
entry33= Entry(master)


entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry5.grid(row=3, column=1)
entry6.grid(row=4, column=1)
entry7.grid(row=5, column=1)
entry8.grid(row=6, column=1)
entry10.grid(row=7, column=1)
entry11.grid(row=8, column=1)
entry12.grid(row=9, column=1)
entry13.grid(row=10, column=1)
entry14.grid(row=11, column=1)
entry15.grid(row=12, column=1)
entry16.grid(row=13, column=1)
entry17.grid(row=14, column=1)
entry18.grid(row=15, column=1)
entry19.grid(row=16, column=1)
entry20.grid(row=17, column=1)
entry21.grid(row=18, column=1)
entry22.grid(row=19, column=1)
entry23.grid(row=20, column=1)
entry24.grid(row=21, column=1)
entry25.grid(row=22, column=1)
entry26.grid(row=23, column=1)
entry27.grid(row=24, column=1)
entry28.grid(row=25, column=1)
entry29.grid(row=26, column=1)
entry30.grid(row=27, column=1)
entry31.grid(row=28, column=1)
#entry32.grid(row=29, column=1)
#entry33.grid(row=30, column=1)

Button(master, text='Quit', command=master.destroy).grid(row=31,column=0, pady=4)
Button(master, text='Submit', command=submit_fields).grid(row=31,column=1, pady=4)

mainloop()