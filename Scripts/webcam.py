import cv2
from flask import Flask, render_template, Response, request
import threading
import os

# Indicar el puerto para el servidor web
puerto = 8000

app = Flask(__name__)
camera = cv2.VideoCapture(0)

cerrar_servidor = False

def video_stream():
    while True:
        if cerrar_servidor:
            break

        ret, frame = camera.read()

        if not ret:
            print("No se pudo obtener el frame de la webcam.")
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

def cerrar_servidor_flask():
    global cerrar_servidor
    while True:
        if cerrar_servidor:
            os._exit(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/', methods=['POST'])
def recibir_solicitud():
    global cerrar_servidor
    texto = request.data.decode('utf-8')
    if texto.strip() == "cerrar":
        cerrar_servidor = True
        return 'Servidor cerrado correctamente.'
    else:
        return 'Solicitud no válida.'

if __name__ == '__main__':
    threading.Thread(target=cerrar_servidor_flask).start()

    app.run(host='0.0.0.0', port=puerto, debug=False)
