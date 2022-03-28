from flask import Flask, request
from flask_restful import Resource,Api, abort, reqparse
import Banco_de_dados
app = Flask(__name__)
api = Api(app)

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
    def post(self, tipo, id):
        if tipo == 1:

        elif tipo == 2:
        elif tipo == 3:
        elif tipo == 4:
        elif tipo == 5:
        elif tipo == 6:
        elif tipo == 7:
        else:
            return {"Opcao invalida"}
    def delete(self, tipo, id):
        if tipo == 1:
        elif tipo == 2:
        elif tipo == 3:
        elif tipo == 4:
        elif tipo == 5:
        elif tipo == 6:
        elif tipo == 7:
        else:
            return {"Opcao invalida"}


api.add_resource(Greenzord,"/greenzord/<int:tipo>/<int:id>")
if __name__=="__main__":
    app.run(debug= True)
