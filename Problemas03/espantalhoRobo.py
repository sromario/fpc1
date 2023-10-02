N,C,S = [int(x) for x in input().split()] #estações / comandos/ prox.devastada
comandos = list(map(int, input().split()))
cord = [0 for i in range(N)] #fazer cordenada do tamanho n
cord[0] = 1 #ponto inicial

var = 0 #armazena valores
for i in comandos:
  if i== 1:
    var += 1
    cord[var] += 1
  elif i == -1:
    var -= 1
    cord[var] += 1

print(cord[S-1])

