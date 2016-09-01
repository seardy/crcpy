import socket
from crc import CrcUtilities

sock = socket.socket()
sock.connect(('127.0.0.1',9999))
calculator = CrcUtilities()

data = input('Ingrese un mensaje: ')
msg = calculator.toBinary(data)
generator = input('Ingrese el generador: ')

crc_code = calculator.crc(msg,generator)

data_raw = msg + ' ' + generator + ' '+ crc_code
sock.send(data_raw.encode())

response = sock.recv(1024)
print(response.decode())
sock.close()