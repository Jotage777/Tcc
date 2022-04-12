import time

from selenium import webdriver
from bs4 import BeautifulSoup
import Banco_de_dados


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
                print(odd[0].getText())
                print(odd[1].getText())
                print(odd[2].getText())
                print(estatisticas)
                Banco_de_dados.add_jogos(estatisticas[4], estatisticas[0], estatisticas[1], int(estatisticas[6]),
                                         estatisticas[2], int(estatisticas[7]), estatisticas[3],
                                         float(estatisticas[12]), float(estatisticas[13]), float(estatisticas[14]))
            except:
                print("Odds não disponiveis")
                print(estatisticas)
                Banco_de_dados.add_jogos(estatisticas[4], estatisticas[0], estatisticas[1], int(estatisticas[6]),
                                         estatisticas[2], int(estatisticas[7]), estatisticas[3], '0.00', '0.00', '0.00')

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
            estatisticas.append('90')
        else:
            tempo_2 = tempo[11:]
            estatisticas.append(tempo_2)
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
            print(resul[0])
            print(resul[2])
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
            print('ok')
        raspagem_odd(id)
        print(estatisticas)

    browser = webdriver.Chrome()
    browser.get('https://www.flashscore.com.br')
    ao_vivo = browser.find_element_by_xpath(
        '/html/body/div[6]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div[2]')
    ao_vivo.click()
    jogos = browser.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div')
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


WebScraping()
