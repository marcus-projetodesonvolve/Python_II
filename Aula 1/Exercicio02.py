def imprimir_invertido(a, b):
    if a > b:
        print("Valores invalidos")
        return
    
    if a == b:
        print(a, end=" ")
    else:
        # Mudança: primeiro chama a recursão, depois imprime
        imprimir_invertido(a + 1, b)
        print(a, end=" ")

# Exemplo: imprimir_invertido(1, 10) -> 10 9 8 7 6 5 4 3 2 1