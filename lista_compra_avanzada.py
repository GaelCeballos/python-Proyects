SALIDA = "SALIR"
Archivo_lista = "Lista de las compras.txt"

def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir]".format(SALIDA))


def Guardar_lista(lista_de_compra):
    with open(Archivo_lista,"w") as mi_archivo:
        mi_archivo.write("\n".join(lista_de_compra))
    
def guardar_item_en_lista(lista_de_compra,item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_de_compra]:
        print("Este producto ya esta agregado")
    else:
        lista_de_compra.append(item_a_guardar)

def main():
    lista_de_compra = []
    if input("Quieres cargar la ultima lista de la compra? [S/N]") == "S":
        try:
            with open(Archivo_lista, "r") as a:
                lista_de_compra = a.read().split("\n")
                print("\n".join(lista_de_compra))
        except FileNotFoundError :
            print("¡Archivo de la compra no encontrado!")

    intput_usuario = preguntar_producto_usuario()
    while intput_usuario != SALIDA:
        guardar_item_en_lista(lista_de_compra , intput_usuario)
        print("\n".join(lista_de_compra))
        intput_usuario = preguntar_producto_usuario()
        
    Guardar_lista(lista_de_compra)
    
    

if __name__ == '__main__':
    main()
