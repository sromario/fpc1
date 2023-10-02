"""Os administradores da Fazenda Fartura planejam criar uma nova plantação de morangos, no formato
retangular. Eles têm vários locais possíveis para a nova plantação, com diferentes dimensões de
comprimento e largura. Para os administradores, o melhor local é aquele que tem a maior área.
Eles gostariam de ter um programa de computador que, dadas as dimensões de dois locais, determina
o que tem maior área. Você pode ajudá-los?
Entrada
A entrada contém quatro linhas, cada uma contendo um número inteiro. As duas primeiras linhas
indicam as dimensões (comprimento e largura) de um dos possíveis locais. As duas últimas linhas
indicam as dimensões (comprimento e largura) de um outro possível local para a plantação de
morangos. As dimensões são dadas em metros.
Saída
Seu programa deve escrever uma linha contendo um único inteiro, a área, em metros quadrados, do
melhor local para a plantação, entre os dois locais dados na entrada."""


#calculo da área e escolher melhor
def area(a,b,c,d):
    maior = max(a*b, c*d)
    return  maior 

#chamada da função
if __name__== "__main__":
    
    #ler entradas
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    
    #chamar função e aplicar
    x = area(a,b,c,d)
    
    #printar
    print(x)
        
