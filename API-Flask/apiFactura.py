from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

url_cliente = "http://localhost:5000/api/cliente"

## POST localhost:port/api/boleta 
## > body: json > { id_producto, cantidad, id_cliente }
## new Factura() -> #3ag32g45 --> Factura{ }
class Factura(Resource):
    def post(self):
        # definimos un objeto para la respuesta de la boleta
        objRespuesta = {
            "id_producto": 0,
            "precio": 0,
            "cantidad": 0,
            "total_venta": 0,
            "id_cliente": 0,
            "nombre_cliente": "",
            "direccion_cliente": ""
        }

        # capturamos el json que nos llega
        json = request.get_json()

        # generamos una nueva consulta hacia el api de cliente
        cliente_response = requests.get(url_cliente+"/"+ str(json["id_cliente"]))
        print(cliente_response.status_code)
        if(cliente_response.status_code == 200):
            cliente_json = cliente_response.json()

            objRespuesta["id_cliente"] = cliente_json["id"]
            objRespuesta["nombre_cliente"] = cliente_json["razonSocial"]
            objRespuesta["direccion_cliente"] = cliente_json["direccion"]
            objRespuesta["id_producto"] = json["producto_id"]
            objRespuesta["cantidad"] = json["cantidad"]
            objRespuesta["precio"] = 500
            objRespuesta["total_venta"] = objRespuesta["precio"] * json["cantidad"]

        return objRespuesta
    
api.add_resource(Factura, "/api/boleta")

app.run(debug=True, port=5001)