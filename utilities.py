import binascii,sys

def crc(message, generator, crc_code='0000'):

	if int(crc_code) == 0 : # if there isnt a crc_code and is the first xor module
		crc_code = ''
		for i in range(len(generator) -1):
			crc_code = crc_code + '0'

	# add the crc_code to the binary message
	message = message + crc_code

	# convert divisors to lists for better management.
	message = list(message)
	generator = list(generator)

	#
	for i in range(len(message) - len(crc_code)):
		if message[i] == '1': # if is a 1 bit
			for j in range(len(generator)):
				message[i+j] = str((int(message[i+j])+int(generator[j]))%2) # mod 2 division

	return ''.join(message[-len(crc_code):])

