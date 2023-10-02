class Baralho:
    def __init__(self, ID, deck=list):
        self.ID = ID
        self.cartas = deck

    def retirar_carta(self):
        del(self.cartas[0])

    def colocar_carta(self):
        temp = self.cartas[0]
        del(self.cartas[0])
        self.cartas.append(temp)
        del(temp)


#########
festas = int(input())
vencedores = []
juvenal = Baralho(0,list)

for i in range(festas):
    id = 1
    jogadores = []
    resposta = str()
    n_de_rodadas = 1
    temos_um_vencedor = False

    deck_inicial = str(input()).split()
    deck_mesa = Baralho(ID=0, deck=deck_inicial)
    
    while '-1' not in resposta:
  
      deck_jogador = str(input()).split()
      jogador = Baralho(id, deck_jogador)
      if '-1' in deck_jogador:
        break

      jogadores.append(jogador)
      id += 1 
      
    #######
    carta_atual = deck_mesa.cartas[0]
    while not temos_um_vencedor or n_de_rodadas <= 1000:
        empatados = []
        for i in range(len(jogadores)):
            jogador_atual = jogadores[i]
            
            if len(jogador_atual.cartas) == 0:
                empatados.append(jogador_atual)
            elif carta_atual == jogador_atual.cartas[0]:
                jogador_atual.retirar_carta()
            else:
                jogador_atual.colocar_carta()

        
        deck_mesa.colocar_carta()
        carta_atual = deck_mesa.cartas[0]
        
        if len(empatados) == 1:
            temos_um_vencedor = True
            vencedores.append(empatados[0])
            break
        if len(empatados) > 1:
            menor = empatados[0]
            for j in range(len(empatados)):
                if empatados[j].ID < menor.ID:
                    menor = empatados[j]
            temos_um_vencedor = True
            vencedores.append(menor)
            break
        elif n_de_rodadas == 1000:
            temos_um_vencedor = True
            vencedores.append(juvenal)
            break

        n_de_rodadas += 1

###########
for vencedor in vencedores:
    print(vencedor.ID)