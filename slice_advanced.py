def slice_advanced():
    texto = "Awesome"
    texto = texto.lower()
    largo = len(texto)
    medio = largo // 2  # Define medio here

    # Primeras 3 letras (awe)
    print(texto[0:3])

    # Las 3 letras en medio (eso)
    print(texto[medio-1:medio+2])

    # De la primera a la cuarta + antepenúltima hasta la última (awesome)
    print(texto[0:4] + texto[-3:])
