# Índices definidos pela questão
RAIZ_IDX = 0
ESQ_IDX = 1
DIR_IDX = 2

def pre_ordem(arvore):
    # Caso base: se o nó for None ou a lista estiver vazia
    if not arvore:
        return
    
    # 1. Visita a RAIZ
    print(arvore[RAIZ_IDX], end=" ")
    
    # 2. Visita a subárvore ESQUERDA recursivamente
    pre_ordem(arvore[ESQ_IDX])
    
    # 3. Visita a subárvore DIREITA recursivamente
    pre_ordem(arvore[DIR_IDX])

# Exemplo de representação da árvore da imagem:
# [4, [2, [1, None, None], [3, None, None]], [5, None, None]]