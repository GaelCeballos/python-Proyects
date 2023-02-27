import random as ra
import math as mt


def tabla_de_divisores(number):
    """Es una tabla para sacar los limites de los divisores"""
    lista_de_divison = []
    lista_de_frecuencia = []
    lista_de_frecuencia_absoluta= []
    division = 100/number
    lista_de_randoms = []
    contador=0
    for p in range(1,number):
        lista_de_divison.append(int(division * p))
        numero_random = ra.randint(0,100)
        lista_de_randoms.append(numero_random)
    print(lista_de_divison)
    for e in lista_de_divison:
        contador = 0
        for f in lista_de_randoms:
            if lista_de_divison(e)< lista_de_randoms <= lista_de_divison(e + 1):
                contador += 1
        print("La cantidad de numeros entre {} es: {}".format(lista_de_divison(e), contador))

  

def desciones(num):
    lista_de_divisor = []
    lista_de_frecuencia = []
    lista_de_frecuencia_absoluta= []
    if 100 % num  == 0 :
        division = 100/num
        print("hola")
        for i in range (0,100):
            numero_ran=ra.randint(0,100)            
    else:
        print("Error no es un divisor par y no se puede realizar") 

def main():
    numer = int(input("Proporciona la cantidad de divisones que tenga\n"))
    desciones(numer)
    tabla_de_divisores(numer)

if __name__ == '__main__':
    main()