
import socket
import xml.etree.ElementTree as ET
from lxml import etree

def recibir_mensaje(ip_receptor, puerto_receptor):
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar el socket a una dirección y puerto específicos
    server_address = (ip_receptor, puerto_receptor)
    sock.bind(server_address)

    # Escuchar las conexiones entrantes
    sock.listen(1)

    print("Esperando conexión...")

    while True:
        # Esperar una conexión
        connection, client_address = sock.accept()

        try:
            print("Conexión establecida desde:", client_address)

            # Recibir los datos en trozos y rearmarlos
            data = ""
            while True:
                chunk = connection.recv(16).decode('utf-8')
                if not chunk:
                    break
                data += chunk

            print("Mensaje XML recibido:\n", data)

            # Validar el XML con un DTD personalizado
            dtd = """
            <!ELEMENT empleados (empleado)>
            <!ELEMENT empleado (nombre, apellido)>
            <!ELEMENT nombre (#PCDATA)>
            <!ELEMENT apellido (#PCDATA)>
            """

            try:
                # Analizar el XML
                parsed_xml = ET.fromstring(data)

                # Crear un objeto parser para el DTD
                dtd_parser = etree.DTD(etree.fromstring(dtd))

                # Validar el XML con el DTD
                if dtd_parser.validate(parsed_xml):
                    print("XML válido según el DTD")
                else:
                    print("XML no válido según el DTD")

            except Exception as e:
                print("Error al validar el XML:", str(e))

        finally:
            # Cerrar la conexión
            connection.close()
            break

# Datos del receptor
ip_receptor = '192.168.1.35' #cambia esta IP por la del receptor 
puerto_receptor = 8080

# Llamar a la función para recibir el mensaje XML y validar con el DTD
recibir_mensaje(ip_receptor, puerto_receptor)