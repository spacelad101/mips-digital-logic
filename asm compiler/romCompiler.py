__author__ = 'Tecnoman5000'
def rom_main(rom_file_name, hex_file_name):
	hex_file_path = hex_file_name
	hex_arr = []
	rom_array = []
	num_lines = 0
	address = 0

	#open file and read in hex values
	with open(hex_file_path, 'r') as hex_file:  # Open file
		for line in hex_file.read().splitlines():  # For lines in hex file pull string data
			#isoate the address in the file line
			address_start = line.find(': ')
			address_end = line.find(' ;')
			line = line[address_start+2:address_end]
			hex_arr.append(line)  # add just the address to the array
			num_lines += 1  # count the number of lines

	print(num_lines)

	# create the rom array to write later
	for index in range(0, len(hex_arr)):
		print (hex_arr[index])
		rom_array.append(hex_arr[index])
		rom_array.append(" 0 0 0 ")
		#rom_array.append(" 0")
		#rom_array.append(" 0")
		#rom_array.append(" 0 ")

	# write file
	with open(rom_file_name, 'w+') as romFile:
		romFile.write('v2.0 raw\n')
		for index in range(0, len(rom_array)):
			if address >= 4:
				address = 0
				romFile.write('\n')
			#print (rom_array[index])
			romFile.write(rom_array[index])
			address += 1

		

