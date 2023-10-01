#Hacer un rompecabezas armable moviendo el cero 
from random import *
fila = 4
columna = 4
def imprimat(matriz):
    for fila in matriz:
        print(fila)
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 0]]
mat2 = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 0]]
def mover_der(mat, fil, col):
    mat[fil][col], mat[fil][col + 1] = mat[fil][col + 1], mat[fil][col]
def mover_izq(mat, fil, col):
    mat[fil][col], mat[fil][col - 1] = mat[fil][col - 1], mat[fil][col]
def mover_arriba(mat, fil, col):
    mat[fil][col], mat[fil - 1][col] = mat[fil - 1][col], mat[fil][col]
def mover_abajo(mat, fil, col):
    mat[fil][col], mat[fil + 1][col] = mat[fil + 1][col], mat[fil][col]
def buscar_cero(mat, fila, columna):
    for fil in range(fila):
        for col in range(columna):
            if mat[fil][col] == 0:
                return fil, col
def mezclar(mat, fila, columna, n):
    fil, col= buscar_cero(mat, fila, columna)
    i = 0
    while i < n:
        jugada = randint(1, 4)
        if jugada == 1 and col < columna - 1:  
            mover_der(mat, fil, col)
            i += 1
        elif jugada == 2 and col > 0:  
            mover_izq(mat, fil, col)
            col -= 1
            i += 1
        elif jugada == 3 and fil < fila - 1:  
            mover_abajo(mat, fil, col)
            fil += 1
            i += 1
        elif jugada == 4 and fil > 0:  
            mover_arriba(mat, fil, col)
            fil -= 1
            i += 1
    imprimat(mat)
def gano(mat,mat2,fila,columna):
    c=0
    for fil in range(fila):
        for col in range(columna):
            if mat[fil][col]==mat2[fil][col]:
                c+=1
                if c==15:
                    return True
def jugar(mat):
    fil, col= buscar_cero(mat, fila, columna)
    while True:  
        mov = input("Presione una de las teclas o salir para salir: w a s d: ") 
        if mov == "w":
            if fil > 0:
                mover_arriba(mat, fil, col)
                fil -= 1
                imprimat(mat)
                if gano(mat, mat2, fila, columna):
                    print("Usted ha finalizado el juego :) FELICIDADES!!!")
                    break
            else:
                print("No puedes mover hacia arriba desde aquí.")
        elif mov == "a":
            if col > 0:
                mover_izq(mat, fil, col)
                col -= 1
                imprimat(mat)
                if gano(mat, mat2, fila, columna):
                    print("Usted ha finalizado el juego :) FELICIDADES!!!")
                    break
            else:
                print("No puedes mover hacia la izquierda desde aquí.")
        elif mov == "s":
            if fil < fila - 1:
                mover_abajo(mat, fil, col)
                fil += 1
                imprimat(mat)
                if gano(mat, mat2, fila, columna):
                    print("Usted ha finalizado el juego :) FELICIDADES!!!")
                    break
            else:
                print("No puedes mover hacia abajo desde aquí.")
        elif mov == "d":
            if col < columna - 1:
                mover_der(mat, fil, col)
                col += 1
                imprimat(mat)
                if gano(mat, mat2, fila, columna):
                    print("Usted ha finalizado el juego :) FELICIDADES!!!")
                    break
            else:
                print("No puedes mover hacia la derecha desde aquí.")
        elif mov.lower() == "salir":
            print("Usted ha salido del juego :( vuelve a intentarlo luego :'(")
            return 0
        else:
            print("Entrada no válida. Intenta nuevamente.")
print("Matriz inicial")
imprimat(mat)
print()
n=int(input("Ingrese cant de veces a mezclar: "))
mezclar(mat, fila, columna, n)
jugar(mat)