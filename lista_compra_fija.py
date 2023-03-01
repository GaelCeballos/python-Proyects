
SALIDA = "SALIR"
lista_final_compra = []

def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir]".format(SALIDA))

def guardado():
    a = open("Compra_definida.txt","w")
    a.write("\n".join(lista_final_compra))
    a.close

def main():

    input_de_usuario = preguntar_producto_usuario()
    lista_de_compra = ["pan","pollo","pipas"]

    print("Las opciones son : {}".format(lista_de_compra))
    while input_de_usuario != SALIDA:
        if input_de_usuario in lista_de_compra:
            lista_final_compra.append(input_de_usuario)
            input_de_usuario = preguntar_producto_usuario()
            print("\n".join(lista_final_compra))
        elif not input_de_usuario in  lista_de_compra:
            print("ERROR, este producto no existe como opción para la lista")
            input_de_usuario = preguntar_producto_usuario()

    guardado()


if __name__ == '__main__':
    main()
    