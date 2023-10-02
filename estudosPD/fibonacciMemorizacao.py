def fib(n):
    #cria uma tabela para armazenar resultados
    memo = {}

  #função para auxiliar no calculo
    def fib_aux(n):

        #verifica se o resultado já existe na tabela
        if n in memo:
            return memo[n]
    
        #caso base 
        if n <= 0:
            return 0
        elif n == 1:
            return 1
    
        #caso recursivo: calcular fibonacci usando resultados anteriores
        result = fib_aux(n - 1) + fib_aux(n -2)

        #armazenar resultado na tabela
        memo[n] = result

        return result

   #chamando função auxiliar
    return fib_aux(n)



#exemplo de uso
n = 15
resultado = fib(n)
print(resultado)