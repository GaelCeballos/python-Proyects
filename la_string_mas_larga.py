from colorama import init , Fore , Back , Style
import time

salida_de_sistema = "SALIR"

def pedir_texto():
    return input("Introduce una oración [{}] para salir ".format(salida_de_sistema))


def guardar_string_en_lista(lista_de_strings ,texto_a_guardar):
    if texto_a_guardar.lower() in [a.lower() for a in lista_de_strings]:
        print("Este texto ya existe ingresa otro")
    else:
        lista_de_strings.append(texto_a_guardar)

def saber_la_string_mas_larga(lista_de_strings):
    string_mas_larga = max(lista_de_strings , key=len)
    return string_mas_larga

def colorear_string(string):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    init(autoreset=True)
    colored_string = ""
    for i, char in enumerate(string):
        color = colors[i % len(colors)]
        colored_string += color + char
    return colored_string


def main():
    lista_de_strings = []
    input_de_usuario = pedir_texto()
    while input_de_usuario != salida_de_sistema:
        guardar_string_en_lista(lista_de_strings , input_de_usuario)
        print("\n".join(lista_de_strings))
        input_de_usuario = pedir_texto()
    texto = saber_la_string_mas_larga(lista_de_strings)
    texto_final = colorear_string(texto)
    print("El texto más largo es : {}".format(texto_final))
     
    
if __name__ == '__main__':
    main()
    