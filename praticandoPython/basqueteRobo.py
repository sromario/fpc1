"""A organização da OIBR, Olimpíada Internacional de
Basquete de Robô, está começando a ter problemas
com dois times: os Bit Warriors e os Byte Bulls. É

que os robôs desses times acertam quase todos os lan-
çamentos, de qualquer posição na quadra! Pensando

bem, o jogo de basquete ficaria mesmo sem graça se
jogadores conseguissem acertar qualquer lançamento,

não é mesmo? Uma das medidas que a OIBR está im-
plantando é uma nova pontuação para os lançamentos,

de acordo com a distância do robô para o início da qua-
dra. A quadra tem 2000 centímetros de comprimento,

como na figura. 0 800 1400 2000
1 pt 2 pts 3 pts

Dada a distância D do robô até o início da quadra, onde está a cesta, a regra é a seguinte:
• Se D ≤ 800, a cesta vale 1 ponto;
• Se 800 < D ≤ 1400, a cesta vale 2 pontos;
• Se 1400 < D ≤ 2000, a cesta vale 3 pontos.
A organização da OIBR precisa de ajuda para automatizar o placar do jogo. Dado o valor da
distância D, você deve escrever um programa para calcular o número de pontos do lançamento.
Entrada
A primeira e única linha da entrada contém um inteiro D indicando a distância do robô para o
início da quadra, em centímetros, no momento do lançamento.
Saída
Seu programa deve produzir uma única linha, contendo um inteiro, 1, 2 ou 3, indicando a pontuação
do lançamento."""


def quadra(robo):
    pontos = 0

    if robo <= 800:
        pontos = 1
        return pontos
    elif  800 < robo <=1400: 
        pontos = 2
        return pontos
    elif 1400 < robo <= 2000:
        pontos = 3
        return pontos
        
    

if __name__ == "__main__":
    robo = int(input())
    quadra(robo)
    print(quadra(robo))