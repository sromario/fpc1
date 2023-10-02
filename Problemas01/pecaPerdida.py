"""Juvenal adora quebra-cabeças, essa é sua brincadeira favorita. O grande problema, porém, é que às vezes o jogo vem com uma peça faltando. Isso irrita bastante o pobre menino, que tem de descobrir qual peça está faltando e solicitar uma peça de reposição ao fabricante do jogo. Sabendo que o quebra-cabeças tem N peças, numeradas de 1 a N e que exatamente uma está faltando, ajude Juvenal a saber qual peça ele tem de pedir.

Tarefa Escreva um programa que, dado um inteiro N e N - 1 inteiros numerados de 1 a N, descubra qual inteiro está faltando.

Entrada A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A entrada contém 2 linhas. A primeira linha contém um inteiro N (2 ≤ N ≤ 1.000). A segunda linha contém N - 1 inteiros numerados de 1 a N (sem repetições).

Saída Seu programa deve imprimir, na saída padrão, uma única linha, contendo o número que está faltando na sequência dada."""

def achar(n,lista_completa,lista_incompleta):
    somaList1 = 0
    somaList2 = 0
    for i in lista_incompleta:
        somaList1= somaList1+i
        continue
     
    for i in lista_completa:
        somaList2 = somaList2+i
        continue
    
    print(  somaList2 - somaList1 )




if __name__== "__main__":
    n = int(input())
    lista_incompleta = [int(x) for x in (input().split())]
    lista_completa = [int(x) for x in range(1, n + 1)]
    achar(n,lista_completa,lista_incompleta)