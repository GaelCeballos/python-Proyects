SALIDA = "SALIR"
lista_final_compra = []
lista_de_compra = ["pan","pollo","pipas"]
mostrar_lista = "m"

def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir] ,[{} para mostras las opciones disponibles]"
                 .format(SALIDA,mostrar_lista))

def guardado():
    a = open("Compra_mostrar_lista.txt","w")
    a.write("\n".join(lista_final_compra))
    a.close

def main():

    input_de_usuario = preguntar_producto_usuario()

    while input_de_usuario != SALIDA:
        if input_de_usuario in lista_de_compra:
            lista_final_compra.append(input_de_usuario)
            input_de_usuario = preguntar_producto_usuario()
            print("\n".join(lista_final_compra))
        elif input_de_usuario == "m":
            print(" Las opciones disponibles son:\n {}".format(lista_de_compra))
            input_de_usuario = preguntar_producto_usuario()
            print("\n".join(lista_final_compra))
        else:
            print("El producto {} no esta disponible para agregar \n".format(input_de_usuario))
            input_de_usuario = preguntar_producto_usuario()
            print("\n".join(lista_final_compra))
    else:
        guardado()


if __name__ == '__main__':
    main()
    