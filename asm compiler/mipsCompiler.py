import sys
from dtb import convert

print(convert(32, 32))

file_name = str(input("Name of file to compile? (*.txt): "))
if file_name == '':
	file_name = "samples\example.txt"  # For testing purposes, making runs faster to test.
commands = []  # Master Command array, will hold arrays or commands

# Defines registers $0 - $31 as corresponding binary values
registers = ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011',
			 '11100', '11101', '11110', '11111']
# Defines binary values for hex characters
hexval = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111', 'A': '1010', 'B': '1011', 'C': '1100',
		  'D': '1101', 'E': '1110', 'F': '1111'}
# Defines binary values for operation codes
opcode = {'addi': '000010', 'addu': '000011', 'addiu': '000100', 'divu': '000110', 'div': '000101', 'multu': '001000', 'mult': '000111', 'subu': '001010', 'sub': '001001', 'andi': '001100', 'and': '001011', 'nandi': '001110', 'nand': '001101', 'ori': '010000',
		  'or': '001111', 'nori': '010010', 'nor': '010001', 'xori': '010100', 'xor': '010011', 'xnori': '010110', 'xnor': '010101', 'sll': '010111', 'srl': '011000', 'lui': '011001', 'slti': '011011', 'sltu': '011100', 'sltiu': '011101', 'beq': '011110',
		  'bgezal': '100000', 'bgtz': '100001', 'blez': '100010', 'bltzal': '100011', 'bltz': '100100', 'bne': '100101', 'jal': '100111', 'jr': '101000', 'j': '100110', 'lb': '101001', 'lh': '101010', 'lw': '101011', 'sb': '101100', 'sh': '101101', 'sw': '101110',
		  'mfhi': '101111', 'mflo': '110000', 'mthi': '110001', 'mtlo': '110010', 'noop': '000000', 'add': '000001', 'bgez': '011111', 'slt': '011010', 'sra': '110011', 'sllv': '110100', 'srlv': '110101', 'srav': '110110'}
# Defines syntax for operation codes
opcode_syntax = {'addi': 'dsC', 'addu': 'dst', 'addiu': 'dsC', 'divu': 'st', 'div': 'st', 'multu': 'st', 'mult': 'st', 'subu': 'dst', 'sub': 'dst', 'andi': 'dsC', 'and': 'dst', 'nandi': 'dsC', 'nand': 'dst', 'ori': 'dst', 'or': 'dst', 'nori': 'dsC', 'nor': 'dst',
				 'xori': 'dsC', 'xor': 'dst', 'xnori': 'dsC', 'xnor': 'dst', 'sll': 'dsH', 'srl': 'dsH', 'lui': 'dC', 'slti': 'dsC', 'sltu': 'dst', 'sltiu': 'dsC', 'beq': 'stC', 'bgezal': 'sC', 'bgtz': 'sC', 'blez': 'sC', 'bltzal': 'sC', 'bltz': 'sC', 'bne': 'stC',
				 'jal': 'C', 'jr': 's', 'j': 'C', 'lb': 'dCs', 'lh': 'dCs', 'lw': 'dCs', 'sb': 'tCs', 'sh': 'tCs', 'sw': 'tCs', 'mfhi': 'd', 'mflo': 'd', 'mthi': 's', 'mtlo': 's', 'noop': '', 'add': 'dst', 'bgez': 'sC', 'slt': 'dst', 'sra': 'dsH', 'sllv': 'dts',
				 'srlv': 'dts', 'srav': 'dts'}
# Defines encoding for operation codes
opcode_encoding = {'addi': 'sdC', 'addu': 'std', 'addiu': 'sdC', 'divu': 'st', 'div': 'st', 'multu': 'st', 'mult': 'st', 'subu': 'std', 'sub': 'std', 'andi': 'sdC', 'and': 'std', 'nandi': 'sdC', 'nand': 'std', 'ori': 'sdC', 'or': 'std', 'nori': 'sdC', 'nor': 'std',
				   'xori': 'sdC', 'xor': 'std', 'xnori': 'sdC', 'xnor': 'std', 'sll': 'sdH', 'srl': 'sdH', 'lui': 'd-C', 'slti': 'sdC', 'sltu': 'std', 'sltiu': 'sdC', 'beq': 'stC', 'bgezal': 's-C', 'bgtz': 's-C', 'blez': 's-C', 'bltzal': 's-C', 'bltz': 's-C',
				   'bne': 'stC', 'jal': 'C', 'jr': 's', 'j': 'C', 'lb': 'sdC', 'lh': 'sdC', 'lw': 'sdC', 'sb': 'stC', 'sh': 'stC', 'sw': 'stC', 'mfhi': 'd', 'mflo': 'd', 'mthi': 's', 'mtlo': 's', 'noop': '-', 'add': 'std', 'bgez': 's-c', 'slt': 'std', 'sra': 'sdH',
				   'sllv': 'std', 'srlv': 'std', 'srav': 'std'}
