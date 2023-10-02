def album(n,m):

  for i in range(m):
    x = int(input())
    if x in tamanho:
      tamanho.remove(x)
    else:
      pass
  return len(tamanho)

if __name__ == "__main__":
  n = int(input())
  m = int(input())
  tamanho = list(range(1,n+1))  
  c = album(n,m)
  print(c)
