from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

clientes = {}

class MiPrimeraApi(Resource):
    def get(self):
        print("Se ejecutó MIPrimeraAPI")
        #return { "cliente": { "nombre": "La sabroza ltda.", "direccion": "vicente huidobro #332, recoleta" } }
        return clientes
    def post(self):
        clientes = request.get_json()
        return True

class MiSegundaApi(Resource):
    def get(self, id):
        print("Se ejecutó MiSegundaAPI")
        #return { "cliente": { "id": id, "nombre": "La sabroza ltda.", "direccion": "vicente huidobro #332, recoleta" } } 
        return clientes[id]
    def put(self, id):
        clientes[id] = request.get_json()
        return True
    def delete(self, id):
        clientes[id].popitem()
        return True

# localhost:5000/cliente
api.add_resource(MiPrimeraApi, "/cliente/")

# localhost:5000/cliente/5
api.add_resource(MiSegundaApi, "/cliente/<string:id>")

app.run(debug=True)