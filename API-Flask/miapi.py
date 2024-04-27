from flask import Flask

app = Flask(__name__)

## APP de Prueba para API Cliente

@app.get("/cliente")
def getClientes():
    return "<h1>hola cliente</h1>"

### GET "localhost:5000/cliente/5"

@app.get("/cliente/<id>")
def getCliente(id):
    return "<h1>Hola cliente, has seleccionado "+ id +"</h1>"

@app.post("/cliente")
def insertaCliente():
    return 0

@app.put("/cliente")
def actualizaCliente():
    return 0

@app.delete("/cliente")
def borrarCliente():
    return 0