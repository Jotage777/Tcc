import time

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import Banco_de_dados

def raspagem_stats(id):
    estatisticas = []
    estatisticas.append(id)
    browser.get(' https://www.flashscore.com.br/jogo/' + id + '/#/resumo-de-jogo/estatisticas-de-jogo/0')
    time.sleep(2)
    jogo = browser.find_element_by_xpath('/html/body/div[2]/div')
    jogo_html = jogo.get_attribute('outerHTML')
    soup_jogo = BeautifulSoup(jogo_html, 'html.parser')
    times = soup_jogo.find_all('div', class_='participant__participantName participant__overflow')
    estatisticas.append(times[0].getText())
    estatisticas.append(times[1].getText())
    # data e hora do jogo
    data_hora = soup_jogo.find('div', class_='duelParticipant__startTime').get_text()
    estatisticas.append(data_hora)
    tempo = soup_jogo.find('div', class_='detailScore__status').get_text()
    estatisticas.append(tempo)
    # Nome de casa estatistica
    stats_name = soup_jogo.find_all('div', class_='stat__categoryName')

    # Estatisticas do time da casa
    casa_stats = soup_jogo.find_all('div', class_='stat__homeValue')

    # Estatistica do time de fora
    fora_stats = soup_jogo.find_all('div', class_='stat__awayValue')

    # Lista com todos os nomes das estatisticas da partida
    nome_stats = ['Posse de bola', 'Finalizações']
    cont = 0
    for i in range(len(stats_name)):
        if stats_name[i].getText() in nome_stats:
            cont+=1
            estatisticas.append(casa_stats[i].getText())
            estatisticas.append(fora_stats[i].getText())
    if cont ==0:
        estatisticas.append('0')
        estatisticas.append('0')
        estatisticas.append('0')
        estatisticas.append('0')
        print(estatisticas)
        return estatisticas
    elif cont==1:
        estatisticas.append('0')
        estatisticas.append('0')
        print(estatisticas)
        return estatisticas
    else:
        print(estatisticas)
        return estatisticas

browser = webdriver.Chrome()
browser.get('https://www.flashscore.com.br')
ao_vivo = browser.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div[2]')
ao_vivo.click()
jogos = browser.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div')
site_html = jogos.get_attribute('outerHTML')
soup = BeautifulSoup(site_html,'html.parser')
for rodada in soup.find_all('div', attrs={"class": "event__match event__match--live event__match--last event__match--twoLine"}  ):
     #Id de cada partida
    id_jogo=rodada['id']
    id_j = id_jogo[4:]
    raspagem_stats(id_j)
for rodada in soup.find_all('div', attrs={"class": "event__match event__match--live event__match--twoLine"}  ):
     #Id de cada partida
    id_jogo=rodada['id']
    id_j = id_jogo[4:]
    raspagem_stats(id_j)