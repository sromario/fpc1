def descobrir_navio(tabuleiro, i, j, id_navio, n_linhas, n_colunas, tamanho_navio):
    if i < 0 or i >= n_linhas or j < 0 or j >= n_colunas:
        return False
    if tabuleiro[i][j] != "#":
        return False  
    
    # Descobri navio
    tabuleiro[i][j] = id_navio
    if id_navio in tamanho_navio.keys():
        tamanho_navio[id_navio] += 1
    else:
        tamanho_navio[id_navio] = 1

    # Para cima
    descobrir_navio(tabuleiro, i-1, j, id_navio, n_linhas, n_colunas, tamanho_navio)
    
    # Para direita
    descobrir_navio(tabuleiro, i, j+1, id_navio, n_linhas, n_colunas, tamanho_navio)
    
    # Para baixo
    descobrir_navio(tabuleiro, i+1, j, id_navio, n_linhas, n_colunas, tamanho_navio)

    # Para esquerda
    descobrir_navio(tabuleiro, i, j-1, id_navio, n_linhas, n_colunas, tamanho_navio)

    return True

# Entradas (substitua isso pelos seus próprios dados)
n_linhas, n_colunas = [int(x) for x in input().split()]
tabuleiro = [None] * n_linhas
tamanho_navio = {}
id_navio = 0

for i in range(n_linhas):
    tabuleiro[i] = list(input())

n_tiros = int(input())
for tiro in range(n_tiros):
    i, j = [int(i) for i in input().split()] 
    descobriu = descobrir_navio(tabuleiro, i-1, j-1, id_navio, n_linhas, n_colunas, tamanho_navio)
    
    if descobriu:
        tamanho_navio[id_navio] -= 1
        id_navio += 1 

n_destruidos = 0
for id_, tamanho in tamanho_navio.items():
    if tamanho == 0:
        n_destruidos += 1

print(n_destruidos)
