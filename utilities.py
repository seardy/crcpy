import binascii, sys

def convertToBinary(data):
	bin_data = bin(int(binascii.hexlify(data.encode()),16))[2:]
	return bin_data

def crc(msg, gen, code='0000'):
	msg = msg + code  #ssd
	
	msg = list(msg)
	gen = list(gen)

	# start 
	for i in range(len(msg)-len(code)):
		if msg[i] == '1': # if bit equals 1
			for j in range(len(gen)):
				msg[i+j] = str((int(msg[i+j])+int(gen[j]))%2)


	return ''.join(msg[-len(code):])

