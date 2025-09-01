# Ejercicio 1
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

# Ejercicio 2
texto = "AWESOME".lower()

# Primeras 3 letras del texto
primeras_tres_letras = texto[:3]
print(primeras_tres_letras)

# Las 3 letras en medio del texto
longitud = len(texto)
mitad = longitud//2
tres_letras_medio = texto[mitad-1:mitad+2]
print(tres_letras_medio)

# De la primera a la cuarta letra y de la antepenúltima hasta la última
primera_a_cuarta = texto[:4]
antepenultima_a_ultima = texto[-3:]
print(primera_a_cuarta + antepenultima_a_ultima)

# Ejercicio 3
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