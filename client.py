import socket
from utilities import crc

sock = socket.socket()
sock.connect(('127.0.0.1',9999))

data = input('Ingrese un mensaje: ')
generator = input('Ingrese el generador: ')

crc_code = crc(data,generator)

request = data + ' ' + generator + ' '+ crc_code
sock.send(request.encode())

response = sock.recv(1024)
print(response.decode())

sock.close()