#divide e ordena
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    #divide array em duas partes
    meio = len(arr) // 2
    esquerda = arr[:meio]
    direita = arr[meio:]

    #chama função merge sort recursivamente para duas metades
    esquerda = mergesort(esquerda)
    direita = mergesort(direita)

    #intercala as duas metades chamando o merg
    return merge(esquerda,direita)


#faz junção das metades já ordenadas em mergesort
def merge(esquerda,direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado



#impressão resultado
minhalista = list(map(int,input().split()))
minhalista = mergesort(minhalista)
print(minhalista)