#usado para ajustar elementos de modo que raiz seja max ou min
def heapify(arr,n,i):
    maior = i #inicializa com o maior como indice atual
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    #verifica se o filho da esquerda existe e é maior que o pai
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    #verifica se o filho da direita existe e é maior que o pai
    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    #Para um Heap Mínimo (min-heap), inverta as comparações para encontrar o menor elemento.
    #if esquerda < n and arr[esquerda] < arr[menor]:
        #menor = esquerda

    #if direita < n and arr[direita] < arr[menor]:
        #menor = direita"""


    #se o maior nao for o indice atual, troca e continua heapify
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr,n, maior)


#ordena, com heapify assegurado que raiz sempre maior(ou menor) 
def heapsort(arr):
    n = len(arr)

    #constroi uma max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


    #extrai elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] #troca o maximo(raiz) com o último elemento não classificado
        heapify(arr, i, 0) #chama heaapify na heap reduzida



#entrada e ordenação
minhalista = list(map(int, input().split()))
heapsort(minhalista)

#impressão ordenada
print(minhalista)