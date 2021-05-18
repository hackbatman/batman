import sys
import numpy as np
from tkinter import *

#incio calculo de matrices

N=30


matriz_add =np.zeros((N,N), dtype=int)

#matriz adyacencia
matriz_add[0,1]=1
matriz_add[0,2]=1
matriz_add[0,4]=1
matriz_add[0,5]=1
matriz_add[0,6]=1
matriz_add[0,7]=1
matriz_add[0,14]=1
matriz_add[0,16]=1

matriz_add[1,0]=1
matriz_add[1,2]=1
matriz_add[1,12]=1
matriz_add[1,16]=1

matriz_add[2,0]=1
matriz_add[2,1]=1
matriz_add[2,12]=1

matriz_add[3,4]=1
matriz_add[3,6]=1

matriz_add[4,0]=1
matriz_add[4,2]=1
matriz_add[4,3]=1

matriz_add[5,0]=1
matriz_add[5,6]=1
matriz_add[5,11]=1

matriz_add[6,0]=1
matriz_add[6,3]=1
matriz_add[6,5]=1
matriz_add[6,0]=1

matriz_add[7,0]=1
matriz_add[7,8]=1
matriz_add[7,14]=1

matriz_add[8,7]=1
matriz_add[8,9]=1
matriz_add[8,10]=1

matriz_add[9,8]=1
matriz_add[9,10]=1
matriz_add[9,11]=1

matriz_add[10,8]=1
matriz_add[10,9]=1
matriz_add[10,11]=1
matriz_add[11,5]=1
matriz_add[11,9]=1
matriz_add[11,10]=1
matriz_add[12,1]=1
matriz_add[12,2]=1
matriz_add[12,15]=1
matriz_add[13,14]=1
matriz_add[13,16]=1
matriz_add[13,26]=1
matriz_add[13,27]=1
matriz_add[14,0]=1
matriz_add[14,7]=1
matriz_add[14,13]=1
matriz_add[15,12]=1
matriz_add[15,16]=1
matriz_add[15,28]=1
matriz_add[16,0]=1
matriz_add[16,1]=1
matriz_add[16,13]=1
matriz_add[16,15]=1
matriz_add[17,18]=1
matriz_add[18,17]=1
matriz_add[18,19]=1
matriz_add[18,20]=1
matriz_add[19,18]=1
matriz_add[19,21]=1
matriz_add[20,18]=1
matriz_add[20,22]=1
matriz_add[20,23]=1
matriz_add[21,19]=1
matriz_add[21,22]=1
matriz_add[21,25]=1
matriz_add[21,26]=1
matriz_add[22,20]=1
matriz_add[22,21]=1
matriz_add[22,23]=1
matriz_add[22,24]=1
matriz_add[23,20]=1
matriz_add[23,22]=1
matriz_add[23,24]=1
matriz_add[23,29]=1
matriz_add[24,22]=1
matriz_add[24,23]=1
matriz_add[24,25]=1
matriz_add[25,21]=1
matriz_add[25,24]=1
matriz_add[25,26]=1
matriz_add[25,28]=1
matriz_add[25,29]=1
matriz_add[26,13]=1
matriz_add[26,21]=1
matriz_add[26,25]=1
matriz_add[26,27]=1
matriz_add[27,13]=1
matriz_add[27,26]=1
matriz_add[28,15]=1
matriz_add[28,25]=1
matriz_add[29,23]=1
matriz_add[29,25]=1

matriz_ad =np.zeros((N,N), dtype=int)

#matriz adyacencia
matriz_ad[0,1]=1
matriz_ad[0,2]=1
matriz_ad[0,4]=1
matriz_ad[0,5]=1
matriz_ad[0,6]=1
matriz_ad[0,7]=1
matriz_ad[0,14]=1
matriz_ad[0,16]=1

matriz_ad[1,0]=1
matriz_ad[1,2]=1
matriz_ad[1,12]=1
matriz_ad[1,16]=1

