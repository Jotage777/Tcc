import os

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, abort, reqparse
import Banco_de_dados
import Web_scraping
from pydantic import BaseModel

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Greenzord.db'


class campeonato_modelo(BaseModel):
    nome: str


class times_modelo(BaseModel):
    nome: str


class jogos_modelo(BaseModel):
    campeonato: str
    id: str
    time_casa: str
    resultado_casa: str
    time_fora: str
    resultado_fora: str
    date: str
    odd_casa: str
    odd_fora: str
    odd_empate: str


class usuario_modelo(BaseModel):
    username: str
    nome: str
    email: str
    data_nascimento: str
    saldo: str


class bots_modelo(BaseModel):
    nome: str
    responsabilidade: str
    odd_minima: str
    odd_maxima: str
    tempo_jogo_maximo: str
    tempo_jogo_minimo: str
    finalizacao_min: str
    finalizacao_max: str
    posse_bola_min: str
    posse_bola_max: str
    ativado: str
    apostar: str
    analisar: str
    username: str


class apostas_modelo(BaseModel):
    mercado: str
    valor_apostado: str
    odd_aposta: str
    id_bot: str
    id_jogo: str


class relatorio_modelo(BaseModel):
    greens: str
    reds: str
    lucro: str
    total_apostas: str
    id_bot: str


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
            informacoes = Banco_de_dados.consultas("SELECT * FROM Jogos_AoVivo")
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

    # def put(self, tipo, id):
    #     if tipo == 1:
    #
    #     elif tipo == 2:
    #     elif tipo == 3:
    #     elif tipo == 4:
    #     elif tipo == 5:
    #     elif tipo == 6:
    #     elif tipo == 7:
    #     else:
    # return {"Opcao invalida"}

    def delete(self, tipo, id):
        if tipo == 1:
            convercao = str(id)
            acao = "DELETE FROM Campeonato WHERE id_campeonato =" + convercao
            Banco_de_dados.deletar(acao)
            return 200
        elif tipo == 2:
            convercao = str(id)
            acao = "DELETE FROM Times WHERE id_time =" + convercao
            Banco_de_dados.deletar(acao)
            return 200
        elif tipo == 3:
            convercao = str(id)
            acao = "DELETE FROM Jogos WHERE id_jogo =" + convercao
            Banco_de_dados.deletar(acao)
            return 200
        elif tipo == 4:
            convercao = str(id)
            acao = "DELETE FROM Usuario WHERE id_usuario =" + convercao
            Banco_de_dados.deletar(acao)
            return 200
        elif tipo == 5:
            convercao = str(id)
            acao = "DELETE FROM Bots WHERE id_bot =" + convercao
            Banco_de_dados.deletar(acao)
            return 200
        elif tipo == 6:
            convercao = str(id)
            acao = "DELETE FROM Apostas WHERE id_apostas =" + convercao
            Banco_de_dados.deletar(acao)
            return 200
        elif tipo == 7:
            convercao = str(id)
            acao = "DELETE FROM Relatorio WHERE id_relatorio =" + convercao
            Banco_de_dados.deletar(acao)
            return 200
        else:
            return {"Opcao invalida"}


class Greenzord_campeonato(Resource):
    def post(campeonato: campeonato_modelo):
        Banco_de_dados.add_campeonato(request.json['nome'])
        return 200


class Greenzord_times(Resource):
    def post(time: times_modelo):
        Banco_de_dados.add_times(request.json['nome'])
        return 200


class Greenzord_jogos(Resource):
    def get(id):
        Web_scraping.WebScraping()


class Greenzord_usuario(Resource):
    def post(usuario: usuario_modelo):
        Banco_de_dados.add_usuario(request.json['username'], request.json['nome'], request.json['email'],
                                   request.json['data_nascimento'],
                                   float(request.json['saldo']))
        return 200


class Greenzord_bots(Resource):
    def post(bots: bots_modelo):
        Banco_de_dados.add_bots(request.json['nome'], float(request.json['responsabilidade']),
                                float(request.json['odd_minima']), float(request.json['odd_maxima']),
                                int(request.json['tempo_jogo_minimo']), int(request.json['tempo_jogo_maximo']),
                                int(request.json['finalizacao_min']), int(request.json['finalizacao_max']),
                                int(request.json['posse_bola_min']), int(request.json['posse_bola_max']),
                                bool(request.json['ativado']), request.json['apostar'], request.json['analisar'],
                                request.json['username'])
        id_bot = Banco_de_dados.consultar_bots(request.json['nome'])
        Banco_de_dados.add_relatorio(0, 0, 0.0, 0, id_bot)
        return 200


class Greenzord_bots_editar(Resource):
    def post(bots: bots_modelo, id):
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


class Greenzord_apostas(Resource):
    def post(aposta: apostas_modelo):
        Banco_de_dados.add_apostas(request.json['mercado'], float(request.json['valor_apostado']),
                                   float(request.json['odd_aposta']), request.json['id_bot'], request.json['id_jogo'])
        return 200


class Greenzord_apagar_bots(Resource):
    def post(Self, id):
        print(id)
        Banco_de_dados.deletar_bot(id)
        return 200


api.add_resource(Greenzord, "/greenzord/<int:tipo>/<int:tipo2>/<string:nome>")
api.add_resource(Greenzord_campeonato, "/greenzord/campeonato")
api.add_resource(Greenzord_times, "/greenzord/times")
api.add_resource(Greenzord_jogos, "/greenzord/jogos/<int:id>")
api.add_resource(Greenzord_usuario, "/greenzord/usuario")
api.add_resource(Greenzord_bots, "/greenzord/bots")
api.add_resource(Greenzord_apostas, "/greenzord/apostas")
api.add_resource(Greenzord_apagar_bots, "/greenzord/bots/deletar/<int:id>")
api.add_resource(Greenzord_bots_editar, "/greenzord/bots/editar/<int:id>")
create_db = not os.path.isfile('Greenzord.db')
if create_db:
    Banco_de_dados.criar_BD()
if __name__ == "__main__":
    app.run(debug=True)

# http://127.0.0.1:5000