# Defines register aliases
reg_ali = {'$at': '$1', 'v0': '$2', 'v1': '$3', 'a0': '$4', 'a1': '$5', 'a2': '$6', 'a3': '$7', 't0': '$8', 't1': '$9', 't2': '$10', 't3': '$11', 't4': '$12', 't5': '$13', 't6': '$14', 't7': '$15', 's0': '$16', 's1': '$17', 's2': '$18', 's3': '$19', 's4': '$20',
		   's5': '$21', 's6': '$22', 's7': '$23', 't8': '$24', 't9': '$25', 'k0': '$26', 'k1': '$27', '$kt0': '$26', '$kt1': '$27', 'gp': '$28', '$gp': '$28', 'sp': '$29', '$sp': '$29', 'fp': '$30', '$fp': '$30', 'ra': '$31'}


def splice_file_input(file_input):  # find comma placement within the current line of the file
	comma_place = []  # Reset comma placement array
	space_place = []
	tmp_array = []  # use a tmp_array to store the commands found on current line

	index = file_input.find('#')  # check asm code for comment
	if index > -1:  # if comment found
		file_input = file_input[:index]  # remove comments from file line

	# find commands based on spaces in the file line
	index = 0
	while index < len(file_input):  # Find spaces in the supplied string
		index = file_input.find(' ', index)  # finds the desired character within the string, then places the place value at which the desired char was found in the 'index' var
		if index == -1:  # if the desired char is not found, the '.find()' command returns -1, then breaks the while loop (to avoid an infinite loop)
			break

		if index != 0 and index < len(file_input):
			space_place.append(index)  # adds the place value of the desired char in the comma_place array
		index += 1  # adds on to the place value of the desired char, so the next such for the char, starts after the initially found one. (to avoid an infinite loop of finding the initial desired char)

	tmp_array.append(file_input[:space_place[0]])  # Adds the encoder command the the tmp_array
	file_input = file_input[space_place[0] + 1:]  # Removes the encoder command from the file input, since it has already been spliced into the tmp_array

	# find commands based on commas in the file line
	index = 0
	while index < len(file_input):  # Find commas in the supplied string
		index = file_input.find(',', index)  # finds the desired character within the string, then places the place value at which the desired char was found in the 'index' var
		if index == -1:  # if the desired char is not found, the '.find()' command returns -1, then breaks the while loop (to avoid an infinite loop)
			break
		# print("Found a comma at %d" %(index))  # print location of ,s when found
		comma_place.append(index)  # adds the place value of the desired char in the comma_place array
		index += 1  # adds on to the place value of the desired char, so the next such for the char, starts after the initially found one. (to avoid an infinite loop of finding the initial desired char)

	comma_place.append(len(file_input))  # add the end of the file_input
	# num_commands = int(len(comma_place) + 1)  # Stores the number of commands found in current line of the file

	# Adds the commands to the tmp_array
	file_start = 0
	for c in comma_place:  # for the number of commas + the end
		tmp_array.append(file_input[file_start:c])  # add the single command to the commands list, c = the end of the command in the string
		file_start = c + 1  # store the beginning of the next command's location in the string

	for c in range(0, len(tmp_array)):  # for the length of the array
		index = tmp_array[c].find(' ')  # search for ' ' (spaces), if found note their index
		if index != -1:  # if one is found
			tmp_array[c] = tmp_array[c].replace(' ', '')  # replace the space with nothing (removing it from the command)

	index = file_input.find('(')  # search for special formatting **($*)
	if index != -1:  # if formatting found
		tmp_array[len(tmp_array) - 1] = tmp_array[len(tmp_array) -1][0:1]  # remove the register formatting from the previous spot in the array
		tmp_array.append(file_input[index + 1:index + 3])  # add the register command to the array (this works because this is the last thing to be added to this array)

	commands.append(tmp_array)  # add the tmp_array to the master array, as a second dimension (representing a new line)
	return


# first part 'encoder' gets converted into binary via the 'opcode' dict.
def opcode_conversion():
	for c in range(0, len(commands)):  # for the number of secondary arrays in commands
		commands[c][0] = opcode[commands[c][0]]  # find encoder command (key) in dict, and replace with definition
	return


