import Banco_de_dados

# Usuários
Banco_de_dados.add_usuario('Gabriel', 'Joao Gabriel', 'gabrieloliveira_pb@hotmail.com', '24/05/1999', '500.00',
                           'gabriel')
Banco_de_dados.add_usuario('Messias', 'Joao Messias', 'joaomessias00@hotmail.com', '27/05/1999', '250.00', 'messias123')
Banco_de_dados.add_usuario('Igor', 'Igor barbosa', 'igor@ifpb.com', '04/04/2000', '1000.00', '1234')
Banco_de_dados.add_usuario('Lucas', 'Lucas Santos', 'lucas@gmail.com', '15/02/1998', '500.00', 'luc321')

# Bots
Banco_de_dados.add_bots('Super Favorito', '5', '1.0', '2.3', '0', '10', '2', '99', '55', '99', '1', 'favapo', 'favesta',
                        'Gabriel')
Banco_de_dados.add_bots('Zebra Bem', '5', '2.1', '4.0', '5', '15', '4', '99', '53', '99', '1', 'zebraapo', 'zebraesta',
                        'Messias')
Banco_de_dados.add_bots('Favorito Amassando', '10', '1.8', '5.0', '45', '70', '15', '99', '65', '99', '1', 'favapo',
                        'favapo', 'Gabriel')
Banco_de_dados.add_bots('Zebra Mal', '10', '1.4', '2.7', '35', '55', '0', '2', '0', '40', '1', 'favapo', 'zebraesta',
                        'Messias')
Banco_de_dados.add_bots('Casa com Muita Chance', '10', '1.0', '2.5', '0', '45', '10', '99', '60', '99', '1', 'casaapo',
                        'casaesta', 'Messias')
Banco_de_dados.add_bots('Fora Mal', '7.5', '1.7', '2.5', '15', '30', '0', '0', '0', '37', '1', 'casaapo', 'foraesta',
                        'Igor')
Banco_de_dados.add_bots('Fora Bem', '2.5', '1.8', '5.0', '20', '45', '8', '99', '58', '99', '1', 'foraapo', 'foraesta',
                        'Igor')
Banco_de_dados.add_bots('Favorito Mal', '5', '2.5', '4.5', '55', '80', '0', '5', '0', '50', '1', 'zebraapo', 'favesta',
                        'Gabriel')
Banco_de_dados.add_bots('Casa Mal', '7.5', '2.5', '4.0', '35', '80', '0', '3', '0', '40', '1', 'foraapo', 'casaesta',
                        'Messias')
Banco_de_dados.add_bots('Zebra Melhor', '2.5', '3.0', '6.0', '60', '85', '17', '99', '60', '99', '1', 'zebraapo',
                        'zebraesta', 'Igor')
Banco_de_dados.add_bots('Sempre Favorito', '5', '1.35', '2.8', '0', '10', '1', '99', '55', '99', '1', 'favapo',
                        'favesta', 'Lucas')
Banco_de_dados.add_bots('Sempre Zebra', '2.5', '2.85', '4.8', '0', '10', '1', '99', '55', '99', '1', 'zebraapo',
                        'zebraesta', 'Lucas')
Banco_de_dados.add_bots('Começo Bom do Favorito', '5', '1', '1.99', '0', '20', '4', '99', '65', '99', '1', 'favapo',
                        'favesta', 'Gabriel')
Banco_de_dados.add_bots('Zebra Iniciou Melhor', '2.5', '2', '3.5', '0', '20', '6', '99', '65', '99', '1', 'zebraapo',
                        'zebraesta', 'Gabriel')
Banco_de_dados.add_bots('Super Favorito', '10', '1.0', '1.5', '0', '20', '0', '1', '0', '40', '1', 'favapo',
                        'zebraesta', 'Lucas')

# Relatorio dos Bots
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '1', '1', 'Super Favorito')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '2', '2', 'Zebra Bem')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '3', '1', 'Favorito Amassando')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '4', '2', 'Zebra Mal')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '5', '2', 'Casa com Muita Chance')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '6', '3', 'Fora Mal')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '7', '3', 'Fora Bem')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '8', '1', 'Favorito Mal')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '9', '2', 'Casa Mal')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '10', '3', 'Zebra Melhor')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '11', '4', 'Sempre Favorito')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '12', '4', 'Sempre Zebra')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '13', '1', 'Começo Bom do Favorito')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '14', '1', 'Zebra Jogando Melhor')
Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, '15', '4', 'Super Favorito')

