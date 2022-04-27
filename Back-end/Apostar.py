import Banco_de_dados


def concluir_aposta():
    lista_apostas = list(Banco_de_dados.consultas("SELECT * FROM Apostas"))
    lista_jogos_encerrados = Banco_de_dados.consultas_jogos('fechado')
    for aposta in lista_apostas:  # lendo cada aposta
        if aposta[5] == 'aberto':  # verificar se esta em aberto a aposta
            for jogos in lista_jogos_encerrados:  # lendo cada jogo encerrado
                if aposta[10] == jogos[0]:  # verificar se o jogo bate com o jogo da aposta
                    if aposta[11] == 1:  # se aposta foi no time da casa
                        if jogos[5] > jogos[4]:  # verificando se o time venceu
                            salvar_green(aposta[12], aposta[9], aposta[4], aposta[2], aposta[0])  # green
                        else:
                            salvar_red(aposta[0], aposta[9], aposta[2])  # red
                    elif aposta[11] == 2:  # se aposta foi no time fora
                        if jogos[4] > jogos[5]:  # verificando se o time venceu
                            salvar_green(aposta[12], aposta[9], aposta[4], aposta[2], aposta[0])  # green
                        else:
                            salvar_red(aposta[0], aposta[9], aposta[2])  # red


def salvar_green(id_usuario, id_bot, retorno, apostado, id_aposta):
    relatorio = Banco_de_dados.consultar_relatorio(id_bot)
    Banco_de_dados.atualizar_relatorio(1, id_bot, (relatorio[1] + 1))
    Banco_de_dados.atualizar_relatorio(5, id_bot, (relatorio[5] - 1))
    lucro = retorno - apostado
    Banco_de_dados.atualizar_relatorio(3, id_bot, (relatorio[3] + lucro))
    saldo = Banco_de_dados.consultar_usuario_saldo(id_usuario)
    novo_saldo = saldo + (float(retorno))
    Banco_de_dados.atulizar_usuario(novo_saldo, id_usuario, 5)
    Banco_de_dados.atulizar_aposta('green', id_aposta, 1)


def salvar_red(id_aposta, id_bot, apostado):
    Banco_de_dados.atulizar_aposta(0, id_aposta, 2)
    Banco_de_dados.atulizar_aposta('red', id_aposta, 1)
    relatorio = Banco_de_dados.consultar_relatorio(id_bot)
    Banco_de_dados.atualizar_relatorio(2, id_bot, (relatorio[2] + 1))
    Banco_de_dados.atualizar_relatorio(5, id_bot, (relatorio[5] - 1))
    lucro = 0 - apostado
    Banco_de_dados.atualizar_relatorio(3, id_bot, (relatorio[3] + lucro))


