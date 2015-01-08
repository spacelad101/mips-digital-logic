__author__ = 'Tecnoman5000'
__author__ = 'spacelad101'
def rom_main(rom_file_name, hex_file_name):
	hex_file_path = hex_file_name
	hex_arr = ['0']
	num_lines = 0

	#open file and read in hex values
	with open(hex_file_path, 'r') as hex_file:  # Open file
		for line in hex_file.read().splitlines():  # For lines in hex file pull string data
			#isoate the address in the file line
			address_start = line.find(': ')
			address_end = line.find(' ;')
			line = line[address_start+2:address_end]
			hex_arr.append(line)  # add just the address to the array
			num_lines += 1  # count the number of lines
		hex_file.close()

	# write file
	with open(rom_file_name, 'w+') as rom_file:
		#print("Rom output file name: "+rom_file_name)
		rom_file.write('v2.0 raw')
		for index in range(0, len(hex_arr)):
			if index % 2 == 0:
				rom_file.write('\n')
			rom_file.write(hex_arr[index])
			rom_file.write(" 0 0 0 ")
		rom_file.close()

		

