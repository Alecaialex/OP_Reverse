import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

CARPETA_DESTINO = os.path.abspath(os.path.join(os.path.dirname(__file__), 'loot'))

class ManejadorPeticiones(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        nombre_archivo = form['file'].filename if 'file' in form else 'archivo_desconocido'
        
        ruta_archivo = os.path.join(CARPETA_DESTINO, nombre_archivo)
        with open(ruta_archivo, 'wb') as archivo:
            archivo.write(form['file'].file.read())
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Archivo subido correctamente.')

def run_server():
    direccion_servidor = ('192.168.0.39', 8080)
    httpd = HTTPServer(direccion_servidor, ManejadorPeticiones)
    print(f"Servidor en {direccion_servidor[0]}:{direccion_servidor[1]}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
