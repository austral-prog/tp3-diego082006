def slice_advanced(texto):
    resultado = texto[4::2] # Obtener el texto a partir del quinto carácter y saltar de a 2 caracteres
    return resultado

def main():
    texto = input("Ingrese un texto: ") # Ingresar un texto usando input
    
    # Imprimir en pantalla el resultado
    print(slice_advanced(texto))
    # Código a implementar utilizando input.

if __name__ == "__main__":
    main()
