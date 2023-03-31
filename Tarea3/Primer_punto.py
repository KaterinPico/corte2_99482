import random as rand
import numpy as np
def Matrices(filas,columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num=rand.randint(1,100) #Ejecuta una matriz aleatoria
            #num=int(input(f'Ingrese el numero de la posicion [{i},{j}]: '))
            matriz[i].append(num)
    return matriz
def Mym():
    Filas=5
    Columnas=10
    Matriz=Matrices(Filas, Columnas)
    mayor = Matriz[0][0]
    menor = Matriz[0][0]
    for fila in Matriz:
        for valor in fila:
            if valor > mayor:
                mayor = valor
            if valor < menor:
                menor = valor
    print("De la matriz: ")
    print(Matriz)
    print(f"El menor es {menor} y el mayor es {mayor}")
    MO= np.array(Matriz)
    print(np.sort(MO))
    
    
if __name__=='__main__':
    Mym()
    





