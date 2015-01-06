__author__ = 'Tecnoman5000'
import ntpath
import os
def rom_main(rom_file_name, hex_file_name):
	hex_file_path = hex_file_name
	hex_arr = []
	rom_array = []
	num_lines = 0
	address = 0

	with open(hex_file_path, 'r') as hex_file:  # Open file
		for line in hex_file.read().splitlines():  # For lines in hex file pull string data
			address_start = line.find(': ')
			address_end = line.find(' ;')
			line = line[address_start+2:address_end]
			hex_arr.append(line)
			num_lines += 1

	print(num_lines)

	for index in range(0, len(hex_arr)):
		print (hex_arr[index])
		rom_array.append(hex_arr[index])
		rom_array.append(" 0")
		rom_array.append(" 0")
		rom_array.append(" 0 ")

	with open(rom_file_name, 'w+') as romFile:
		for index in range(0, len(rom_array)):
			#print (rom_array[index])
			romFile.write("test")
			address += 1
		

