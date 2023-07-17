import xml.etree.ElementTree as ET


import socket

def enviar_mensaje(ip_destino, puerto_destino, mensaje):
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar el socket al puerto donde el receptor está escuchando
    server_address = (ip_destino, puerto_destino)
    sock.connect(server_address)

    try:
        # Enviar el mensaje
        sock.sendall(mensaje.encode('utf-8'))
        print("Mensaje enviado:", mensaje)

    finally:
        # Cerrar la conexión
        sock.close()

# Datos del receptor
ip_receptor = '192.168.1.35'
puerto_receptor = 8080

# Crear el mensaje XML
root = ET.Element("empleados")
empleado1 = ET.SubElement(root, "empleado")
nombre1 = ET.SubElement(empleado1, "nombre")
nombre1.text = "Juan"
apellido1 = ET.SubElement(empleado1, "apellido")
apellido1.text = "Pérez"
empleado2 = ET.SubElement(root, "empleado")
nombre2 = ET.SubElement(empleado2, "nombre")
nombre2.text = "María"
apellido2 = ET.SubElement(empleado2, "apellido")
apellido2.text = "López"

# Convertir el mensaje XML a una cadena
mensaje_xml = ET.tostring(root, encoding='utf-8', method='xml').decode()


# Llamar a la función para enviar el mensaje
enviar_mensaje(ip_receptor, puerto_receptor, mensaje_xml)