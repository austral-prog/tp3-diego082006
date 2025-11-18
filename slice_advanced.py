def slice_advanced():
    texto = "Awesome"
    texto = texto.lower()
    largo = len(texto)
    medio = largo // 2
    print(texto[0:3])
    print(texto[medio-1:medio+2])
    print(texto[0:4] + texto[-3:])
