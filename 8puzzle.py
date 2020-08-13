# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:05:00 2020

@author: Nico
"""
import copy

objetivo = [[0,1,2],[3,4,5],[6,7,8]]
tablero = [[3,7,5],[0,8,2],[1,4,6]]
movimientos = []
pasos= []
tablero2 = [[0,1,2],[3,4,5],[6,7,8]]

def imprimirTablero(tablero):
    for i in range(0,3):
        print(tablero[i])
    print("\n")

def posiblesMovimientos(tab, mov):
    aux = []
    x = 0
    y = 0
    for i in range(0,3):
        if tab[i].count(0) > 0:
            x = i
            y = tab[i].index(0)
    
    print("x = " + str(x))
    print("y = " + str(y))
    
    if x + 1 < 3:
        print("x+1")
        aux = copy.deepcopy(tab)
        aux[x][y] = tab[x+1][y]
        aux[x+1][y] = 0
        mov.append(aux)
        imprimirTablero(aux)
        imprimirTablero(tab)
    if x - 1 >= 0:
        print("x-1")
        aux = copy.deepcopy(tab)
        aux[x][y] = tab[x-1][y]
        aux[x-1][y] = 0
        mov.append(aux)
        imprimirTablero(aux)
        imprimirTablero(tab)
    if y + 1 < 3:
        print("y+1")
        aux = copy.deepcopy(tab)
        aux[x][y] = tab[x][y+1]
        aux[x][y+1] = 0
        mov.append(aux)
        imprimirTablero(aux)
        imprimirTablero(tab)
    if y - 1 >= 0:
        print("y-1")
        aux = copy.deepcopy(tab)
        aux[x][y] = tab[x][y-1]
        aux[x][y-1] = 0
        mov.append(aux)
        imprimirTablero(aux)
        imprimirTablero(tab)

imprimirTablero(tablero)
print("-----------------posibles movimientos--------------")
posiblesMovimientos(tablero, movimientos)
#for i in range(0,len(movimientos)):
#    imprimirTablero(movimientos[i])

print("-----------------posibles movimientos--------------")
imprimirTablero(objetivo)
print(objetivo == tablero)
print(objetivo == tablero2)