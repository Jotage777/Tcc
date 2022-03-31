import os

from flask import Flask, request
from flask_restful import Resource,Api, abort, reqparse
import Banco_de_dados
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
    time_casa:str
    resultado_casa: int
    time_fora: str
    resultado_fora: int
    date: str
    odd_casa: float
    odd_fora: float
    odd_empate: float

class usuario_modelo(BaseModel):
    username: str
    nome: str
    email: str
    data_nascimento: str
    saldo: float

class bots_modelo(BaseModel):
    nome: str
    responsabilidade: float
    odd_minima: float
    odd_maxima: float
    tempo_jogo_max: int
    tempo_jogo_min: int
    finalizacao_casa: int
    finalizacao_fora: int
    posse_bola_casa: int
    posse_bola_fora: int
    ativado: bool
    casa_ou_fora: str
    username: str


class apostas_modelo(BaseModel):
    mercado:str
    valor_apostado: float
    odd_aposta: float
    id_bot:str
    id_jogo: str

class relatorio_modelo(BaseModel):
    greens: int
    reds: int
    lucro: int
    total_apostas: int
    id_bot: str


class Greenzord(Resource):
    def get(self, tipo, id):
        if tipo == 1:
            informacoes = Banco_de_dados.consultas("Campeonato")
            for i in informacoes:
                if informacoes[i][0] == id:
                    campeonato = informacoes[i]
                    return campeonato

        elif tipo == 2:
            informacoes = Banco_de_dados.consultas("Times")
            for i in informacoes:
                if informacoes[i][0] == id:
                    times = informacoes[i]
                    return times

        elif tipo == 3:
            informacoes = Banco_de_dados.consultas("Jogos")
            for i in informacoes:
                if informacoes[i][0] == id:
                    jogos = informacoes[i]
                    return jogos

        elif tipo == 4:
            informacoes = Banco_de_dados.consultas("Usuario")
            for i in informacoes:
                if informacoes[i][0] == id:
                    jogos = informacoes[i]
                    return jogos
        elif tipo == 5:
            informacoes = Banco_de_dados.consultas("Bots")
            for i in informacoes:
                if informacoes[i][0] == id:
                    bots = informacoes[i]
                    return bots

        elif tipo == 6:
            informacoes = Banco_de_dados.consultas("Apostas")
            for i in informacoes:
                if informacoes[i][0] == id:
                    apostas = informacoes[i]
                    return apostas
        elif tipo == 7:
            informacoes = Banco_de_dados.consultas("Relatorio")
            for i in informacoes:
                if informacoes[i][0] == id:
                    relatorio = informacoes[i]
                    return relatorio

        else:
            return {"Opcao invalida"}
     # def put(self, tipo, id):
        # if tipo == 1:

        # elif tipo == 2:
        # elif tipo == 3:
        # elif tipo == 4:
        # elif tipo == 5:
        # elif tipo == 6:
        # elif tipo == 7:
        # else:
        #     return {"Opcao invalida"}
    def delete(self, tipo, id):
        if tipo == 1:
            convercao = str(id)
            acao = "DELETE FROM Campeonato WHERE id_campeonato ="+convercao
            Banco_de_dados.deletar(acao)
            return {200}
        elif tipo == 2:
            convercao = str(id)
            acao = "DELETE FROM Times WHERE id_time =" +convercao
            Banco_de_dados.deletar(acao)
            return {200}
        elif tipo == 3:
            convercao = str(id)
            acao = "DELETE FROM Jogos WHERE id_jogo =" +convercao
            Banco_de_dados.deletar(acao)
            return {200}
        elif tipo == 4:
            convercao = str(id)
            acao = "DELETE FROM Usuario WHERE id_usuario =" +convercao
            Banco_de_dados.deletar(acao)
            return {200}
        elif tipo == 5:
            convercao = str(id)
            acao = "DELETE FROM Bots WHERE id_bot =" +convercao
            Banco_de_dados.deletar(acao)
            return {200}
        elif tipo == 6:
            convercao = str(id)
            acao = "DELETE FROM Apostas WHERE id_apostas =" +convercao
            Banco_de_dados.deletar(acao)
            return {200}
        elif tipo == 7:
            convercao = str(id)
            acao = "DELETE FROM Relatorio WHERE id_relatorio =" +convercao
            Banco_de_dados.deletar(acao)
            return {200}
        else:
            return {"Opcao invalida"}
class Greenzord_campeonato(Resource):
    def post(campeonato: campeonato_modelo):
        Banco_de_dados.add_campeonato(campeonato.nome )
        return {"Campeonato:"+campeonato.nome +"Cadastrado com sucesso"}

class Greenzord_times(Resource):
    def post(time:times_modelo):
        Banco_de_dados.add_times(time.nome)
        return {"Time:"+time.nome + "Cadastrado com sucesso"}

class Greenzord_jogos(Resource):
    def post(jogos: jogos_modelo):
        Banco_de_dados.add_jogos(jogos.campeonato,jogos.id,jogos.time_casa,jogos.resultado_casa,jogos.time_fora,jogos.resultado_fora,jogos.date,jogos.odd_casa,jogos.odd_fora,jogos.odd_empate)
        return {"Jogo:"+jogos.id + "Cadastrado com sucesso"}
class Greenzord_usuario(Resource):
    def post(usuario: usuario_modelo):
        Banco_de_dados.add_usuario(usuario.username,usuario.nome,usuario.email,usuario.data_nascimento,usuario.saldo)
        return {"Usuario:"+usuario.nome+"cadastrado com sucesso"}
class Greenzord_bots(Resource):
    def post(bots: bots_modelo):
        Banco_de_dados.add_bots(bots.nome,bots.responsabilidade,bots.odd_minima,bots.odd_maxima,bots.tempo_jogo_min,bots.tempo_jogo_max,bots.finalizacao_casa,bots.finalizacao_fora,bots.posse_bola_casa,
                                bots.posse_bola_fora,bots.ativado,bots.casa_ou_fora,bots.username)
        return {"Bot:"+bots.nome+"cadastrado com sucesso"}
class Greenzord_apostas(Resource):
    def post(aposta: apostas_modelo):
        Banco_de_dados.add_apostas(aposta.mercado,aposta.valor_apostado,aposta.odd_aposta,aposta.id_bot,aposta.id_jogo)
        return {"Aposta realizada com sucesso!"}
class Greenzord_relatorio(Resource):
    def post(relatorio: relatorio_modelo):
        Banco_de_dados.add_relatorio(relatorio.greens,relatorio.reds,relatorio.lucro,relatorio.total_apostas,relatorio.id_bot)
        return {"Relatorio cadastrado com sucesso"}
api.add_resource(Greenzord,"/greenzord/<int:tipo>/<int:id>")
api.add_resource(Greenzord_campeonato,"/greenzord/campeonato")
api.add_resource(Greenzord_times,"/greenzord/times")
api.add_resource(Greenzord_jogos,"/greenzord/jogos")
api.add_resource(Greenzord_usuario,"/greenzord/usuario")
api.add_resource(Greenzord_bots,"/greenzord/bots")
api.add_resource(Greenzord_apostas,"/greenzord/apostas")
api.add_resource(Greenzord_relatorio,"/greenzord/relatorio")

create_db = not os.path.isfile('Greenzord.db')
if create_db:
  Banco_de_dados.criar_BD()
if __name__=="__main__":
    app.run(debug= True)