def analise():
    lista_bots = Banco_de_dados.consultas("SELECT * FROM Bots")
    jogos_AoVivo = Banco_de_dados.consultas_jogos('aberto')
    for bot in lista_bots:
        if bot[11] == True and bot[2] <= Banco_de_dados.consultar_usuario_saldo(
                bot[14]):  # se ativado e saldo suficiente
            for jogo in jogos_AoVivo:  # percorrer jogos
                if bot[2] <= Banco_de_dados.consultar_usuario_saldo(bot[14]):
                    var_esta = 0
                    if bot[6] >= jogo[6] >= bot[5]:  # verificar se o tempo de jogo esta no intervalo do bot
                        if bot[13] == 'favesta':  # analisar o time favorito
                            if jogo[12] <= jogo[13] and bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[
                                9]:  # 1* casa favorito 2* analisar finalizações casa 3* analisar posse casa
                                var_esta = 1
                            elif jogo[13] < jogo[12] and bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[
                                9]:  # 1* fora favorito 2* analisar finalizações fora 3* analisar posse fora
                                var_esta = 1
                        elif bot[13] == 'zebraesta':  # analisar a zebra
                            if jogo[12] >= jogo[13] and bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[
                                9]:  # 1* casa zebra 2* analisar finalizações casa 3* analisar posse casa
                                var_esta = 1
                            elif jogo[13] > jogo[12] and bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[
                                9]:  # 1* fora zebra 2* analisar finalizações fora 3* analisar posse fora
                                var_esta = 1
                        elif bot[13] == 'casaesta':  # analisar o time da casa
                            if bot[8] >= jogo[10] >= bot[7] and bot[10] >= jogo[8] >= bot[
                                9]:  # 1* analisar finalizações casa 2* analisar posse casa
                                var_esta = 1
                        elif bot[13] == 'foraesta':  # analisar o time de fora
                            if bot[8] >= jogo[11] >= bot[7] and bot[10] >= jogo[9] >= bot[
                                9]:  # 1* analisar finalizações fora 2* analisar posse fora
                                var_esta = 1
                    verificar = Banco_de_dados.verificar_apostas(jogo[0], bot[0])  # verificar se já foi feita a aposta
                    if var_esta == 1 and verificar == False:  # se jogo atendeu as estaticar e se já não tem aposta nesse jogo por este bot
                        if bot[12] == 'favapo':  # apostar no favorito
                            if jogo[12] <= jogo[13]:  # casa é o favorito
                                if bot[4] >= jogo[12] >= bot[3]:  # analisar odd casa
                                    apostar(bot[0], bot[14], bot[2], bot[12], jogo[12], jogo[1], jogo[3], jogo[7],
                                            jogo[0], bot[1])
                            else:  # fora é o favorito
                                if bot[4] >= jogo[13] >= bot[3]:  # analisar odd fora
                                    apostar(bot[0], bot[14], bot[2], bot[12], jogo[13], jogo[1], jogo[3], jogo[7],
                                            jogo[0], bot[1])
                        elif bot[12] == 'zebraapo':  # apostar na zebra
                            if jogo[12] > jogo[13]:  # casa é a zebra
                                if bot[4] >= jogo[12] >= bot[3]:  # analisar odd casa
                                    apostar(bot[0], bot[14], bot[2], bot[12], jogo[12], jogo[1], jogo[3], jogo[7],
                                            jogo[0], bot[1])
                            else:  # fora é a zebra
                                if bot[4] >= jogo[13] >= bot[3]:  # analisar odd fora
                                    apostar(bot[0], bot[14], bot[2], bot[12], jogo[13], jogo[1], jogo[3], jogo[7],
                                            jogo[0], bot[1])
                        elif bot[12] == 'casaapo':  # apostar no time da casa
                            if bot[4] >= jogo[12] >= bot[3]:  # analisar odd casa
                                apostar(bot[0], bot[14], bot[2], bot[12], jogo[12], jogo[1], jogo[3], jogo[7], jogo[0],
                                        bot[1])
                        elif bot[12] == 'foraapo':  # apostar no time fora
                            if bot[4] >= jogo[13] >= bot[3]:  # analisar odd fora
                                apostar(bot[0], bot[14], bot[2], bot[12], jogo[13], jogo[1], jogo[3], jogo[7], jogo[0],
                                        bot[1])
    concluir_aposta()


def apostar(id_bot, id_usuario, responsabilidade, apostar, odd, casa, fora, data, id_jogo, nome_bot):
    relatorio = Banco_de_dados.consultar_relatorio(id_bot)
    Banco_de_dados.atualizar_relatorio(4, id_bot, (relatorio[4] + 1))
    Banco_de_dados.atualizar_relatorio(5, id_bot, (relatorio[5] + 1))
    saldo = Banco_de_dados.consultar_usuario_saldo(id_usuario)
    novo_saldo = saldo - float(responsabilidade)
    Banco_de_dados.atulizar_usuario(novo_saldo, id_usuario, 5)
    Banco_de_dados.add_apostas(apostar, float(responsabilidade), float(odd), float(responsabilidade * odd), 'aberto',
                               casa, fora, data, id_bot, id_jogo, 1, id_usuario, nome_bot)
