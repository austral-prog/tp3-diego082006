def slice_simple(texto):
    resultado = texto[4::2]  
    return resultado

def main():
    texto = input("Ingrese un texto: ") 
    print(slice_simple(texto))

main()