# the numbers following get converted into binary via the 'registers' array, number = registers[number]
# encoders with 'i' at the end will have a hex value, hex value will always be the last value in the second dimensional array and start with '0x'
# all register address start with '$'
def to_binary_converter():
	for c in range(0, len(commands)):  # for the number of secondary arrays in commands
		# if commands[c][0] == 'j' or commands[c][0] == 'jal':  # If encoder is a jump instruction
		# 	for sc in range(1, len(commands[c])):  # runs for the number of commands in the second dimension array (start at one to avoid conflict with the encoder command)
		# 		# print('checking')
		# 		index = commands[c][sc].find('0x')  # search for hex value formatting
		# 		if index == -1:  # if none found display error message and end script
		# 			print('Bad "' + commands[c][0] + '" formatting, on line ' + str(c + 1) + '. "' + commands[c][sc][:3] + '" is an invalid option. MUST BE CONTAIN A HEX VALUE!')  # Error message
		# 			sys.exit(0)  # End Script
		input_syntax = opcode_syntax[commands[c][0]]  # store the input syntax of the current instruction
		output_syntax = opcode_encoding[commands[c][0]]  # store the syntax for the output binary config
		tmp_dict = {}
		tmp_array = []

		for sc in range(1, len(commands[c])):  # runs for the number of commands in the second dimension array, except the encoder command range(start after the encoder position in the array, length of the array)
			tmp_dict[input_syntax[sc-1:sc]] = commands[c][sc] #
		for sc in range(1, len(commands[c])):  # runs for the number of commands in the second dimension array, except the encoder command range(start after the encoder position in the array, length of the array)
			tmp_array.append(tmp_dict[output_syntax[sc-1:sc]])

		for sc in range(0, len(tmp_array)):  # runs for the number of commands in the second dimension array, except the encoder command range(start after the encoder position in the array, length of the array)
			index = tmp_array[sc].find('$')  # search for '$' and hold the place value of the '$' in the current string, within the second dimension array

			if index == 0:  # if a '$' was found and is at the beginning of the commands (to avoid conflict with hex value commands)
				tmp_array[sc] = tmp_array[sc][index + 1:]  # remove the '$' formatting
				tmp_array[sc] = registers[int(tmp_array[sc])]  # use the register commands as a reference in the 'registers' array and replace with the corresponding binary number

			else:  # if not a register value ($*), assume it's a decimal number
				if tmp_array[sc].isdigit():  # check if the command is indeed only digits
					current_bit_length = 0  # track the bit length
					for b in range(0, len(tmp_array) - 1):
						current_bit_length += len(tmp_array[b])  # find current bit length
						print(current_bit_length)
					if current_bit_length == 0:
						tmp_array[sc] =  convert(26, int(tmp_array[sc]))
					else:
						tmp_array[sc] =  convert(current_bit_length, int(tmp_array[sc]))

		for sc in range(0, len(tmp_array)):
			commands[c][sc + 1] = tmp_array[sc]

	return

def condense_line():
	for c in range(0, len(commands)):
		tmp_string = ''  # will hold the newly created string

		for sc in range(0, len(commands[c])):
			tmp_string += commands[c][sc]  # add the commands in each position of the second dimensional array into the string

		if len(tmp_string) != 32: #if the string is not a perfect 32 bits long adds '0's to the end until it is
			while len(tmp_string) < 32:  # while the string isn't 32 bits long
				tmp_string += '0'  # add zero to the end (this needs to be fixed, this needs to add to the front of the immediate value)
		commands[c] = tmp_string  # add the new string in place of the old array


with open(file_name, 'r') as asmFile:  # Open file
	for line in asmFile.read().splitlines():  # For lines in ams file pull string data
		index = line.find('#')  # check for comment formatting
		if index != 0:  # if comment formatting not found at the beginning of the line
			splice_file_input(line)  # pull the commands out of the input
print(commands)
to_binary_converter()  # Start the hex value conversion process
print(commands)
opcode_conversion()  # Start the opcode conversion for the encoder commands from ascii to binary
print(commands)
condense_line()  # condense the array of commands in a single string
print(commands)

# for c in range(0, len(commands)):  # check bit lengths for each of the lines of commands
# 	total_bit_length = 0
# 	for sc in range(0, len(commands[c])):
# 		total_bit_length += len(commands[c][sc])
# 	print(total_bit_length)

# Default rule - hex value must be 4 long after '0x'  (implemented)
# rule  # 1 - sll & srl must have a hexValue that starts with 0x1* or 0x0*, where * stands for one more single hex value (implemented)
# rule  # 2 - j & jal must have a hexValue (check this before doing conversions)
