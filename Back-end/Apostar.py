import Banco_de_dados


def concluir_aposta():
    lista_apostas = list(Banco_de_dados.consultas("SELECT * FROM Apostas"))
    lista_jogos_encerrados = Banco_de_dados.consultas_jogos('fechado')
    # lendo cada aposta
    for aposta in lista_apostas:
        # constantes
        id_aposta = aposta[0]
        valor_apostado = aposta[2]
        retorno = aposta[4]
        situacao = aposta[5]
        id_bot = aposta[9]
        id_jogo_aposta = aposta[10]
        casa_fora = aposta[11]
        id_usuario = aposta[12]
        # verificar se esta em aberto a aposta
        if situacao == 'aberto':
            # lendo cada jogo encerrado
            for jogos in lista_jogos_encerrados:
                id_jogo = jogos[0]
                resultado_casa = jogos[4]
                resultado_fora = jogos[5]
                if id_jogo_aposta == id_jogo:
                    # se aposta foi no time da casa
                    if casa_fora == 1:
                        # verificando se o time casa venceu
                        if resultado_casa > resultado_fora:
                            salvar_green(id_usuario, id_bot, retorno, valor_apostado, id_aposta)
                        else:
                            salvar_red(id_aposta, id_bot, valor_apostado)
                    # se aposta foi no time fora
                    elif casa_fora == 2:
                        # verificando se o time fora venceu
                        if resultado_fora > resultado_casa:
                            salvar_green(id_usuario, id_bot, retorno, valor_apostado, id_aposta)
                        else:
                            salvar_red(id_aposta, id_bot, valor_apostado)


def salvar_green(id_usuario, id_bot, retorno, apostado, id_aposta):
    relatorio = Banco_de_dados.consultar_relatorio(id_bot)
    # constantes
    greens = relatorio[1]
    lucro_rel = relatorio[3]
    apostas_abertas = relatorio[5]
    Banco_de_dados.atualizar_relatorio(1, id_bot, (greens + 1))
    Banco_de_dados.atualizar_relatorio(5, id_bot, (apostas_abertas - 1))
    lucro = retorno - apostado
    Banco_de_dados.atualizar_relatorio(3, id_bot, (lucro_rel + lucro))
    saldo = Banco_de_dados.consultar_usuario_saldo(id_usuario)
    novo_saldo = saldo + (float(retorno))
    Banco_de_dados.atulizar_usuario(novo_saldo, id_usuario, 5)
    Banco_de_dados.atulizar_aposta('green', id_aposta, 1)


def salvar_red(id_aposta, id_bot, apostado):
    Banco_de_dados.atulizar_aposta(0, id_aposta, 2)
    Banco_de_dados.atulizar_aposta('red', id_aposta, 1)
    relatorio = Banco_de_dados.consultar_relatorio(id_bot)
    # constantes
    reds = relatorio[2]
    lucro_rel = relatorio[3]
    apostas_abertas = relatorio[5]
    Banco_de_dados.atualizar_relatorio(2, id_bot, (reds + 1))
    Banco_de_dados.atualizar_relatorio(5, id_bot, (apostas_abertas - 1))
    lucro = 0 - apostado
    Banco_de_dados.atualizar_relatorio(3, id_bot, (lucro_rel + lucro))


