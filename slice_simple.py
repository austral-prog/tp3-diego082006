def slice_simple():
    # 1. Get input (this is mocked by the test file)
    texto = input("Ingrese un texto: ") 
    
    # 2. Perform the slicing: Start at index 4 (5th character), step by 2
    resultado = texto[4::2]
    
    # 3. Print the result
    print(resultado)
