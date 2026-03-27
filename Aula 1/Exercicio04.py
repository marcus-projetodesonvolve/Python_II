def eh_primo(n, divisor=None):
    if n < 2: return False
    if divisor is None: divisor = n - 1
    
    # Caso base 1: Se o divisor chegou a 1, é primo
    if divisor == 1:
        return True
    # Caso base 2: Se n for divisível pelo divisor, não é primo
    if n % divisor == 0:
        return False
    
    # Passo recursivo: tenta com o próximo divisor abaixo
    return eh_primo(n, divisor - 1)

# Exemplo: eh_primo(7) -> True | eh_primo(10) -> False