import Banco_de_dados

def concluir_aposta():
    lista_apostas = list(Banco_de_dados.consultas("SELECT * FROM Apostas"))
    lista_jogos_encerrados = Banco_de_dados.consultas("SELECT * FROM Jogos_Encerrados")
    for aposta in lista_apostas:
        if aposta[5] == 'aberto':
            for jogos in lista_jogos_encerrados:
                if aposta[10] == jogos[0]:
                    if aposta[11]== 1 :
                        if jogos[5] > jogos[4]:
                            id_usuario = Banco_de_dados.consultar_usuario_bots(aposta[12])
                            relatorio = Banco_de_dados.consultar_relatorio(aposta[9])
                            Banco_de_dados.atualizar_relatorio(1, aposta[9], (relatorio[1] + 1))
                            Banco_de_dados.atualizar_relatorio(5, aposta[9], (relatorio[5] - 1))
                            lucro = aposta[4]-aposta[2]
                            Banco_de_dados.atualizar_relatorio(3, aposta[9], (relatorio[3] + lucro))
                            saldo = Banco_de_dados.consultar_usuario_saldo(id_usuario)
                            novo_saldo = saldo + (float(aposta[4]))
                            Banco_de_dados.atulizar_usuario(novo_saldo,id_usuario, 5)
                            Banco_de_dados.atulizar_aposta('green',aposta[0],1)
                            print('Deu Green')
                        else:
                            Banco_de_dados.atulizar_aposta(0, aposta[0], 2)
                            Banco_de_dados.atulizar_aposta('red', aposta[0],1)
                            relatorio = Banco_de_dados.consultar_relatorio(aposta[9])
                            Banco_de_dados.atualizar_relatorio(2, aposta[9], (relatorio[2] + 1))
                            Banco_de_dados.atualizar_relatorio(5, aposta[9], (relatorio[5] - 1))
                            lucro = 0 - aposta[2]
                            Banco_de_dados.atualizar_relatorio(3, aposta[9], (relatorio[3] + lucro))
                            print('Deu Red')
                    elif aposta[11] == 2:
                        if jogos[4] > jogos[5]:
                            id_usuario = Banco_de_dados.consultar_usuario_bots(aposta[12])
                            relatorio = Banco_de_dados.consultar_relatorio(aposta[9])
                            Banco_de_dados.atualizar_relatorio(1, aposta[9], (relatorio[1] + 1))
                            Banco_de_dados.atualizar_relatorio(5, aposta[9], (relatorio[5] - 1))
                            lucro = aposta[4] - aposta[2]
                            Banco_de_dados.atualizar_relatorio(3, aposta[9], (relatorio[3] + lucro))
                            saldo = Banco_de_dados.consultar_usuario_saldo(id_usuario)
                            novo_saldo = saldo + (float(aposta[4]))
                            Banco_de_dados.atulizar_usuario(novo_saldo, id_usuario, 5)
                            Banco_de_dados.atulizar_aposta('green', aposta[0],1)
                            print('Deu Green')
                        else:
                            Banco_de_dados.atulizar_aposta(0, aposta[0], 2)
                            Banco_de_dados.atulizar_aposta('red', aposta[0], 1)
                            relatorio = Banco_de_dados.consultar_relatorio(aposta[9])
                            Banco_de_dados.atualizar_relatorio(2, aposta[9], (relatorio[2] + 1))
                            Banco_de_dados.atualizar_relatorio(5, aposta[9], (relatorio[5] - 1))
                            lucro = 0 - aposta[2]
                            Banco_de_dados.atualizar_relatorio(3, aposta[9], (relatorio[3] + lucro))
                            print('Deu Red')
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
                        elif jogo[13] > jogo[12] and bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[9]: #1* fora zebra 2* analisar finalizações fora 3* analisar posse fora
                            var = 1
                    elif bot[13] == 'casaesta': #analisar o time da casa
                        if bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[9]: #1* analisar finalizações casa 2* analisar posse casa
                            var = 1
                    elif bot[13] == 'foraesta': #analisar o time de fora
                        if bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[9]: #1* analisar finalizações fora 2* analisar posse fora
                            var = 1
                verificar = Banco_de_dados.verificar_apostas(jogo[0], bot[0])
                if var == 1 and verificar == False:
                    if bot[12] == 'favapo': #apostar no favorito
                        if jogo[12] <= jogo[13]: #casa é o favorito
                            if bot[4] >= jogo[12] >= bot[3]: #analizar odd casa
                                Banco_de_dados.add_apostas(bot[12],float(bot[2]),float(jogo[12]),float(bot[2]*jogo[12]),'aberto',jogo[1],jogo[3],jogo[7],bot[0],jogo[0],1,bot[14],bot[1])
                                relatorio =Banco_de_dados.consultar_relatorio(bot[0])
                                Banco_de_dados.atualizar_relatorio(4,bot[0],(relatorio[4]+1))
                                Banco_de_dados.atualizar_relatorio(5, bot[0], (relatorio[5]+1))
                                saldo = Banco_de_dados.consultar_usuario_saldo(bot[14])
                                novo_saldo = saldo - float(bot[2])
                                Banco_de_dados.atulizar_usuario(novo_saldo, bot[14], 5)
                                print("Apostado em favorito(casa) id bot: " + str(bot[0]) + " id jogo: " + str(jogo[0]))
                        else: #fora é o favorito
                            if bot[4] >= jogo[13] >= bot[3]: #analizar odd fora
                                Banco_de_dados.add_apostas(bot[12], float(bot[2]), float(jogo[13]),float(bot[2] * jogo[13]), 'aberto', jogo[1], jogo[3],jogo[7], bot[0], jogo[0], 2, bot[14],bot[1])
                                relatorio = Banco_de_dados.consultar_relatorio(bot[0])
                                Banco_de_dados.atualizar_relatorio(4, bot[0], (relatorio[4] + 1))
                                Banco_de_dados.atualizar_relatorio(5, bot[0], (relatorio[5] + 1))
                                saldo = Banco_de_dados.consultar_usuario_saldo(bot[14])
                                novo_saldo = saldo - float(bot[2])
                                Banco_de_dados.atulizar_usuario(novo_saldo, bot[14], 5)
                                print("Apostado em favorito(fora) id bot: " + str(bot[0]) + " id jogo: " + str(jogo[0]))
                    elif bot[12] == 'zebraapo': #apostar na zebra
                        if jogo[12] > jogo[13]: #casa é a zebra
                            if bot[4] >= jogo[12] >= bot[3]: #analizar odd casa
                                Banco_de_dados.add_apostas(bot[12], float(bot[2]), float(jogo[12]),(bot[2] * jogo[12]), 'aberto', jogo[1], jogo[3],jogo[7], bot[0], jogo[0], 1, bot[14],bot[1])
                                relatorio = Banco_de_dados.consultar_relatorio(bot[0])
                                Banco_de_dados.atualizar_relatorio(4, bot[0], (relatorio[4] + 1))
                                Banco_de_dados.atualizar_relatorio(5, bot[0], (relatorio[5] + 1))
                                saldo = Banco_de_dados.consultar_usuario_saldo(bot[14])
                                novo_saldo = saldo - float(bot[2])
                                Banco_de_dados.atulizar_usuario(novo_saldo, bot[14], 5)
                                print("Apostado em zebra(casa) id bot: " + str(bot[0]) + " id jogo: " + str(jogo[0]))
                        else: #fora é a zebra
                            if bot[4] >= jogo[13] >= bot[3]: #analizar odd fora
                                Banco_de_dados.add_apostas(bot[12], float(bot[2]),float(jogo[13]),float(bot[2] * jogo[13]), 'aberto', jogo[1], jogo[3],jogo[7], bot[0], jogo[0], 2, bot[14],bot[1])
                                relatorio = Banco_de_dados.consultar_relatorio(bot[0])
                                Banco_de_dados.atualizar_relatorio(4, bot[0], (relatorio[4] + 1))
                                Banco_de_dados.atualizar_relatorio(5, bot[0], (relatorio[5] + 1))
                                saldo = Banco_de_dados.consultar_usuario_saldo(bot[14])
                                novo_saldo = saldo - float(bot[2])
                                Banco_de_dados.atulizar_usuario(novo_saldo,bot[14],5)
                                print("Apostado em zebra(fora) id bot: " + str(bot[0]) + " id jogo: " + str(jogo[0]))
                    elif bot[12] == 'casaapo': #apostar no time da casa
                        if bot[4] >= jogo[12] >= bot[3]: #analizar odd casa
                            Banco_de_dados.add_apostas(bot[12], float(bot[2]), float(jogo[12]),float(bot[2] * jogo[12]), 'aberto', jogo[1], jogo[3], jogo[7],bot[0], jogo[0], 1, bot[14],bot[1])
                            relatorio = Banco_de_dados.consultar_relatorio(bot[0])
                            Banco_de_dados.atualizar_relatorio(4, bot[0], (relatorio[4] + 1))
                            Banco_de_dados.atualizar_relatorio(5, bot[0], (relatorio[5] + 1))
                            saldo = Banco_de_dados.consultar_usuario_saldo(bot[14])
                            novo_saldo = saldo - float(bot[2])
                            Banco_de_dados.atulizar_usuario(novo_saldo, bot[14], 5)
                            print("Apostado em casa id bot: " + str(bot[0]) + " id jogo: " + str(jogo[0]))
                    elif bot[12] == 'foraapo': #apostar no time fora
                        if bot[4] >= jogo[13] >= bot[3]:  #analizar odd fora
                            Banco_de_dados.add_apostas(bot[12], float(bot[2]), float(jogo[13]),float(bot[2] * jogo[13]), 'aberto', jogo[1], jogo[3], jogo[7],bot[0], jogo[0], 2, bot[14],bot[1])
                            relatorio = Banco_de_dados.consultar_relatorio(bot[0])
                            Banco_de_dados.atualizar_relatorio(4, bot[0], (relatorio[4] + 1))
                            Banco_de_dados.atualizar_relatorio(5, bot[0], (relatorio[5] + 1))
                            saldo = Banco_de_dados.consultar_usuario_saldo(bot[14])
                            novo_saldo = saldo - float(bot[2])
                            Banco_de_dados.atulizar_usuario(novo_saldo, bot[14], 5)
                            print("Apostado em fora id bot: " + str(bot[0]) + " id jogo: " + str(jogo[0]))
    concluir_aposta()