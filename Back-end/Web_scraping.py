import requests
from bs4 import BeautifulSoup

url = 'https://www.flashscore.com.br'

site = requests.get(url)
soup = BeautifulSoup(site.content,'html.parser')
ao_vivo = soup.select('.filters__tab')
print(ao_vivo)
#for rodada in soup.find_all('div', attrs={"class": "event__match event__match--live event__match--last event__match--twoLine"}):
#    # Id de cada partida
 #   id_jogo = rodada['id']
 #   id_j = id_jogo[4:]
 #   print(id_j)

def scrap_jogos(id):
    estatisticas =[]
    #estatisticas.append(id)

    url_jogo = ' https://www.flashscore.com.br/jogo/'+id+'/#/resumo-de-jogo/resumo-de-jogo'
    site_jogo = requests.get(url_jogo)
    soup_jogo= BeautifulSoup(site_jogo.content,'html.parser')
    times = soup_jogo.find_all('div', class_='participant__participantName participant__overflow')
    #estatisticas.append(times[0].getText())
    #estatisticas.append(times[1].getText())
    # data e hora do jogo
    data_hora = soup_jogo.find_all('div', class_='duelParticipant__startTime')
    #estatisticas.append(data_hora[0].getText())
    tempo = soup_jogo.find_all('div', class_='detailScore__status')
    print(tempo)
    # Nome de casa estatistica
    stats_name = soup_jogo.find_all('div', class_='statCategoryName')
    # Estatisticas do time da casa
    casa_stats = soup_jogo.find_all('div', class_='statHomeValue')
    # Estatistica do time de fora
    fora_stats = soup_jogo.find_all('div', class_='statAwayValue')
    # Lista com todos os nomes das estatisticas da partida
    nome_stats = ['Posse de bola', 'Finalizações']
    for i in range(len(nome_stats)):
        if nome_stats[i] in stats_name:
            for o in range(len(stats_name)):
                if nome_stats[i] == stats_name[o]:
                    estatisticas.append(casa_stats[o])
                    estatisticas.append(fora_stats[o])
        else:
            estatisticas.append('0')
            estatisticas.append('0')

    return estatisticas