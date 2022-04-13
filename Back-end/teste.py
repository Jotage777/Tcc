import Banco_de_dados
import Web_scraping

Banco_de_dados.add_usuario('Gabriel', 'Joao Gabriel de Oliveira Ponciano', 'gabrieloliveira_pb@hotmail.com',
                           '24/05/1999', '200.00')
Banco_de_dados.add_usuario('Messias', 'Joao Messias da Silva Medeiros', 'joaomessias00@hotmail.com', '27/05/1999',
                           '500.00')
Banco_de_dados.add_usuario('Igor', 'Igor barbosa', 'igor@ifpb.com', '04/04/2000', '1000.00')

Banco_de_dados.add_bots('bot1g', '1', '1.2', '2.0', '0', '50', '5', '99', '55', '99', '1', 'favapo', 'favesta',
                        'Gabriel')
Banco_de_dados.add_bots('bot2m', '5', '1.8', '2.9', '15', '60', '0', '2', '0', '40', '1', 'favapo', 'zebraesta',
                        'Messias')
Banco_de_dados.add_bots('bot3g', '2', '2.2', '5.0', '15', '30', '1', '99', '60', '99', '1', 'foraesta', 'foraesta',
                        'Gabriel')
Banco_de_dados.add_bots('bot4m', '10', '2.8', '3.9', '10', '50', '0', '1', '50', '70', '1', 'favapo', 'zebraesta',
                        'Messias')
Banco_de_dados.add_bots('bot5m', '2.5', '1.2', '2.5', '5', '40', '0', '10', '55', '99', '1', 'favapo', 'favesta',
                        'Messias')
Banco_de_dados.add_bots('bot6i', '5', '1.1', '2.6', '0', '25', '5', '99', '0', '35', '1', 'casaapo', 'foraesta', 'Igor')

Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '1')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '2')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '3')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '4')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '5')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, '6')

Web_scraping.WebScraping()

# estatisticas=['h8dml01n', 'França F', 'Eslovénia F', '12.04.2022 16:10', 'EUROPA: Copa do Mundo de Futebol Feminino ', '0', '1', '0', '0', '0', '0', '1.03', '13.00', '36.00']
# ('n3F6bzD0', 'U. Católica (Chi)', 'AMÉRICA DO SUL: Copa Libertadores ', 'Sporting Cristal (Per)', 1, 0, 46, '12.04.2022 19:15', 48, 52, 2, 0, 1.55, 6.0, 4.2, 8)
# Banco_de_dados.add_jogos_aovivo(estatisticas[4], estatisticas[0], estatisticas[1], int(estatisticas[6]),
#                                 estatisticas[2], int(estatisticas[7]), int(estatisticas[5]), estatisticas[3],
#                                 int(estatisticas[8]), int(estatisticas[9]), int(estatisticas[10]),
#                                 int(estatisticas[11]), float(estatisticas[12]), float(estatisticas[13]),
#                                 float(estatisticas[14]))

# delete = "DELETE FROM Bots WHERE id_bot = 1"
# delete = "DELETE FROM Usuario WHERE id_usuario = 1"
# Banco_de_dados.deletar(delete)