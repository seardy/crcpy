import socket
from utilities import crc

# socket requirements
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(('127.0.0.1',9999))
server.listen(1)

#while True:	
# when a client is connected
client, client_addr = server.accept()
print('Device connected: ', client_addr)
data = client.recv(1024)
data = data.decode()
print('Received: ' , data)

#split received message
msg, gen, crc_code = data.split(' ')

# calculate the crc checksum of data received
result = crc(msg, gen, crc_code)

# show the crc_code
print ('Checksum result: ' ,result)

# parse the string of result to an int.
result = int(result)

# if checksum is not 0  then there was a transmission bit error.
if result != 0:
	response = 'Error, please send it again!'
else:
	response = 'Ok'

# response a ack or a nak 
client.send(response.encode())

#close the connection.
client.close()

#close server socket.
server.close()