def analise():
    lista_bots = Banco_de_dados.consultas("SELECT * FROM Bots")
    jogos_AoVivo = Banco_de_dados.consultas_jogos('aberto')
    # percorrer bots
    for bot in lista_bots:
        # constantes
        id_bot = bot[0]
        nome = bot[1]
        responsabilidade = bot[2]
        odd_minima = bot[3]
        odd_maxima = bot[4]
        tempo_jogo_minimo = bot[5]
        tempo_jogo_maximo = bot[6]
        finalizacao_min = bot[7]
        finalizacao_max = bot[8]
        posse_bola_min = bot[9]
        posse_bola_max = bot[10]
        ativado = bot[11]
        apostar = bot[12]
        analisar = bot[13]
        id_usuario = bot[14]
        # se ativado e saldo suficiente
        if ativado == True and responsabilidade <= Banco_de_dados.consultar_usuario_saldo(id_usuario):
            # percorrer jogos
            for jogo in jogos_AoVivo:
                # constantes
                id_jogo = jogo[0]
                time_casa = jogo[1]
                time_fora = jogo[3]
                resultado_casa = jogo[4]
                resultado_fora = jogo[5]
                tempo = jogo[6]
                data = jogo[7]
                posse_bola_casa = jogo[8]
                posse_bola_fora = jogo[9]
                finalizacao_casa = jogo[10]
                finalizacao_fora = jogo[11]
                odd_casa = jogo[12]
                odd_fora = jogo[14]
                # Se o jogo estiver empate
                if resultado_casa == resultado_fora:
                    verificar = Banco_de_dados.verificar_apostas(id_jogo, id_bot)
                    if tempo_jogo_maximo >= tempo >= tempo_jogo_minimo and verificar == False:
                        if analisar == 'casaesta' or (analisar == 'favesta' and odd_casa <= odd_fora) or (analisar == 'zebraesta' and odd_casa > odd_fora):
                            if finalizacao_max >= finalizacao_casa >= finalizacao_min and posse_bola_max >= posse_bola_casa >= posse_bola_min:
                                if (apostar == 'casaapo' or (apostar == 'favapo' and odd_casa <= odd_fora) or (apostar == 'zebraapo' and odd_casa > odd_fora)) and odd_maxima >= odd_casa >= odd_minima:
                                    fazer_aposta(id_bot, id_usuario, responsabilidade, apostar, odd_casa, time_casa, time_fora, data, id_jogo, nome, 1)
                                elif (apostar == 'foraapo' or (apostar == 'favapo' and odd_casa > odd_fora) or (apostar == 'zebraapo' and odd_casa <= odd_fora)) and odd_maxima >= odd_fora >= odd_minima:
                                    fazer_aposta(id_bot, id_usuario, responsabilidade, apostar, odd_fora, time_casa, time_fora, data, id_jogo, nome, 2)
                        elif analisar == 'foraesta' or (analisar == 'favesta' and odd_casa > odd_fora) or (analisar == 'zebraesta' and odd_casa <= odd_fora):
                            if finalizacao_max >= finalizacao_fora >= finalizacao_min and posse_bola_max >= posse_bola_fora >= posse_bola_min:
                                if (apostar == 'casaapo' or (apostar == 'favapo' and odd_casa <= odd_fora) or (apostar == 'zebraapo' and odd_casa > odd_fora)) and odd_maxima >= odd_casa >= odd_minima:
                                    fazer_aposta(id_bot, id_usuario, responsabilidade, apostar, odd_casa, time_casa, time_fora, data, id_jogo, nome, 1)
                                elif (apostar == 'foraapo' or (apostar == 'favapo' and odd_casa > odd_fora) or (apostar == 'zebraapo' and odd_casa <= odd_fora)) and odd_maxima >= odd_fora >= odd_minima:
                                    fazer_aposta(id_bot, id_usuario, responsabilidade, apostar, odd_fora, time_casa, time_fora, data, id_jogo, nome, 2)
    concluir_aposta()


def fazer_aposta(id_bot, id_usuario, responsabilidade, apostar, odd, casa, fora, data, id_jogo, nome_bot, casa_fora):
    relatorio = Banco_de_dados.consultar_relatorio(id_bot)
    # constantes
    total_apostas = relatorio[4]
    apostas_abertas = relatorio[5]
    Banco_de_dados.atualizar_relatorio(4, id_bot, (total_apostas + 1))
    Banco_de_dados.atualizar_relatorio(5, id_bot, (apostas_abertas + 1))
    saldo = Banco_de_dados.consultar_usuario_saldo(id_usuario)
    novo_saldo = saldo - float(responsabilidade)
    Banco_de_dados.atulizar_usuario(novo_saldo, id_usuario, 5)
    Banco_de_dados.add_apostas(apostar, float(responsabilidade), float(odd), float(responsabilidade * odd), 'aberto', casa, fora, data, id_bot, id_jogo, casa_fora, id_usuario, nome_bot)