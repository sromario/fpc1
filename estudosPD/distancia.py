def distancia_da_adicao(nome01,nome02):
    num_linhas = len(nome01) + 1
    num_colunas = len(nome02) + 1


    tab = [[0 for _ in range(num_colunas)] for _ in range(num_linhas)]

    #preencher linha e coluna, caso base
    for i in range(num_linhas):
        tab[i][0] = i
    for j in range(num_colunas):
        tab[0][j] = j

    #distancia
    #programação dinamica
    for i in range(1,num_linhas):
        for j in range(1,num_colunas):
            if nome01[i - 1] == nome02[j - 1]:
                c = 0
            else:
                c = 1

            tab[i][j] = min(tab[i - 1][j - 1] + c, tab[i - 1][j] + 1, tab[i][j-1] + 1)
    return tab[num_linhas - 1][num_colunas - 1]


nome01 = input()
nome02 = input()
print(distancia_da_adicao(nome01,nome02))