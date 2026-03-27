def decimal_para_binario(n):
    # Caso base: quando o quociente chega a 0
    if n == 0:
        return ""
    
    # Passo recursivo: 
    # Primeiro chamamos a função com o quociente (n // 2)
    # Depois concatenamos o resto (n % 2) no final da string
    return decimal_para_binario(n // 2) + str(n % 2)

# Exemplo: decimal_para_binario(13) -> "1101"