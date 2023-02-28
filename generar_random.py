import random as ra
import math as mt

def tabla_de_divisores(number):
    """Es una tabla para sacar los limites de los divisores"""
    lista_de_division = []
    lista_de_frecuencia = []
    lista_de_frecuencia_absoluta = []
    division = 100/number
    lista_de_randoms = []
    contador = 0
    ultimo_elemento = 0
    
    lista_de_division.append(0)
    for p in range(1, number):
        lista_de_division.append(int(division * p))
    lista_de_division.append(100)

    for g in range(0 , 101):
        numero_random = ra.randint(0, 100)
        lista_de_randoms.append(numero_random)
        
    print(lista_de_division)
    
    for e in range(len(lista_de_division)-1):
        contador = 0
            
        for f in lista_de_randoms:
            if lista_de_division[e] <= f < lista_de_division[e+1]:
                contador += 1
                ultimo_elemento +=1

        print("La cantidad de numeros entre {} y {} es: {}".format(lista_de_division[e],lista_de_division[e+1] ,contador))
    

def main():
    numer = int(input("Proporciona la cantidad de divisiones que tenga\n"))
    if numer % 100:
        tabla_de_divisores(numer)
    else:
        print("ERROR........ el {} no se puede dividir".format(numer))
if __name__ == '__main__':
    main()
