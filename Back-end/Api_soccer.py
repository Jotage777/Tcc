import os

from flask import Flask, request
from flask_restful import Resource, Api
import Banco_de_dados
import Web_scraping
import Apostar


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Greenzord.db'


class Greenzord(Resource):
    def get(self, tipo, tipo2, nome):
        if tipo == 1:
            informacoes = Banco_de_dados.consultas("SELECT * FROM Campeonato")
            if tipo2 == 1:
                for i in range(len(informacoes)):
                    if informacoes[i][1] == nome:
                        campeonato = informacoes[i]
                        return campeonato
            elif tipo2 == 2:
                for i in range(len(informacoes)):
                    if informacoes[i][1] == nome:
                        id = informacoes[i][0]
                        return id

        elif tipo == 2:
            informacoes = Banco_de_dados.consultas("SELECT * FROM Times")
            if tipo2 == 1:
                for i in range(len(informacoes)):
                    if informacoes[i][1] == nome:
                        time = informacoes[i]
                        return time
            elif tipo2 == 2:
                for i in range(len(informacoes)):
                    if informacoes[i][1] == nome:
                        id = informacoes[i][0]
                        return id

        elif tipo == 3:
            informacoes = Banco_de_dados.consultas_jogos('aberto')
            if tipo2 == 1:
                return informacoes
            elif tipo2 == 2:
                Web_scraping.WebScraping()
                return 200

        elif tipo == 4:
            informacoes = Banco_de_dados.consultas("SELECT * FROM Usuario")
            if tipo2 == 1:
                for i in range(len(informacoes)):
                    if informacoes[i][1] == nome:
                        usuario = informacoes[i]
                        return usuario
            elif tipo2 == 2:
                for i in range(len(informacoes)):
                    if informacoes[i][1] == nome:
                        id = informacoes[i][0]
                        return id
            elif tipo2 == 3:
                saldo = Banco_de_dados.consultar_usuario_saldo(nome)
                return saldo

        elif tipo == 5:
            bots = []
            index = 0
            informacoes = Banco_de_dados.consultas("SELECT * FROM Bots")
            if tipo2 == 1:
                for i in range(len(informacoes)):
                    if informacoes[i][-1] == int(nome):
                        index += 1
                        bots.insert(index, informacoes[i])
                return bots
            elif tipo2 == 2:
                for i in range(len(informacoes)):
                    if informacoes[i][0] == int(nome):
                        bot = informacoes[i]
                        return bot
                return 0

        elif tipo == 6:
            # falta configurar
            informacoes = Banco_de_dados.consultas("SELECT * FROM Apostas")
            if tipo2 == 1:
                for i in range(len(informacoes)):
                    if informacoes[i][1] == nome:
                        usuario = informacoes[i]
                        return usuario
            elif tipo2 == 2:
                for i in range(len(informacoes)):
                    if informacoes[i][0] == nome:
                        id = informacoes[i][0]
                        return id
            for i in informacoes:
                if informacoes[i][0] == id:
                    apostas = informacoes[i]
                    return apostas

        elif tipo == 7:
            informacoes = Banco_de_dados.consultas("SELECT * FROM Relatorio")
            if tipo2 == 1:
                for i in range(len(informacoes)):
                    if informacoes[i][-1] == int(nome):
                        relatorio = informacoes[i]
                        return relatorio
            elif tipo2 == 2:
                for i in range(len(informacoes)):
                    if informacoes[i][-1] == int(nome):
                        id = informacoes[i][0]
                        return id

        else:
            return {"Opcao invalida"}


class Greenzord_jogos(Resource):
    def get(self):
        Web_scraping.WebScraping()


class Greenzord_bots(Resource):
    def post(self):
        Banco_de_dados.add_bots(request.json['nome'], float(request.json['responsabilidade']),
                                float(request.json['odd_minima']), float(request.json['odd_maxima']),
                                int(request.json['tempo_jogo_minimo']), int(request.json['tempo_jogo_maximo']),
                                int(request.json['finalizacao_min']), int(request.json['finalizacao_max']),
                                int(request.json['posse_bola_min']), int(request.json['posse_bola_max']),
                                bool(request.json['ativado']), request.json['apostar'], request.json['analisar'],
                                request.json['username'])
        id_bot = Banco_de_dados.consultar_bots(request.json['nome'])
        id_usuario = Banco_de_dados.consultar_usuario(request.json['username'])
        Banco_de_dados.add_relatorio(0, 0, 0.0, 0, 0, id_bot, id_usuario, request.json['nome'])
        return 200


