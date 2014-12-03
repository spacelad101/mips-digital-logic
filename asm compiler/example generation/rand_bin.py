from random import randint
def getrandbin(file,bits,lines):

	binary_arr = ['']*bits

	with open(file, 'w+') as randbin:
			for x in range(0,lines):
				for y in range(0,bits):
					binary_arr
					randbin.write(str(randint(0,1)))
				randbin.write('\n')

getrandbin(str(input('Choose File Name: ')),int(input('Choose a bit length: ')),int(input('Choose number of lines: ')))