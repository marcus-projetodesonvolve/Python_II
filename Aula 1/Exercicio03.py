def soma_recursiva(n):
    # Caso base: se n for 1, a soma é 1
    if n <= 1:
        return n
    # Passo recursivo: n + soma do anterior
    return n + soma_recursiva(n - 1)

# Exemplo: soma_recursiva(5) -> 15 (5+4+3+2+1)