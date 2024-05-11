from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

clientes = { }
contador = 10
class HoliMundo(Resource):
    def get(self, cliente_id):
        return clientes[cliente_id]
    def put(self, cliente_id):
        clientes[cliente_id] = request.get_json()
    def delete(self, cliente_id):
        clientes.pop(cliente_id)

class HoliMundoSinId(Resource):
    def get(self):
        return clientes
    def post(self):
        json = request.get_json()
        clientes[json["id"]] = json
        return json["id"]
    
# GET localhost:5000/
# GET localhost:5000/5 --> "5" --> cliente_id
api.add_resource(HoliMundo, '/<string:cliente_id>')
api.add_resource(HoliMundoSinId, '/')

if __name__ == '__main__':
    app.run(debug=True)