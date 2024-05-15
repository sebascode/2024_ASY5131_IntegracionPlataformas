import requests

uri = " http://127.0.0.1:5000/cliente"

# creamos un cliente nuevo
r = requests.put(uri+"/10", json={ "nombre": "David", "Apellido": "Salamanca"   })

print("status: " + str(r.status_code))
print("text: " + r.text)
print(r.json())


# consultamos un cliente
resp = requests.get(uri)

print("status: " + str(resp.status_code))
print("text: " + resp.text)
print(resp.json())