matriz_ad[2,0]=1
matriz_ad[2,1]=1
matriz_ad[2,12]=1

matriz_ad[3,4]=1
matriz_ad[3,6]=1

matriz_ad[4,0]=1
matriz_ad[4,2]=1
matriz_ad[4,3]=1

matriz_ad[5,0]=1
matriz_ad[5,6]=1
matriz_ad[5,11]=1

matriz_ad[6,0]=1
matriz_ad[6,3]=1
matriz_ad[6,5]=1
matriz_ad[6,0]=1

matriz_ad[7,0]=1
matriz_ad[7,8]=1
matriz_ad[7,14]=1

matriz_ad[8,7]=1
matriz_ad[8,9]=1
matriz_ad[8,10]=1

matriz_ad[9,8]=1
matriz_ad[9,10]=1
matriz_ad[9,11]=1

matriz_ad[10,8]=1
matriz_ad[10,9]=1
matriz_ad[10,11]=1
matriz_ad[11,5]=1
matriz_ad[11,9]=1
matriz_ad[11,10]=1
matriz_ad[12,1]=1
matriz_ad[12,2]=1
matriz_ad[12,15]=1
matriz_ad[13,14]=1
matriz_ad[13,16]=1
matriz_ad[13,26]=1
matriz_ad[13,27]=1
matriz_ad[14,0]=1
matriz_ad[14,7]=1
matriz_ad[14,13]=1
matriz_ad[15,12]=1
matriz_ad[15,16]=1
matriz_ad[15,28]=1
matriz_ad[16,0]=1
matriz_ad[16,1]=1
matriz_ad[16,13]=1
matriz_ad[16,15]=1
matriz_ad[17,18]=1
matriz_ad[18,17]=1
matriz_ad[18,19]=1
matriz_ad[18,20]=1
matriz_ad[19,18]=1
matriz_ad[19,21]=1
matriz_ad[20,18]=1
matriz_ad[20,22]=1
matriz_ad[20,23]=1
matriz_ad[21,19]=1
matriz_ad[21,22]=1
matriz_ad[21,25]=1
matriz_ad[21,26]=1
matriz_ad[22,20]=1
matriz_ad[22,21]=1
matriz_ad[22,23]=1
matriz_ad[22,24]=1
matriz_ad[23,20]=1
matriz_ad[23,22]=1
matriz_ad[23,24]=1
matriz_ad[23,29]=1
matriz_ad[24,22]=1
matriz_ad[24,23]=1
matriz_ad[24,25]=1
matriz_ad[25,21]=1
matriz_ad[25,24]=1
matriz_ad[25,26]=1
matriz_ad[25,28]=1
matriz_ad[25,29]=1
matriz_ad[26,13]=1
matriz_ad[26,21]=1
matriz_ad[26,25]=1
matriz_ad[26,27]=1
matriz_ad[27,13]=1
matriz_ad[27,26]=1
matriz_ad[28,15]=1
matriz_ad[28,25]=1
matriz_ad[29,23]=1
matriz_ad[29,25]=1



print('Matriz de adyacencia')
print(matriz_ad)

matrizc=matriz_ad
#Algoritmo
'''
Repetir con K desde 1 hasta N
    Repetir con I desde 1 hasta N
        Repetir con J desde 1 hasta N
            Si ( M[I,J] = 0 ) entonces
                M[I,J] ← M[I,K] && M[K,J]
            Fin Si
        Fin Repetir
    Fin Repetir
Fin Repetir
'''

#implementacion del algoritmo de warshall

for k in  range(N):
    for i in range(N):
        for j in range(N):
            if matrizc[i,j]==0:
                matrizc[i,j]=matrizc[i,k] and matrizc[k,j]

print('la matriz C es :')
print(matrizc)

