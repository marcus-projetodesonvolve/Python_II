def imprimir_intervalo(a, b):
    if a > b:
        print("Valores invalidos")
        return
    
    # Caso base
    if a == b:
        print(a)
    else:
        # Passo recursivo
        print(a, end=" ")
        imprimir_intervalo(a + 1, b)

# Exemplo: imprimir_intervalo(1, 10) -> 1 2 3 4 5 6 7 8 9 10