class Greenzord_bots_editar(Resource):
    def post(self, tipo,id):
        if tipo ==1:
            Banco_de_dados.atulizar_bots(request.json['nome'], id, 1)
            Banco_de_dados.atulizar_bots(float(request.json['responsabilidade']), id, 2)
            Banco_de_dados.atulizar_bots(float(request.json['odd_minima']), id, 3)
            Banco_de_dados.atulizar_bots(float(request.json['odd_maxima']), id, 4)
            Banco_de_dados.atulizar_bots(int(request.json['tempo_jogo_minimo']), id, 5)
            Banco_de_dados.atulizar_bots(int(request.json['tempo_jogo_maximo']), id, 6)
            Banco_de_dados.atulizar_bots(int(request.json['finalizacao_min']), id, 7)
            Banco_de_dados.atulizar_bots(int(request.json['finalizacao_max']), id, 8)
            Banco_de_dados.atulizar_bots(int(request.json['posse_bola_min']), id, 9)
            Banco_de_dados.atulizar_bots(int(request.json['posse_bola_max']), id, 10)
            Banco_de_dados.atulizar_bots(bool(request.json['ativado']), id, 11)
            Banco_de_dados.atulizar_bots(request.json['apostar'], id, 12)
            Banco_de_dados.atulizar_bots(request.json['analisar'], id, 13)
            return 200
        if tipo ==2:
            print('entrou')
            if request.json['ativado'] == '1':
                Banco_de_dados.atulizar_bots(1, id, 11)
            if request.json['ativado'] =='0':
                Banco_de_dados.atulizar_bots(0, id, 11)


class Greenzord_apagar_bots(Resource):
    def get(self, id):
        Banco_de_dados.deletar_bot(id)
        return 200


class Greenzord_Login_Cadastro(Resource):
    def get(self):
        validar = Banco_de_dados.consultar_login(request.json['username'], request.json['password'])

        return validar

    def post(self):
        Banco_de_dados.add_usuario(request.json['username'], request.json['nome'], request.json['email'],
                                   request.json['data_nascimento'],
                                   float(request.json['saldo']), request.json['senha'])
        return 200


class Greenzord_realizar_apostas(Resource):
    def get(self):
        Apostar.analise()
        return 200


class Greenzord_apostas_bot(Resource):
    def get(self, id, tipo):
        if tipo == 1:
            apostas = Banco_de_dados.consultar_aposta_bot(id, 1)
            return apostas
        elif tipo == 2:
            apostas = Banco_de_dados.consultar_aposta_bot(id, 2)
            return apostas


class Greenzord_relatorio(Resource):
    def get(self, id, tipo):
        if tipo == 1:
            relatorio = Banco_de_dados.consultar_relatorio(id)
            return relatorio
        if tipo == 2:
            relatorio = Banco_de_dados.consultar_relatorio_usuario(id)
            return relatorio


api.add_resource(Greenzord, "/greenzord/<int:tipo>/<int:tipo2>/<string:nome>")
api.add_resource(Greenzord_jogos, "/greenzord/jogos")
api.add_resource(Greenzord_bots, "/greenzord/bots")
api.add_resource(Greenzord_apagar_bots, "/greenzord/bots/deletar/<int:id>")
api.add_resource(Greenzord_bots_editar, "/greenzord/bots/editar/<int:tipo>/<int:id>")
api.add_resource(Greenzord_Login_Cadastro, "/greenzord/login_cadastro")
api.add_resource(Greenzord_realizar_apostas, "/greenzord/apostar")
api.add_resource(Greenzord_apostas_bot, "/greenzord/apostas/bot/<int:id>/<int:tipo>")
api.add_resource(Greenzord_relatorio, "/greenzord/relatorio/<int:tipo>/<int:id>")
create_db = not os.path.isfile('Greenzord.db')

if create_db:
    Banco_de_dados.criar_BD()
if __name__ == "__main__":
    app.run(debug=True)
