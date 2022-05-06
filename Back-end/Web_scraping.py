import time
from bs4 import BeautifulSoup
from selenium import webdriver

import Banco_de_dados

jogos_ao_vivo_momento = 0


def WebScraping():
    def raspagem_stats(id):
        def raspagem_odd(id):
            browser.get(
                'https://www.flashscore.com.br/jogo/' + id + '/#/comparacao-de-odds/1x2-odds/tempo-regulamentar')
            time.sleep(1)
            try:
                odds = browser.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[3]/div/div[2]/div[1]')
                odds_html = odds.get_attribute('outerHTML')
                soup_odds = BeautifulSoup(odds_html, 'html.parser')
                odd = soup_odds.find_all('a', class_='oddsCell__odd')
                estatisticas.append(odd[0].getText())
                estatisticas.append(odd[1].getText())
                estatisticas.append(odd[2].getText())

                if estatisticas[5] == 'Encerrado':
                    Banco_de_dados.atualizar_jogos('fechado', estatisticas[0], 11)
                else:
                    primeiro = True
                    atualizou = 0
                    jogo = Banco_de_dados.consultas_jogos('aberto')
                    for i in range(len(jogo)):
                        if jogo[i][0] == estatisticas[0]:
                            esse = jogo[i]
                            primeiro = False
                    if primeiro == False:
                        atualizou = 1
                        if esse[4] != int(estatisticas[6]):
                            Banco_de_dados.atualizar_jogos(int(estatisticas[6]), estatisticas[0], 1)

                        if esse[5] != int(estatisticas[7]):
                            Banco_de_dados.atualizar_jogos(int(estatisticas[7]), estatisticas[0], 2)

                        if esse[6] != int(estatisticas[5]):
                            Banco_de_dados.atualizar_jogos(int(estatisticas[5]), estatisticas[0], 3)

                        if esse[8] != int(estatisticas[8]):
                            Banco_de_dados.atualizar_jogos(int(estatisticas[8]), estatisticas[0], 4)

                        if esse[9] != estatisticas[9]:
                            Banco_de_dados.atualizar_jogos(int(estatisticas[9]), estatisticas[0], 5)

                        if esse[10] != estatisticas[10]:
                            Banco_de_dados.atualizar_jogos(int(estatisticas[10]), estatisticas[0], 6)

                        if esse[11] != estatisticas[11]:
                            Banco_de_dados.atualizar_jogos(int(estatisticas[11]), estatisticas[0], 7)

                        if esse[12] != estatisticas[12]:
                            Banco_de_dados.atualizar_jogos(float(estatisticas[12]), estatisticas[0], 8)

                        if esse[13] != estatisticas[13]:
                            Banco_de_dados.atualizar_jogos(float(estatisticas[13]), estatisticas[0], 9)

                        if esse[14] != estatisticas[14]:
                            Banco_de_dados.atualizar_jogos(float(estatisticas[14]), estatisticas[0], 10)

                        if atualizou == 1:
                            for i in range(len(jogos_ao_vivo_momento)):
                                if jogos_ao_vivo_momento[i][0] == estatisticas[0]:
                                    del (jogos_ao_vivo_momento[i])
                                    break
                    else:
                        Banco_de_dados.add_jogos(estatisticas[4], estatisticas[0], estatisticas[1],
                                                 int(estatisticas[6]), estatisticas[2], int(estatisticas[7]),
                                                 int(estatisticas[5]), estatisticas[3], int(estatisticas[8]),
                                                 int(estatisticas[9]), int(estatisticas[10]),
                                                 int(estatisticas[11]), float(estatisticas[12]),
                                                 float(estatisticas[14]), float(estatisticas[13]), 'aberto')

            except:

                estatisticas.append('0.00')
                estatisticas.append('0.00')
                estatisticas.append('0.00')
                if estatisticas[5] == 'Encerrado':
                    Banco_de_dados.atualizar_jogos('fechado', estatisticas[0], 11)
                else:
                    primeiro = True
                    atualizou = 0
                    jogo = Banco_de_dados.consultas_jogos('aberto')
                    for i in range(len(jogo)):
                        if jogo[i][0] == estatisticas[0]:
                            esse = jogo[i]

                            primeiro = False
                    if primeiro == False:
                        atualizou = 1
                        if esse[4] != int(estatisticas[6]):
                            Banco_de_dados.atualizar_jogos(int(estatisticas[6]), estatisticas[0], 1)

                        if esse[5] != int(estatisticas[7]):
                            Banco_de_dados.atualizar_jogos(int(estatisticas[7]), estatisticas[0], 2)

                        if esse[6] != int(estatisticas[5]):
                            Banco_de_dados.atualizar_jogos(int(estatisticas[5]), estatisticas[0], 3)

                        if esse[8] != int(estatisticas[8]):
                            Banco_de_dados.atualizar_jogos(int(estatisticas[8]), estatisticas[0], 4)

                        if esse[9] != estatisticas[9]:
                            Banco_de_dados.atualizar_jogos(int(estatisticas[9]), estatisticas[0], 5)

                        if esse[10] != estatisticas[10]:
                            Banco_de_dados.atualizar_jogos(int(estatisticas[10]), estatisticas[0], 6)

                        if esse[11] != estatisticas[11]:
                            Banco_de_dados.atualizar_jogos(int(estatisticas[11]), estatisticas[0], 7)

                        if esse[12] != estatisticas[12]:
                            Banco_de_dados.atualizar_jogos(float(estatisticas[12]), estatisticas[0], 8)

                        if esse[13] != estatisticas[13]:
                            Banco_de_dados.atualizar_jogos(float(estatisticas[13]), estatisticas[0], 9)

                        if esse[14] != estatisticas[14]:
                            Banco_de_dados.atualizar_jogos(float(estatisticas[14]), estatisticas[0], 10)

                        if atualizou == 1:
                            for i in range(len(jogos_ao_vivo_momento)):
                                if jogos_ao_vivo_momento[i][0] == estatisticas[0]:
                                    del (jogos_ao_vivo_momento[i])
                                    break

                    else:
                        Banco_de_dados.add_jogos(estatisticas[4], estatisticas[0], estatisticas[1],
                                                 int(estatisticas[6]), estatisticas[2], int(estatisticas[7]),
                                                 int(estatisticas[5]), estatisticas[3], int(estatisticas[8]),
                                                 int(estatisticas[9]), int(estatisticas[10]),
                                                 int(estatisticas[11]), float(estatisticas[12]),
                                                 float(estatisticas[14]), float(estatisticas[13]), 'aberto')

        estatisticas = []
        estatisticas.append(id)
        browser.get(' https://www.flashscore.com.br/jogo/' + id + '/#/resumo-de-jogo/estatisticas-de-jogo/0')
        time.sleep(1)
        jogo = browser.find_element_by_xpath('/html/body/div[2]/div')
        jogo_html = jogo.get_attribute('outerHTML')
        soup_jogo = BeautifulSoup(jogo_html, 'html.parser')
        times = soup_jogo.find_all('div', class_='participant__participantName participant__overflow')
        estatisticas.append(times[0].getText())
        estatisticas.append(times[1].getText())
        # data e hora do jogo
        data_hora = soup_jogo.find('div', class_='duelParticipant__startTime').get_text()
        estatisticas.append(data_hora)
        campeonato = soup_jogo.find('span', class_='tournamentHeader__country').get_text()
        if '-' in campeonato:
            for i in range(len(campeonato)):
                if campeonato[i] == '-':
                    camp = campeonato[:i]
                    estatisticas.append(camp)
                    break
        else:
            estatisticas.append(campeonato)
        tempo = soup_jogo.find('div', class_='detailScore__status').get_text()

        if tempo == "Intervalo":
            estatisticas.append('45')
        elif tempo == 'Encerrado':
            estatisticas.append(tempo)
        else:
            tempo_2 = tempo[11:]
            if len(tempo_2) > 2:
                tempo_3 = tempo_2[:2]
                if tempo_3[0] == '0' or tempo_3[0] == '1' or tempo_3[0] == '2' or tempo_3[0] == '3' or tempo_3[0] == \
                        '4' or tempo_3[0] == '5' or tempo_3[0] == '6' or tempo_3[0] == '7' or tempo_3[0] == '8' or \
                        tempo_3[0] == '9':
                    if tempo_3[1] == '0' or tempo_3[1] == '1' or tempo_3[1] == '2' or tempo_3[1] == '3' or tempo_3[0] \
                            == '4' or tempo_3[1] == '5' or tempo_3[1] == '6' or tempo_3[1] == '7' or tempo_3[1] == '8' \
                            or tempo_3[1] == '9':
                        estatisticas.append(tempo_3)
                    else:
                        estatisticas.append(tempo_3[0])
            elif len(tempo_2) == 2:
                if tempo_2[0] == '0' or tempo_2[0] == '1' or tempo_2[0] == '2' or tempo_2[0] == '3' or tempo_2[0] == \
                        '4' or tempo_2[0] == '5' or tempo_2[0] == '6' or tempo_2[0] == '7' or tempo_2[0] == '8' or \
                        tempo_2[0] == '9':
                    if tempo_2[1] == '0' or tempo_2[1] == '1' or tempo_2[1] == '2' or tempo_2[1] == '3' or tempo_2[1] \
                            == '4' or tempo_2[1] == '5' or tempo_2[1] == '6' or tempo_2[1] == '7' or tempo_2[1] == '8' \
                            or tempo_2[1] == '9':
                        estatisticas.append(tempo_2)
                    else:
                        estatisticas.append(tempo_2[0])

        # Nome de casa estatistica
        if tempo == 'Encerrado':
            resultado = soup_jogo.find('div', class_='detailScore__matchInfo').get_text()
            resul = list(resultado)
            estatisticas.append(resul[0])
            estatisticas.append(resul[2])
        else:
            resultado = soup_jogo.find('div', class_='detailScore__wrapper detailScore__live').get_text()
            resul = list(resultado)
            estatisticas.append(resul[0])
            estatisticas.append(resul[2])

        stats_name = soup_jogo.find_all('div', class_='stat__categoryName')
        # Estatisticas do time da casa
        casa_stats = soup_jogo.find_all('div', class_='stat__homeValue')
        # Estatisticas do time de fora
        fora_stats = soup_jogo.find_all('div', class_='stat__awayValue')
        # Lista com todos os nomes das estatisticas da partida
        nome_stats = ['Posse de bola', 'Finalizações']
        cont = 0
        for i in range(len(stats_name)):
            if stats_name[i].getText() in nome_stats:
                if len(casa_stats[i].getText()) > 2:
                    cont += 1
                    casa_stat = casa_stats[i].getText()
                    fora_stat = fora_stats[i].getText()
                    casa_sta = casa_stat[:2]
                    fora_sta = fora_stat[:2]
                    estatisticas.append(casa_sta)
                    estatisticas.append(fora_sta)
                else:
                    cont += 1
                    estatisticas.append(casa_stats[i].getText())
                    estatisticas.append(fora_stats[i].getText())
        if cont == 0:
            estatisticas.append('0')
            estatisticas.append('0')
            estatisticas.append('0')
            estatisticas.append('0')
        elif cont == 1:
            estatisticas.append('0')
            estatisticas.append('0')
        else:
            ok = 1
        raspagem_odd(id)

    jogos_ao_vivo_momento = Banco_de_dados.consultas_jogos('aberto')
    browser = webdriver.Chrome()
    browser.get('https://www.flashscore.com.br')
    ao_vivo = browser.find_element_by_xpath('/html/body/div[7]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div[2]')
    ao_vivo.click()
    jogos = browser.find_element_by_xpath('/html/body/div[7]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/section/div/div')
    site_html = jogos.get_attribute('outerHTML')
    soup = BeautifulSoup(site_html, 'html.parser')
    for rodada in soup.find_all('div', attrs={
        "class": "event__match event__match--live event__match--last event__match--twoLine"}):
        # Id de cada partida
        id_jogo = rodada['id']
        id_j = id_jogo[4:]
        raspagem_stats(id_j)
    for rodada in soup.find_all('div', attrs={"class": "event__match event__match--live event__match--twoLine"}):
        # Id de cada partida
        id_jogo = rodada['id']
        id_j = id_jogo[4:]
        raspagem_stats(id_j)

    tamanho = len(jogos_ao_vivo_momento)
    if tamanho > 0:
        for i in range(tamanho):
            Banco_de_dados.atualizar_jogos('fechado', jogos_ao_vivo_momento[i][0], 11)
