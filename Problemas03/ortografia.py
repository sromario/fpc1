def distancia_da_adicao(n, m):
    num_linhas = len(n) + 1
    num_colunas = len(m) + 1

    tab = [[0 for _ in range(num_colunas)] for _ in range(num_linhas)]

    # Preencher linha e coluna, caso base
    for i in range(num_linhas):
        tab[i][0] = i
    for j in range(num_colunas):
        tab[0][j] = j

    # Programação dinâmica
    for i in range(1, num_linhas):
        for j in range(1, num_colunas):
            if n[i - 1] == m[j - 1]:
                tab[i][j] = tab[i - 1][j - 1]
            else:
                tab[i][j] = 1 + min(tab[i - 1][j], tab[i][j - 1], tab[i - 1][j - 1])

    return tab[num_linhas - 1][num_colunas - 1]



def busca_correcoes(dicionario, palavra_usuario):
    correcoes = []

    for palavra_dict in dicionario:
        distancia = distancia_da_adicao(palavra_usuario, palavra_dict)
        if distancia <= 2:
            correcoes.append(palavra_dict)

    return correcoes

# Leitura da entrada
n, m = map(int, input().split())
dicionario = [input() for _ in range(n)]
palavras_usuario = [input() for _ in range(m)]

# Processamento das palavras do usuário
for palavra in palavras_usuario:
    correcoes = busca_correcoes(dicionario, palavra)
    if correcoes:
        print(" ".join(correcoes))
    else:
        print()
