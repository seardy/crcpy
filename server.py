import socket

from utilities import crc

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #servere crea el serverocket tcp
server.bind(('192.168.0.6',9999))

server.listen(1)

client, client_addr = server.accept()

print('Se ha conectado el host: ', client_addr)

data = client.recv(1024)

data = data.decode()

print('Recibido: ' , data)


msg, gen, crc_code = data.split(' ')

result = crc(msg, gen, crc_code)

print ('Checksum result: ' ,result)

result = int(result)

if(result != 0):
	response = 'Error, please send it again!'
else:
	response = 'Ok'


client.send(response.encode())

client.close()

server.close()