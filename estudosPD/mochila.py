#mochila em PD
def gerar_lucros(n, t, pedidos):
  lucros = [[0] * (t + 1) for _ in range(n+1)]

  for i in range(1, n + 1):
    for j in range(1,t + 1):
      if pedidos[i -1][0] > j:
          lucros[i][j] = lucros[i-1][j]
      else:
         lucros[i][j] = max(lucros[i-1][j], lucros[i-1][j - pedidos[i-1][0]] + pedidos[i-1][1])
        
  return lucros[n][t]




n,t = map(int, input().split())
pedidos = []

for _ in range(n):
  comprimento, valor = map(int, input().split())
  pedidos.append((comprimento, valor))
  
maior_lucro = gerar_lucros(n,t,pedidos)

print(maior_lucro)

