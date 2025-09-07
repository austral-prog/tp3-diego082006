def test_slice_advanced():
    texto = "Awesome"

    # Pasar todo a minúsculas
    texto = texto.lower()

    # Primeras 3 letras (índices positivos)
    print(texto[0:3])

    # 3 letras del medio (índices positivos)
    medio = len(texto) // 2
    print(texto[medio-1:medio+2])

    # De la primera a la cuarta letra (incluida)
    # y de la antepenúltima hasta la última (incluida)
    print(texto[0:4] + texto[-3:])

test_slice_advanced()
