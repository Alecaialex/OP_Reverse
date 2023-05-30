import requests

#Introduce la ID y el puerto elegidos anteriormente
url = 'http://192.168.0.28:8000'

#Enviar solicitud POST con el texto "cerrar"
try:
    response = requests.post(url, data='cerrar')
    if response.status_code == 200:
        print("Solicitud de cierre enviada correctamente.")
    else:
        print("Error al enviar la solicitud de cierre.")
except requests.exceptions.RequestException as e:
    print("Error al enviar la solicitud al servidor:", str(e))