# Jogos Ao Vivo
# Banco_de_dados.add_jogos('BRASIL: Campeonato Brasileiro ', 'nion4234', 'Atlético-MG', 0, 'Cuiabá', 0, 5,
#                                 '24.04.2022 19:30', 70, 30, 2, 0, 1.3, 3.9, 8.0, 'aberto')
# Banco_de_dados.add_jogos('BRASIL: Campeonato Brasileiro ', 'plewmn45', 'Flamengo', 1, 'Avaí', 0, 9,
#                                 '17.04.2022 19:30', 65, 35, 3, 0, 1.15, 5.5, 12.0, 'aberto')
# Banco_de_dados.add_jogos('BRASIL: Campeonato Brasileiro ', 'qdwno453', 'Corinthians', 0, 'Vasco', 0, 14,
#                                 '17.04.2022 19:30', 45, 55, 2, 4, 2.1, 2.8, 3.6, 'aberto')
# Banco_de_dados.add_jogos('BRASIL: Campeonato Brasileiro ', 'nfoasnfw', 'Flamengo', 3, 'São Paulo', 1, 45,
#                                 '19.04.2022 19:30', 60, 40, 7, 2, 1.8, 2.8, 4.0, 'aberto')
# Banco_de_dados.add_jogos('BRASIL: Copa do Brasil ', 'okpasjg', 'Flamengo', 7, 'Campinense', 1, 30,
#                                 '19.04.2022 19:30', 80, 20, 16, 1, 1.05, 8.0, 17.0, 'aberto')
# Banco_de_dados.add_jogos('AMERICA: Copa America ', 'opfjea', 'Argentina', 0, 'Peru', 0, 35, '19.04.2022 19:30',
#                                 40, 60, 2, 3, 1.4, 2.9, 5.2, 'aberto')
# Banco_de_dados.add_jogos('EUROPA: Liga dos Campeões ', 'oihfd4f', 'Barcelona', 0, 'Bayern', 2, 20,
#                                 '19.04.2022 19:30', 48, 52, 2, 3, 2.1, 2.8, 3.1, 'aberto')
# Banco_de_dados.add_jogos('MUNDO: Copa do Mundo ', 'agadgadg', 'Brasil', 2, 'Alemanha', 0, 40, '19.04.2022 19:30',
#                                 40, 60, 2, 1, 2.6, 3.0, 2.4, 'aberto')
# Banco_de_dados.add_jogos('MUNDO: Copa do Mundo ', 'gag6433g', 'Japão', 2, 'Alemanha', 2, 85, '19.04.2022 19:30',
#                                 55, 45, 3, 10, 4.5, 1.5, 1.9, 'aberto')
# Banco_de_dados.add_jogos('MUNDO: Copa do Mundo ', 'pjp431oj', 'Espanha', 0, 'Gales', 0, 60, '19.04.2022 19:30',
#                                 40, 60, 7, 4, 2.0, 1.9, 3.4, 'aberto')
# Banco_de_dados.add_jogos('BRASIL: Campeonato Brasileiro ', 'dafag4g35', 'Flamengo', 0, 'Palmeiras', 0, 45,
#                                 '20.04.2022 20:00', 52, 48, 9, 7, 2.5, 1.9, 4.9, 'aberto')
# Banco_de_dados.add_jogos('BRASIL: Copa do Brasil ', 'pou32894', 'Juventude', 2, 'São Paulo', 0, 35,
#                                 '20.04.2022 19:30', 38, 62, 5, 4, 3.2, 2.8, 2.1, 'aberto')
# Banco_de_dados.add_jogos('BRASIL: Copa do Brasil ', 'poj4923o', 'Atletico-MG', 3, 'Brasiliense', 0, 40,
#                                 '20.04.2022 19:30', 82, 18, 14, 0, 1.1, 8.0, 17.0, 'aberto')
# Banco_de_dados.add_jogos('INGLATERRA: Campeonato Inglês ', 'amoa4134', 'Chelsea', 2, 'Arsenal', 2, 35,
#                                 '20.04.2022 15:45', 60, 40, 6, 8, 2.3, 1.7, 5.5, 'aberto')
# Banco_de_dados.add_jogos('INGLATERRA: Campeonato Inglês ', 'y5892hr9', 'Manchester City', 0, 'Brighton', 0, 50,
#                                 '20.04.2022 16:00', 67, 33, 8, 0, 1.5, 3.0, 8.0, 'aberto')
# Banco_de_dados.add_jogos('ESPANHA: Campeonato Espanhol ', 'op43j5p', 'Osasuna', 1, 'Real Madrid', 2, 75,
#                                 '20.04.2022 16:30', 35, 65, 10, 17, 11.0, 4.0, 1.3, 'aberto')
# Banco_de_dados.add_jogos('ESPANHA: Campeonato Espanhol ', '2opr2fd', 'Barcelona', 0, 'Girona', 0, 60,
#                                 '17.04.2022 16:30', 70, 30, 17, 3, 2.6, 5.0, 13.0, 'aberto')
# Banco_de_dados.add_jogos('ALEMANHA: Campeonato Alemão ', '13pot3p', 'Bayern', 0, 'Red Bull', 0, 50,
#                                 '17.04.2022 16:30', 66, 34, 12, 1, 1.7, 3.4, 8.0, 'aberto')
# Banco_de_dados.add_jogos('FRANÇA: Campeonato Frances ', '7m43osk', 'Strasbourg', 1, 'Rennais', 1, 75,
#                                 '20.04.2022 16:00', 37, 63, 8, 18, 3.95, 1.9, 4.75, 'aberto')
# Banco_de_dados.add_jogos('ITALIA: Campeonato Italiano ', 'pok690j', 'Juventus', 0, 'Inter', 0, 45,
#                                 '20.04.2022 16:00', 39, 61, 2, 8, 3.2, 2.1, 3.5, 'aberto')
# Banco_de_dados.add_jogos('Alemanha: Campeonato Alemão ', '22re89b', 'Leipzig', 0, 'Frankfurt', 0, 15,
#                          '22.04.2022 14:00', 62, 38, 2, 0, 1.45, 3.8, 6.0, 'aberto')
# Banco_de_dados.add_jogos('EUROPA: Liga dos Campeões ', 'dad265w', 'Real Madrid', 0, 'Leverkusen', 0, 5,
#                          '22.04.2022 16:00', 65, 35, 3, 0, 1.3, 4.1, 8.3, 'aberto')