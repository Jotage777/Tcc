import Banco_de_dados
import Web_scraping
import Apostar
#
# Banco_de_dados.add_usuario('Gabriel', 'Joao Gabriel de Oliveira Ponciano', 'gabrieloliveira_pb@hotmail.com',
#                            '24/05/1999', '200.00', 'gabriel')
# Banco_de_dados.add_usuario('Messias', 'Joao Messias da Silva Medeiros', 'joaomessias00@hotmail.com', '27/05/1999',
#                            '500.00', 'messias123')
# Banco_de_dados.add_usuario('Igor', 'Igor barbosa', 'igor@ifpb.com', '04/04/2000', '1000.00', '1234')
#
# Banco_de_dados.add_bots('bot1g', '1', '1.2', '2.0', '0', '50', '5', '99', '55', '99', '1', 'favapo', 'favesta',
#                         'Gabriel')
# Banco_de_dados.add_bots('bot2m', '5', '1.8', '2.9', '15', '60', '0', '2', '0', '40', '1', 'favapo', 'zebraesta',
#                         'Messias')
# Banco_de_dados.add_bots('bot3g', '2', '2.2', '5.0', '15', '30', '1', '99', '60', '99', '1', 'foraapo', 'foraesta',
#                         'Gabriel')
# Banco_de_dados.add_bots('bot4m', '10', '2.8', '3.9', '10', '50', '0', '1', '50', '70', '1', 'favapo', 'zebraesta',
#                         'Messias')
# Banco_de_dados.add_bots('bot5m', '2.5', '1.2', '2.5', '5', '40', '0', '10', '55', '99', '1', 'favapo', 'favesta',
#                         'Messias')
# Banco_de_dados.add_bots('bot6i', '5', '1.1', '2.6', '0', '25', '5', '99', '0', '35', '1', 'casaapo', 'foraesta',
#                         'Igor')
# Banco_de_dados.add_bots('bot7i', '2.5', '2.1', '5.0', '0', '95', '0', '10', '55', '99', '1', 'zebrapo', 'casaesta',
#                         'Igor')
# Banco_de_dados.add_bots('bot8g', '30', '2.1', '3.6', '45', '95', '0', '5', '0', '65', '1', 'zebrapo', 'foraesta',
#                         'Gabriel')
# Banco_de_dados.add_bots('bot9m', '50', '1.1', '1.6', '75', '95', '0', '2', '0', '40', '1', 'casaapo', 'zebraesta',
#                         'Messias')
#
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '1')
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '2')
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '3')
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '4')
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '5')
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '6')
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '7')
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '8')
# Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '9')

# Web_scraping.WebScraping()
# Banco_de_dados.deletar_bot(2)

Apostar.analise()

# estatisticas=['h8dml01n', 'França F', 'Eslovénia F', '12.04.2022 16:10', 'EUROPA: Copa do Mundo de Futebol Feminino ', '0', '1', '0', '0', '0', '0', '1.03', '13.00', '36.00']
# ('n3F6bzD0', 'U. Católica (Chi)', 'AMÉRICA DO SUL: Copa Libertadores ', 'Sporting Cristal (Per)', 1, 0, 46, '12.04.2022 19:15', 48, 52, 2, 0, 1.55, 6.0, 4.2, 8)
#('zmhbk8Ea', 'Bahia', 'BRASIL: Copa do Brasil ', 'Azuriz', 0, 0, 6, '19.04.2022 19:30', 0, 0, 0, 0, 0.0, 0.0, 0.0, 1)
# Banco_de_dados.add_jogos_aovivo('BRASIL: Campeonato Brasileiro ', 'nfoasnfw', 'Flamengo', 3,  'São Paulo', 1, 45, '19.04.2022 19:30', 60, 40, 7, 2, 1.8, 2.8, 4.0)
# Banco_de_dados.add_jogos_aovivo('BRASIL: Copa do Brasil ', 'okpasjg', 'Flamengo', 7, 'Campinense', 1, 30, '19.04.2022 19:30', 80, 20, 16, 1, 1.05, 8.0, 17.0)
# Banco_de_dados.add_jogos_aovivo('MUNDO: Copa do Mundo ', 'asf24fs', 'Brasil', 2, 'Alemanha', 0, 40, '19.04.2022 19:30', 40, 60, 2, 1, 2.6, 3.0, 2.4)
# Banco_de_dados.add_jogos_aovivo('EUROPA: Liga dos Campeões ', 'oihfd4f', 'Barcelona', 0, 'Bayern', 2, 20, '19.04.2022 19:30', 48, 52, 2, 3, 2.1, 2.8, 3.1)
# Banco_de_dados.add_jogos_aovivo('MUNDO: Copa do Mundo ', 'agadgadg', 'Brasil', 2, 'Alemanha', 0, 40, '19.04.2022 19:30', 40, 60, 2, 1, 2.6, 3.0, 2.4)
# Banco_de_dados.add_jogos_aovivo('MUNDO: Copa do Mundo ', 'gag6433g', 'Japão', 2, 'Alemanha', 2, 85, '19.04.2022 19:30', 55, 45, 3, 10, 4.5, 1.5, 1.9)
# Banco_de_dados.add_jogos_aovivo('MUNDO: Copa do Mundo ', 'pjp431oj', 'Espanha', 0, 'Gales', 0, 60, '19.04.2022 19:30', 40, 60, 7, 4, 2.0, 1.9, 3.4)

# campeonato: str, id: str, casa: str, resultado_casa: int, fora: str, resultado_fora: int,
#                      tempo: int, data: str, posse_casa: int, posse_fora: int, finalizacao_casa: int,
#                      finalizacao_fora: int, odd_casa: float, odd_empate: float, odd_fora: float

# Banco_de_dados.add_jogos_aovivo(estatisticas[4], estatisticas[0], estatisticas[1], int(estatisticas[6]),
#                                 estatisticas[2], int(estatisticas[7]), int(estatisticas[5]), estatisticas[3],
#                                 int(estatisticas[8]), int(estatisticas[9]), int(estatisticas[10]),
#                                 int(estatisticas[11]), float(estatisticas[12]), float(estatisticas[13]),
#                                 float(estatisticas[14]))


# delete = "DELETE FROM Jogos_AoVivo"
# Banco_de_dados.deletar_jogoAoVivo('xn5lxz59')
# Banco_de_dados.deletar(delete)