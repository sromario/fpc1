def main():
  n = int(input())
  cubos = [int(x) for x in input().split()]
  total = sum(cubos)
    
  
  total -= (n * (n + 1)) // 2
  
  if total >= 0 and total % n == 0:
      steps = 0
      media = (total // n) + 1
  
  
      for i in cubos:
          if i > media:
            steps = steps + (i - media)
          media = media + 1
      print(steps)
  else:  
    print(-1)
    

if __name__ == '__main__':
   main()
      