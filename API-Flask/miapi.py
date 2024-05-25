from flask import Flask, request

app = Flask(__name__)

## APP de Prueba para API Cliente

listaCliente = []

@app.get("/cliente")
def getClientes():
    return listaCliente

### GET "localhost:5000/cliente/5"

@app.get("/cliente/<id>")
def getCliente(id):
    return listaCliente.index(id)

@app.post("/cliente")
def insertaCliente():
    json = request.get_json()
    
    cliente = {
        "id": json["id"],
        "razonSocial": json["nombre"],
        "rut": json["rut"],
        "direccion": json["direccion"] 
    }
    print(cliente)

    listaCliente.append(cliente)
    return ""

@app.put("/cliente/<id>")
def actualizaCliente(id):
    json = request.get_json()
    
    cliente = {
        "id": json["id"],
        "razonSocial": json["nombre"],
        "rut": json["rut"],
        "direccion": json["direccion"] 
    }
    listaCliente.pop(id)
    listaCliente.append(cliente)

    return ""

@app.delete("/cliente")
def borrarCliente():
    listaCliente.pop(id)
    return ""