from flask import Flask

app = Flask(__name__)

# CRUD de Cliente guardado en una lista estática

lista = []

@app.get("/cliente")
def getClientes():
    return lista

@app.get("/cliente/<id>")
def getCliente(id):
    return id

@app.post("/cliente")
def postCliente():
    return 0

@app.put("/cliente/<id>")
def putCliente(id):
    return 0

@app.delete("/cliente/<id>")
def deleteCliente(id):
    return 0