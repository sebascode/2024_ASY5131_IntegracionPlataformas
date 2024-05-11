# Como usar

Generar dependencias:
```bash
pip freeze > requirements.txt
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```

Descargar y ejecutar:

```bash
# usando solo flask
flask --app miApi run --debug

# usando flask-restful 
python miNuevaApi.py
```