def procesar_texto(texto):
    # Obtener el texto a partir del quinto carácter y saltar de a 2 caracteres
    resultado = texto[4::2]
    return resultado

def main():
    # Ingresar un texto usando input
    texto = input("Ingrese un texto: ")
    
    # Imprimir en pantalla el resultado
    print(procesar_texto(texto))

if __name__ == "__main__":
    main()