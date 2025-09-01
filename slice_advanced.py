def slice_advanced():
    resultado = texto[4::2] # Obtener el texto a partir del quinto carácter y saltar de a 2 caracteres
    return resultado

def main():
    texto = input("Ingrese un texto: ") # Ingresar un texto usando input
    
    # Imprimir en pantalla el resultado
    print(slice_advanced(texto))
    # Código a implementar utilizando input.

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
if __name__ == "__main__":
    main()
