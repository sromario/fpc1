N = int(input())
instantes = []

for i in range(N):
  instante = int(input())
  instantes.append(instante)

T_total = 0

for i in range(N):
  if i==0:
     T_total += 10

  else:
    T_decorrido = instantes[i] - instantes[i - 1]
    
  
    if T_decorrido <= 10:
        T_total += T_decorrido

    else:
      T_total += 10
    
print(T_total)

