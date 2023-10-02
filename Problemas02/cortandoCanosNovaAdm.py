
n, t = map(int, input().split())
p = []
v = []

for i in range(n):
    canos = [int(x) for x in input().split()]
    for i in range(t // canos[0]):
      p.append(canos[0])
      v.append(canos[1])

itens = len(p)
capacidade = t

T = [[0 for j in range (capacidade + 1)] for i in range(itens + 1)]
for j in range(1, capacidade+1):
    for i in range(1, itens+1):
        if p[i - 1] > j:
            T[i][j] = T[i - 1][j]
        else:
            T[i][j] = max(T[i - 1][j], T[i - 1][j - p[i - 1]]+v[i-1])
print(T[itens][capacidade])