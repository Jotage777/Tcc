import Banco_de_dados


def analise():
    lista_bots = Banco_de_dados.consultas("SELECT * FROM Bots")
    jogos_AoVivo = Banco_de_dados.consultas("SELECT * FROM Jogos_AoVivo")

    for bot in lista_bots:
        if bot[11] == True and bot[2] <= Banco_de_dados.consultar_usuario_saldo(bot[14]): #se ativado e saldo suficiente
            for jogo in jogos_AoVivo: #percorrer jogos
                var = 0
                if bot[6] >= jogo[6] >= bot[5]: #verificar se o tempo de jogo esta no intervalo do bot
                    if bot[13] == 'favesta': #analisar o time favorito
                        if jogo[12] <= jogo[13] and bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[9]: #1* casa favorito 2* analisar finalizações casa 3* analisar posse casa
                            var = 1
                        elif jogo[13] < jogo[12] and bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[9]: #1* fora favorito 2* analisar finalizações fora 3* analisar posse fora
                            var = 1
                    elif bot[13] == 'zebraesta': #analisar a zebra
                        if jogo[12] >= jogo[13] and bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[9]: #1* casa zebra 2* analisar finalizações casa 3* analisar posse casa
                            var = 1
                        if jogo[13] > jogo[12] and bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[9]: #1* fora zebra 2* analisar finalizações fora 3* analisar posse fora
                            var = 1
                    elif bot[13] == 'casaesta': #analisar o time da casa
                        if bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[9]: #1* analisar finalizações casa 2* analisar posse casa
                            var = 1
                    elif bot[13] == 'foraesta': #analisar o time de fora
                        if bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[9]: #1* analisar finalizações fora 2* analisar posse fora
                            var = 1
                verificar = Banco_de_dados.verificar_apostas(jogo[0],bot[0])
                if var == 1 and verificar == False:
                    if bot[12] == 'favapo': #apostar no favorito
                        if jogo[12] <= jogo[13]: #casa é o favorito
                            if bot[4] >= jogo[12] >= bot[3]: #analizar odd casa
                                print("Apostado em favorito(casa)")
                        else: #fora é o favorito
                            if bot[4] >= jogo[13] >= bot[3]: #analizar odd fora
                                print("Apostado em favorito(fora)")
                    elif bot[12] == 'zebraapo': #apostar na zebra
                        if jogo[12] > jogo[13]: #casa é a zebra
                            if bot[4] >= jogo[12] >= bot[3]: #analizar odd casa
                                print("Apostado em zebra(casa)")
                        else: #fora é a zebra
                            if bot[4] >= jogo[13] >= bot[3]: #analizar odd fora
                                print("Apostado em zebra(fora)")
                    elif bot[12] == 'casaapo': #apostar no time da casa
                        if bot[4] >= jogo[12] >= bot[3]: #analizar odd casa
                            print("Apostado em casa")
                    elif bot[12] == 'foraapo': #apostar no time fora
                        if bot[4] >= jogo[13] >= bot[3]:  #analizar odd fora
                            print("Apostado em fora")