#algoritmo de floyd
matriz_floyd = np.array([
[0,   16,  23,  999, 28,  11,  24,  15,  999, 999, 999, 999, 999, 999, 16,  999, 24,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[16,  0,   11,  999, 999, 999, 999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 22,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[23,  11,  0,   999, 20,  999, 999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 0,   25,  999, 22,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[28,  999, 20,  25,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[11,  999, 999, 999, 999, 0,   22,  999, 999, 999, 999, 23,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[24,  999, 999, 22,  999, 22,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[15,  999, 999, 999, 999, 999, 999, 0,   14,  999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 14,  0,   6.8, 15,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 6.8, 0,   13,  28,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 15,  13,  0,   16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 23,  999, 999, 999, 28,  16,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   999, 999, 23,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   12,  999, 13 , 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  18,  999, 999],
[24,  999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 12,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 23,  999, 999, 0,   8.8, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 47,  999],
[24,  22,  16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  999, 8.8, 0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   17,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 17,  0,   49,  66,  999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 49,  0,   999, 8.6, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 66,  999, 0,   999, 23,  50,  999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 8.6, 999, 0,   10,  999, 999, 25,  46,  999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 23,  10,  0,   46,  34,  999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 50,  999, 46,  0,   38,  999, 999, 999, 999, 15],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 34,  38,  0,   16,  999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 25,  999, 999, 16,  0,   27,  999, 28,  51.8],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  999, 999, 999, 999, 999, 999, 999, 46,  999, 999, 999, 27,  0,   9.8, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 18,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 9.8, 0,   999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 47,  999, 999, 999, 999, 999, 999, 999, 999, 999, 28,  999, 999, 0,   999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 15,  999, 51.8,999, 999, 999, 0]
])

print('Matriz de Costos/Distancias')
print(matriz_floyd)



#Algoritmo Floyd
'''
Repetir con K desde 1 hasta N
    Repetir con I desde 1 hasta N
        Repetir con J desde 1 hasta N
            Si ( M[I,K] + M[K,J]  < M[I,J] ) entonces
                M[I,J] ← M[I,K] + M[K,J]
            Fin Si
        Fin Repetir
    Fin Repetir
Fin Repetir
'''
#implementacion del algoritmo de floyd
for k in range(N):
    for i in range(N):
        for j in range(N):
            if (matriz_floyd[i,k] + matriz_floyd[k,j]) < matriz_floyd[i,j]:
                matriz_floyd[i,j] = matriz_floyd[i,k]+matriz_floyd[k,j]

print('Matriz Caminos Minimos:')
print(matriz_floyd)


# algoritmo Floyd Guarda Vértices



matriz = np.array([
[0,   16,  23,  999, 28,  11,  24,  15,  999, 999, 999, 999, 999, 999, 16,  999, 24,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[16,  0,   11,  999, 999, 999, 999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 22,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[23,  11,  0,   999, 20,  999, 999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 0,   25,  999, 22,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[28,  999, 20,  25,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[11,  999, 999, 999, 999, 0,   22,  999, 999, 999, 999, 23,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[24,  999, 999, 22,  999, 22,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[15,  999, 999, 999, 999, 999, 999, 0,   14,  999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 14,  0,   6.8, 15,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 6.8, 0,   13,  28,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 15,  13,  0,   16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 23,  999, 999, 999, 28,  16,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   999, 999, 23,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   12,  999, 13 , 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  18,  999, 999],
[24,  999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 12,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 23,  999, 999, 0,   8.8, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 47,  999],
[24,  22,  16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  999, 8.8, 0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   17,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 17,  0,   49,  66,  999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 49,  0,   999, 8.6, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 66,  999, 0,   999, 23,  50,  999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 8.6, 999, 0,   10,  999, 999, 25,  46,  999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 23,  10,  0,   46,  34,  999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 50,  999, 46,  0,   38,  999, 999, 999, 999, 15],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 34,  38,  0,   16,  999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 25,  999, 999, 16,  0,   27,  999, 28,  51.8],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  999, 999, 999, 999, 999, 999, 999, 46,  999, 999, 999, 27,  0,   9.8, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 18,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 9.8, 0,   999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 47,  999, 999, 999, 999, 999, 999, 999, 999, 999, 28,  999, 999, 0,   999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 15,  999, 51.8,999, 999, 999, 0]
                  ])
matrizz=np.array([
[0,   16,  23,  999, 28,  11,  24,  15,  999, 999, 999, 999, 999, 999, 16,  999, 24,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[16,  0,   11,  999, 999, 999, 999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 22,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[23,  11,  0,   999, 20,  999, 999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 0,   25,  999, 22,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[28,  999, 20,  25,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[11,  999, 999, 999, 999, 0,   22,  999, 999, 999, 999, 23,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[24,  999, 999, 22,  999, 22,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[15,  999, 999, 999, 999, 999, 999, 0,   14,  999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 14,  0,   6.8, 15,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 6.8, 0,   13,  28,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 15,  13,  0,   16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 23,  999, 999, 999, 28,  16,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   999, 999, 23,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   12,  999, 13 , 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  18,  999, 999],
[24,  999, 999, 999, 999, 999, 999, 16,  999, 999, 999, 999, 999, 12,  0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 23,  999, 999, 0,   8.8, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 47,  999],
[24,  22,  16,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  999, 8.8, 0,   999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 0,   17,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 17,  0,   49,  66,  999, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 49,  0,   999, 8.6, 999, 999, 999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 66,  999, 0,   999, 23,  50,  999, 999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 8.6, 999, 0,   10,  999, 999, 25,  46,  999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 23,  10,  0,   46,  34,  999, 999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 50,  999, 46,  0,   38,  999, 999, 999, 999, 15],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 34,  38,  0,   16,  999, 999, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 25,  999, 999, 16,  0,   27,  999, 28,  51.8],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 13,  999, 999, 999, 999, 999, 999, 999, 46,  999, 999, 999, 27,  0,   9.8, 999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 18,  999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 9.8, 0,   999, 999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 47,  999, 999, 999, 999, 999, 999, 999, 999, 999, 28,  999, 999, 0,   999],
[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 15,  999, 51.8,999, 999, 999, 0]
                  ])

print('Matriz de Costos/Distancias')
print(matriz)

'''
Repetir con K desde 1 hasta N
    Repetir con I desde 1 hasta N
        Repetir con J desde 1 hasta N
            Si ( M[I,K] + M[K,J]  < M[I,J] ) entonces
                M[I,J] ← M[I,K] + M[K,J]
            Fin Si
        Fin Repetir
    Fin Repetir
Fin Repetir
'''
#declaramos e inicializamos matriz t
matrizT = np.zeros( (N,N),dtype=int)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if (matriz[i,k] + matriz[k,j]) < matriz[i,j]:
                matriz[i,j] = matriz[i,k]+matriz[k,j]
                matrizT[i,j] = k   #agregamos matriz t al algoritmo de floyd

print('Matriz T:')
print(matrizT)



#fin de calculos de matrices


def ver_matriz_c():
    try:
        _valor1 = int(entrada_texto.get())
        _valor2 = int(entrada2_texto.get())
        _valor =matrizc[ _valor1][_valor2]
        r.set(_valor)
        _valor =matriz_floyd[ _valor1][_valor2]
        s.set(_valor)
        _valor =matrizT[ _valor1][_valor2]
        t.set(_valor)

    except ValueError:
        etiqueta3.config(text="Introduce un numero")


def verad():
    app=Tk()
    app.title("matriz de adyacencia")
    vpp=Frame(app)
    vpp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
    vpp.columnconfigure(0,weight=1)
    vpp.rowconfigure(0,weight=1)
    etiqueta3= Label(vpp, text=matriz_add)
    etiqueta3.grid(column=1,row=3,sticky=W+E)

    app.mainloop()


def verc():
    app=Tk()
    app.title("matriz c")
    vpp=Frame(app)
    vpp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
    vpp.columnconfigure(0,weight=1)
    vpp.rowconfigure(0,weight=1)

    etiqueta3= Label(vpp, text=matrizc)
    etiqueta3.grid(column=1,row=3,sticky=W+E)
    app.mainloop()

def veradis():
    app=Tk()
    app.title("matriz de adyacencia")

    for r in range(30):
        for c in range(30):
            a=matrizz[r][c]
            cell = Entry(app, width=5)
            cell.grid(row=r, column=c)
            cell.insert(0,'{}'.format(a))


    app.mainloop()



def vercam():
    app=Tk()
    app.title("matriz Camino Minimos")
    for r in range(30):
        for c in range(30):
            a=matriz_floyd[r][c]
            cell = Entry(app, width=5)
            cell.grid(row=r, column=c)
            cell.insert(0,'{}'.format(a))

    app.mainloop()


def vert():
    app=Tk()
    app.title("matriz de adyacencia")

    for r in range(30):
        for c in range(30):
            a=matrizT[r][c]
            cell = Entry(app, width=5)
            cell.grid(row=r, column=c)
            cell.insert(0,'{}'.format(a))


    app.mainloop()



app=Tk()
app.title("proyecto python")

vp=Frame(app)
vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)


# BOTONES
boton=Button(vp,text=" MATRIZ ADYACENCIA",command=verad)
boton.grid(column=1,row=1,sticky=W+E)

boton1=Button(vp,text=" MATRIZ C",command=verc)
boton1.grid(column=2,row=1,sticky=W+E)

boton2=Button(vp,text=" MATRIZ DISTANCIAS",command=veradis)
boton2.grid(column=3,row=1,sticky=W+E)

boton3=Button(vp,text=" MATRIZ CAMINOS MINIMOS",command=vercam)
boton3.grid(column=4,row=1,sticky=W+E)

boton4=Button(vp,text=" MATRIZ T",command=vert)
boton4.grid(column=5,row=1,sticky=W+E)

#LABEL Y AREA DE INGRESION DE TEXTO



etiqueta=Label(vp,text="DEPARTAMENTO a :")
etiqueta.grid(column=1,row=3,sticky=W+E)

etiqueta=Label(vp,text="DEPARTAMENTO b :")
etiqueta.grid(column=3,row=3,sticky=W+E)



valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=3)
valor2 = ""
entrada2_texto = Entry(vp, width=10, textvariable=valor2)
entrada2_texto.grid(column=4, row=3)


boton=Button(vp,text=" CALCULAR", command=ver_matriz_c )
boton.grid(column=5,row=3,sticky=W+E)

r = StringVar()
s = StringVar()
t = StringVar()
etiqueta3= Label(vp, text="EXISTE CAMINO ENTRE AMBOS DEP. :")
etiqueta3.grid(column=1, row=18, sticky=W+E)

resultado_texto = Entry(vp,justify="center", width=10, textvariable=r,foreground="red",state="disabled")
resultado_texto.grid(column=2, row=18)


etiqueta4= Label(vp, text="Longitud del camino más corto")
etiqueta4.grid(column=1, row=19, sticky=W+E)
resultado_texto = Entry(vp,justify="center", width=10, textvariable=s,state="disabled")
resultado_texto.grid(column=2, row=19)

etiqueta5= Label(vp, text=" nodo intermedio para llegar del origen al destino")
etiqueta5.grid(column=1, row=20, sticky=(W+E))
resultado_texto = Entry(vp,justify="center", width=10, textvariable=t,state="disabled")
resultado_texto.grid(column=2, row=20)




#AREA DE DEPARTAMENTOS
etiqueta=Label(vp,text=" ")
etiqueta.grid(column=1,row=5)
etiqueta=Label(vp,text=" DEPARTAMENTO DE GUATEMA")
etiqueta.grid(column=1,row=6)

etiqueta=Label(vp,text="0) GUATEMALA  ")
etiqueta.grid(column=1,row=7,sticky=W+E)
etiqueta=Label(vp,text="1) SANTA CATARINA  ")
etiqueta.grid(column=2,row=7,sticky=W+E)
etiqueta=Label(vp,text="2) SAN JOSE PINULA ")
etiqueta.grid(column=3,row=7,sticky=W+E)
etiqueta=Label(vp,text="3) SAN JOSE DEL GOLFO  ")
etiqueta.grid(column=4,row=7,sticky=W+E)

etiqueta=Label(vp,text="4) PALENCIA  ")
etiqueta.grid(column=1,row=8,sticky=W+E)
etiqueta=Label(vp,text="5) CHINAUTLA  ")
etiqueta.grid(column=2,row=8,sticky=W+E)
etiqueta=Label(vp,text="6) SAN PEDRO AYAMPUC ")
etiqueta.grid(column=3,row=8,sticky=W+E)
etiqueta=Label(vp,text="7) MIXCO  ")
etiqueta.grid(column=4,row=8,sticky=W+E)

etiqueta=Label(vp,text="8) SAN PEDRO SAC  ")
etiqueta.grid(column=1,row=9,sticky=W+E)
etiqueta=Label(vp,text="9) SAN JUAN  ")
etiqueta.grid(column=2,row=9,sticky=W+E)
etiqueta=Label(vp,text="10) SAN RAYMUNDO ")
etiqueta.grid(column=3,row=9,sticky=W+E)
etiqueta=Label(vp,text="11) CHUARRANCHO  ")
etiqueta.grid(column=4,row=9,sticky=W+E)

etiqueta=Label(vp,text="12) FRAIJANES  ")
etiqueta.grid(column=1,row=10,sticky=W+E)
etiqueta=Label(vp,text="13) AMATITLAN  ")
etiqueta.grid(column=2,row=10,sticky=W+E)
etiqueta=Label(vp,text="14) VILLA NUEVA ")
etiqueta.grid(column=3,row=10,sticky=W+E)
etiqueta=Label(vp,text="15) VILLA CANLES  ")
etiqueta.grid(column=4,row=10,sticky=W+E)

etiqueta=Label(vp,text="16) PETAPA ")
etiqueta.grid(column=1,row=11,sticky=W+E)


etiqueta=Label(vp,text=" ")
etiqueta.grid(column=1,row=12)
etiqueta=Label(vp,text=" DEPARTAMENTO DE ESCUINTLA")
etiqueta.grid(column=1,row=13)

etiqueta=Label(vp,text="17) TIQUISATE  ")
etiqueta.grid(column=1,row=14,sticky=W+E)
etiqueta=Label(vp,text="18) NUEVA CONCEPCION ")
etiqueta.grid(column=2,row=14,sticky=W+E)
etiqueta=Label(vp,text="19) SANTA LUCIA ")
etiqueta.grid(column=3,row=14,sticky=W+E)
etiqueta=Label(vp,text="20) LA GOMERA ")
etiqueta.grid(column=4,row=14,sticky=W+E)

etiqueta=Label(vp,text="21) SIQUINALA  ")
etiqueta.grid(column=1,row=15,sticky=W+E)
etiqueta=Label(vp,text="22) LA DEMOCRACIA ")
etiqueta.grid(column=2,row=15,sticky=W+E)
etiqueta=Label(vp,text="23) SAN JOSE ")
etiqueta.grid(column=3,row=15,sticky=W+E)
etiqueta=Label(vp,text="24) MANAGUA ")
etiqueta.grid(column=4,row=15,sticky=W+E)

etiqueta=Label(vp,text="25) ESCUINTLA  ")
etiqueta.grid(column=1,row=16,sticky=W+E)
etiqueta=Label(vp,text="26) PALIN ")
etiqueta.grid(column=2,row=16,sticky=W+E)
etiqueta=Label(vp,text="27) SAN VICENTE ")
etiqueta.grid(column=3,row=16,sticky=W+E)
etiqueta=Label(vp,text="28) GUANAGAZAPA ")
etiqueta.grid(column=4,row=16,sticky=W+E)

etiqueta=Label(vp,text="29) IZTAPA ")
etiqueta.grid(column=4,row=17,sticky=W+E)


app.mainloop()
