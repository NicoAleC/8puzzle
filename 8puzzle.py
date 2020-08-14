# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:05:00 2020

@author: Nico
"""
import numpy as np
import sys

sys.setrecursionlimit(10000)

objetivo = np.matrix('0 1 2; 3 4 5; 6 7 8')
movimientos = []
pasos = []
pasados = []

#tablero = np.matrix('3 7 5; 0 8 2; 1 4 6') imposible
#tablero = np.matrix('2 1 0; 3 4 5; 6 7 8') imposible
#tablero = np.matrix('1 2 0; 3 4 5; 6 7 8')
tablero = np.matrix('6 1 3; 0 2 8; 4 7 5')
pasos.append(tablero)

def imprimirTablero(tablero):
    for i in range(0,3):
        print(tablero[i])
    print("\n")

def verificarFilasColumnas(tab):
    aux = tab == objetivo
    verif = lambda lista, i: lista[0].item(i - 1) == True if i == 3 else lista[0].item(i - 1) == lista[0].item(i) and verif(lista, i + 1) 
    filas = [False, False, False]
    columnas = [False, False, False]
    
    for i in range(0, 3):
        filas[i] = verif(aux[i], 1)
    
    auxT = aux.T
    for i in range(0, 3):
        columnas[i] = verif(auxT[i], 1)
    
    return filas, columnas

def posiblesMovimientos(tab, mov, paso, pasa):
    aux = []
    aux2 = []
    _x, _y = np.where(tab == 0)
    x = _x[0]
    y = _y[0]
    
    filas, columnas = verificarFilasColumnas(tab)
    verif = lambda elem, lista, i: False if i >= len(lista) else (elem == lista[i]).all() or verif(elem, lista, i + 1)
    
    print(filas, columnas)

    posibles = 0
    if x + 1 < 3:
        aux = tab.copy()
        aux[x, y] = tab[x+1].item(y)
        aux[x+1, y] = 0
        #print(filas[x+1])
        if not(verif(aux, paso, 0)) and not(verif(aux, mov, 0)) and not(verif(aux, pasa, 0)) and not(filas[x+1]):
            mov.append(aux.copy())
            aux2.append(aux.copy())
            posibles = posibles + 1
    if x - 1 >= 0:
        aux = tab.copy()
        aux[x, y] = tab[x-1].item(y)
        aux[x-1, y] = 0
        #print(filas[x-1])
        if not(verif(aux, paso, 0)) and not(verif(aux, mov, 0)) and not(verif(aux, pasa, 0)) and not(filas[x-1]):
            mov.append(aux.copy())
            aux2.append(aux.copy())
            posibles = posibles + 1
    if y + 1 < 3:
        aux = tab.copy()
        aux[x, y] = tab[x].item(y+1)
        aux[x, y+1] = 0
        #print(columnas[y+1])
        if not(verif(aux, paso, 0)) and not(verif(aux, mov, 0)) and not(verif(aux, pasa, 0)) and not(columnas[y+1]):
            mov.append(aux.copy())
            aux2.append(aux.copy())
            posibles = posibles + 1
    if y - 1 >= 0:
        aux = tab.copy()
        aux[x, y] = tab[x].item(y-1)
        aux[x, y-1] = 0
        #print(columnas[y-1])
        if not(verif(aux, paso, 0)) and not(verif(aux, mov, 0)) and not(verif(aux, pasa, 0)) and not(columnas[y-1]):
            mov.append(aux.copy())
            aux2.append(aux.copy())
            posibles = posibles + 1
    return posibles, aux2

def mover(tab, mov, paso, pasa, contador):
    aux = []
    if contador % 1 == 0:
        print("profundidad = " + str(contador))
        print(tab)
    if (tab == objetivo).all():
        paso.append(tab)
        print("Resultado encontrado!!!!!!!!!!")
        for i in range(0,len(paso)):
            imprimirTablero(paso[i])
        print("Resultado encontrado!!!!!!!!!!")
        return True
    else:
        posibles, caminos = posiblesMovimientos(tab, mov, paso, pasa)
        if contador % 1 == 0:
            print("caminos...........")
            for i in range(0, len(caminos)):
                print(caminos[i])
        if posibles <= 0:
            pasa.append(paso.pop().copy())
            aux = paso.pop().copy()
            return mover(aux, mov, paso, pasa, contador + 1)
        else:
            aux = mov.pop().copy()
            paso.append(aux.copy())
            return mover(aux, mov, paso, pasa, contador + 1)

#buscar()
#print(tablero == objetivo)
mover(tablero, movimientos, pasos, pasados, contador=0)

#print(verificarFilasColumnas(tablero))
#imprimirTablero(tablero)

print("-----------------posibles movimientos--------------")
#pasos.append([[3, 7, 5],[1, 8, 2],[0, 4, 6]])
#posiblesMovimientos(tablero, movimientos, pasos)
#for i in range(0,len(movimientos)):
#    print(i)
#    print(movimientos[i])
print("-----------------posibles movimientos--------------")

#print((objetivo == tablero).all())
#print(objetivo)
#i, j = np.where(objetivo == 9)
#print(i[0], j[0])
#print(tablero)
#print((objetivo == objetivo).all())