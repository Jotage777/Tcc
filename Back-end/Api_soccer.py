from flask import Flask, request
from flask_restful import Resource,Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWord(Resource):
    def get(self):
        return {"data":"Hello Word"}
class Greenzord(Resource):
    def get(self,tipo,id):
        if tipo == 1:
        elif tipo == 2:
        elif tipo ==3:
        elif tipo == 4:
        elif tipo == 5:
        elif tipo == 6:
        elif tipo == 7:
    def post(self, tipo, id):
        if tipo == 1:
        elif tipo == 2:
        elif tipo == 3:
        elif tipo == 4:
        elif tipo == 5:
        elif tipo == 6:
        elif tipo == 7:
    def delete(self, tipo, id):
        if tipo == 1:
        elif tipo == 2:
        elif tipo == 3:
        elif tipo == 4:
        elif tipo == 5:
        elif tipo == 6:
        elif tipo == 7:

api.add_resource(HelloWord,"/helloword")
api.add_resource(Greenzord,"/greenzord/<int:tipo>/<int:id>")
if __name__=="__main__":
    app.run(debug= True)
