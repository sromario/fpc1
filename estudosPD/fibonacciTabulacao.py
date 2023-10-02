def fib(n):
    if n <= 1:
        return n
    
    #criar tabela para armazenar resultados
    dp = [0] * (n + 1)

    #inicia caso base
    dp[0] = 0
    dp[1] = 1

    #preencher tabela de forma iterativa
    for i in range(2, n + 1):
       dp[i] = dp[i - 1] + dp[i - 2]


    #solução em dp[n]
    return dp[n]


#exemplo de uso
n = 10
resultado = fib(n)
print(resultado)
