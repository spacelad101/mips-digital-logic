__author__ = 'Tecnoman5000'
def rom_main(rom_file_name, hex_file_name):
	hex_file_path = "output/" + hex_file_name
	hex_arr = []
	num_lines = 0

	with open(hex_file_path, 'r') as hex_file:  # Open file
		for line in hex_file.read().splitlines():  # For lines in hex file pull string data
			hex_arr.append(line)
			num_lines += 1
	for index in range(0, len(hex_arr)):
		print(hex_arr[index])
	print(num_lines)

	for index in range(0, int(len(hex_arr))/2):
			print (hex_arr[index])

