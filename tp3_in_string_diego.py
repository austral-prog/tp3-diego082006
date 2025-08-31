# Ingreso del nombre
def verificar_vocales(nombre):
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