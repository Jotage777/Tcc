import Banco_de_dados
def analise():
    lista_bots= Banco_de_dados.consultas("SELECT * FROM Bots")
    jogos_AoVivo = Banco_de_dados.consultas("SELECT * FROM Jogos_AoVivo")

    for bot in lista_bots:
        if bot[11] == True and bot[2] <= Banco_de_dados.consultar_usuario_saldo(bot[14]) :
            for jogo in jogos_AoVivo:
                var = 0
                if bot[6] >= jogo[6] >= bot[5] :
                   if bot[13]=='favesta':
                       if jogo[12]<=jogo[13] and bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[9]:
                            var = 1
                       elif jogo[13] < jogo[12] and bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[9]:
                           var = 1
                   elif bot[13] =='zebraesta':
                       if jogo[12] >= jogo[13] and bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[9]:
                           var = 1
                       if jogo[13] > jogo[12] and bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[9]:
                           var = 1
                   elif bot[13] == 'casaesta':
                       if bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[9]:
                           var = 1
                   elif bot[13] == 'foraesta':
                        if bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[9]:
                            var = 1
                if var==1:
                    if bot[12] == 'favapo':

                       if jogo[12] <= jogo[13]:
                           if bot[4] >= jogo[12] >= bot[3]:
                               print("Apostado em favorito analisado em favorito")
                       else:
                           if bot[4] >= jogo[13] >= bot[3]:
                               print("Apostado em favorito analisado em favorito")
                    elif bot[12] == 'zebraapo':
                       if jogo[12] >= jogo[13]:
                           if bot[4] >= jogo[12] >= bot[3]:
                               print("Apostado em zebra analisado em favorito")
                       else:
                           if bot[4] >= jogo[13] >= bot[3]:
                               print("Apostado em zebra analisado em favorito")
                    elif bot[12] == 'casaapo':
                       if bot[4] >= jogo[12] >= bot[3]:
                           print("Apostado em casa analisado em favorito")
                    elif bot[12] == 'foraapo':
                       if bot[4] >= jogo[13] >= bot[3]:
                           print("Apostado em fora analisado em favorito")