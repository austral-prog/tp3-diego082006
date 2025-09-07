def check_vowels():
    # Ingresar un nombre usando input
    nombre = input("Ingrese un nombre: ")

    # Pasar todo a minúsculas para no diferenciar entre mayúsculas/minúsculas
    nombre = nombre.lower()

    # Lista de vocales a verificar
    vocales = ["a", "e", "i", "o", "u"]

    # Verificar cada vocal y mostrar resultado
    for vocal in vocales:
        print(f"Contiene {vocal}: {vocal in nombre}")

check_vowels()
