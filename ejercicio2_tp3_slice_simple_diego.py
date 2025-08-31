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