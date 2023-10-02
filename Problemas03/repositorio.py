C,N = map(int,input().split()) #total aplicativos no pc / total disponivel para instalar
dicionario = {} #armazenar programas existentes

#itera sobre c e armazena programas já instalados
for i in range(C):
    pc, vc = map(int,input().split())
    dicionario[pc] = vc


instalar = [] #armazenar a serem instalados
#itera sobre n a serem instalados e compara se é existente ou maior que contido no dicionario
for i in range(N):
    pn, vn = map(int,input().split())

    #compara com dicionario, se melhor adiciona a uma lista instalar
    if pn not in dicionario or vn > dicionario[pc]:
        instalar.append((pn,vn))

#impressão resultados da lista instalar
for i in instalar:
    print(i[0], i[1]) 