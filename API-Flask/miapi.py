from flask import Flask, request

app = Flask(__name__)

# CRUD de Cliente guardado en una lista estática

lista = []

@app.get("/cliente")
def getClientes():
    return lista

@app.get("/cliente/<id>")
def getCliente(id):
    return lista[int(id)]

@app.post("/cliente")
def postCliente():
    json = request.get_json()
    lista.append(json)
    return ""

@app.put("/cliente/<id>")
def putCliente(id):
    json = request.get_json()
    lista.pop(int(id))
    lista.append(json)
    return ""

@app.delete("/cliente/<id>")
def deleteCliente(id:int):
    lista.pop(int(id))
    return ""