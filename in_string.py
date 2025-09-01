def check_vowels():
    # Código a implementar utilizando input.

    vocales = 'aeiou'
    nombre = nombre.lower()  
    for vocal in vocales:
        print(f"Contiene {vocal}: {vocal in nombre}")

# Verificación de cada una de sus vocales
def main():
    nombre = input("Ingrese un nombre: ")
    verificar_vocales(nombre)

if __name__ == "__main__":
    main()

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
