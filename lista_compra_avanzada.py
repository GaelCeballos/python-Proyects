SALIDA = "SALIR"

def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir]".format(SALIDA))


def main():
    lista_de_compra = []
    intput_usuario = preguntar_producto_usuario()

    while intput_usuario != SALIDA:
        lista_de_compra.append(intput_usuario)
        print("\n".join(lista_de_compra))
        intput_usuario = preguntar_producto_usuario()
    
    a = open("Compra.txt","w")
    a.write("\n".join(lista_de_compra))
    a.close

if __name__ == '__main__':
    main()
