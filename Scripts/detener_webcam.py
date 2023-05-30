import requests

#Introduce la ID y el puerto elegidos anteriormente
url = 'http://192.168.0.28:8000'

#Enviar solicitud POST con el texto "cerrar"
response = requests.post(url, data='cerrar')
print("Solicitud enviada")