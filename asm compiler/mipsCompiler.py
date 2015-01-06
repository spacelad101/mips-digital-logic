__author__ = 'Tecnoman5000'
__author__ = 'spacelad101'
import sys
import ntpath
import os
from dtb import convert
sys.path.append('example generation')

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
opcode_syntax = {'addi': 'dsC', 'addu': 'dst', 'addiu': 'dsC', 'divu': 'st', 'div': 'st', 'multu': 'st', 'mult': 'st', 'subu': 'dst', 'sub': 'dst', 'andi': 'dsC', 'and': 'dst', 'nandi': 'dsC', 'nand': 'dst', 'ori': 'dsC', 'or': 'dst', 'nori': 'dsC', 'nor': 'dst',
				 'xori': 'dsC', 'xor': 'dst', 'xnori': 'dsC', 'xnor': 'dst', 'sll': 'dsH', 'srl': 'dsH', 'lui': 'dC', 'slti': 'dsC', 'sltu': 'dst', 'sltiu': 'dsC', 'beq': 'stC', 'bgezal': 'sC-', 'bgtz': 'sC-', 'blez': 'sC-', 'bltzal': 'sC-', 'bltz': 'sC-', 'bne': 'stC',
				 'jal': 'C', 'jr': 's', 'j': 'C', 'lb': 'dCs', 'lh': 'dCs', 'lw': 'dCs', 'sb': 'tCs', 'sh': 'tCs', 'sw': 'tCs', 'mfhi': 'd', 'mflo': 'd', 'mthi': 's', 'mtlo': 's', 'noop': '', 'add': 'dst', 'bgez': 'sC-', 'slt': 'dst', 'sra': 'dsH', 'sllv': 'dts',
				 'srlv': 'dts', 'srav': 'dts'}
# Defines encoding for operation codes
opcode_encoding = {'addi': 'sdC', 'addu': 'std', 'addiu': 'sdC', 'divu': 'st', 'div': 'st', 'multu': 'st', 'mult': 'st', 'subu': 'std', 'sub': 'std', 'andi': 'sdC', 'and': 'std', 'nandi': 'sdC', 'nand': 'std', 'ori': 'sdC', 'or': 'std', 'nori': 'sdC', 'nor': 'std',
				   'xori': 'sdC', 'xor': 'std', 'xnori': 'sdC', 'xnor': 'std', 'sll': 'sdH', 'srl': 'sdH', 'lui': 'd-C', 'slti': 'sdC', 'sltu': 'std', 'sltiu': 'sdC', 'beq': 'stC', 'bgezal': 's-C', 'bgtz': 's-C', 'blez': 's-C', 'bltzal': 's-C', 'bltz': 's-C',
				   'bne': 'stC', 'jal': 'C', 'jr': 's', 'j': 'C', 'lb': 'sdC', 'lh': 'sdC', 'lw': 'sdC', 'sb': 'stC', 'sh': 'stC', 'sw': 'stC', 'mfhi': 'd', 'mflo': 'd', 'mthi': 's', 'mtlo': 's', 'noop': '', 'add': 'std', 'bgez': 's-C', 'slt': 'std', 'sra': 'sdH',
				   'sllv': 'std', 'srlv': 'std', 'srav': 'std'}
# Defines register aliases
reg_ali = {'$at': '$1', 'v0': '$2', 'v1': '$3', 'a0': '$4', 'a1': '$5', 'a2': '$6', 'a3': '$7', 't0': '$8', 't1': '$9', 't2': '$10', 't3': '$11', 't4': '$12', 't5': '$13', 't6': '$14', 't7': '$15', 's0': '$16', 's1': '$17', 's2': '$18', 's3': '$19', 's4': '$20',
		   's5': '$21', 's6': '$22', 's7': '$23', 't8': '$24', 't9': '$25', 'k0': '$26', 'k1': '$27', '$kt0': '$26', '$kt1': '$27', 'gp': '$28', '$gp': '$28', 'sp': '$29', '$sp': '$29', 'fp': '$30', '$fp': '$30', 'ra': '$31'}


def splice_file_input(file_input):  # find comma placement within the current line of the file
	comma_place = []  # Reset comma placement array
	space_place = []
	tmp_array = []  # use a tmp_array to store the commands found on current line

	find_reg_formatting = file_input.find('#')  # check asm code for comment
	if find_reg_formatting > -1:  # if comment found
		file_input = file_input[:find_reg_formatting]  # remove comments from file line

	# find commands based on spaces in the file line
	number = 0
	while number < len(file_input):  # Find spaces in the supplied string
		number = file_input.find(' ', number)  # finds the desired character within the string, then places the place value at which the desired char was found in the 'index' var
		if number == -1:  # if the desired char is not found, the '.find()' command returns -1, then breaks the while loop (to avoid an infinite loop)
			break

		if number != 0 and number < len(file_input):
			space_place.append(number)  # adds the place value of the desired char in the comma_place array
		number += 1  # adds on to the place value of the desired char, so the next such for the char, starts after the initially found one. (to avoid an infinite loop of finding the initial desired char)

	tmp_array.append(file_input[:space_place[0]])  # Adds the encoder command the the tmp_array
	file_input = file_input[space_place[0] + 1:]  # Removes the encoder command from the file input, since it has already been spliced into the tmp_array

	# find commands based on commas in the file line
	number = 0
	while number < len(file_input):  # Find commas in the supplied string
		number = file_input.find(',', number)  # finds the desired character within the string, then places the place value at which the desired char was found in the 'index' var
		if number == -1:  # if the desired char is not found, the '.find()' command returns -1, then breaks the while loop (to avoid an infinite loop)
			break
		# print("Found a comma at %d" %(index))  # print location of ,s when found
		comma_place.append(number)  # adds the place value of the desired char in the comma_place array
		number += 1  # adds on to the place value of the desired char, so the next such for the char, starts after the initially found one. (to avoid an infinite loop of finding the initial desired char)

	comma_place.append(len(file_input))  # add the end of the file_input
	# num_commands = int(len(comma_place) + 1)  # Stores the number of commands found in current line of the file

	# Adds the commands to the tmp_array
	file_start = 0
	for times in comma_place:  # for the number of commas + the end
		tmp_array.append(file_input[file_start:times])  # add the single command to the commands list, c = the end of the command in the string
		file_start = times + 1  # store the beginning of the next command's location in the string

	for times in range(0, len(tmp_array)):  # for the length of the array
		number = tmp_array[times].find(' ')  # search for ' ' (spaces), if found note their index
		if number != -1:  # if one is found
			tmp_array[times] = tmp_array[times].replace(' ', '')  # replace the space with nothing (removing it from the command)

	number = file_input.find('(')  # search for special formatting **($*)
	if number != -1:  # if formatting found
		tmp_array[len(tmp_array) - 1] = tmp_array[len(tmp_array) -1][0:1]  # remove the register formatting from the previous spot in the array
		tmp_array.append(file_input[number + 1:number + 3])  # add the register command to the array (this works because this is the last thing to be added to this array)

	commands.append(tmp_array)  # add the tmp_array to the master array, as a second dimension (representing a new line)
	return


# first part 'encoder' gets converted into binary via the 'opcode' dict.
def opcode_conversion():
	for command_arrays in range(0, len(commands)):  # for the number of secondary arrays in commands
		commands[command_arrays][0] = opcode[commands[command_arrays][0]]  # find encoder command (key) in dict, and replace with definition
	return


# the numbers following get converted into binary via the 'registers' array, number = registers[number]
# encoders with 'i' at the end will have a hex value, hex value will always be the last value in the second dimensional array and start with '0x'
# all register address start with '$'
def to_binary_converter():
	for command_arrays in range(0, len(commands)):  # for the number of secondary arrays in commands
		input_syntax = opcode_syntax[commands[command_arrays][0]]  # store the input syntax of the current instruction
		output_syntax = opcode_encoding[commands[command_arrays][0]]  # store the syntax for the output binary config
		tmp_dict = {}
		tmp_array = []

		for len_input_script in range(0, len(input_syntax)):  # runs for the number of commands in the second dimension array, except the encoder command range(start after the encoder position in the array, length of the array)
			if input_syntax[len_input_script:len_input_script+1] == '':  # noop instruction exception
				tmp_dict[input_syntax[len_input_script:len_input_script+1]] = '000000000000000000000000000000000'  # add to the dict with the key ''
				commands[command_arrays].append(tmp_dict[input_syntax[len_input_script:len_input_script+1]])  # add '00000' to the array

			if input_syntax[len_input_script:len_input_script+1] == '-':  # if - found, then it won't be in the array and we have to create it
				tmp_dict[input_syntax[len_input_script:len_input_script+1]] = '00000'  # add to the dict with the key '-'

			else: # if it's not a '-' that means the command is already in the array
				tmp_dict[input_syntax[len_input_script:len_input_script+1]] = commands[command_arrays][len_input_script+1]  # add a syntax key to each of the commands

		for len_input_script in range(0, len(output_syntax)):  # runs for the number of commands in the second dimension array, except the encoder command range(start after the encoder position in the array, length of the array)
			if output_syntax[len_input_script:len_input_script+1] == '-' and output_syntax[len_input_script:len_input_script+1].find('-') != len(output_syntax) - 1:  # if - found, then it won't be in the array and we have to create it
				tmp_array.append('00000')  # add to the array
				commands[command_arrays].append('00000')  # add to the command line array, to avoid conflict later
			else:
				tmp_array.append(tmp_dict[output_syntax[len_input_script:len_input_script+1]])  # add the commands into the right order, so after processing the commands come out as the syntax.

		for len_input_script in range(0, len(tmp_array)):  # runs for the number of commands in the second dimension array, except the encoder command range(start after the encoder position in the array, length of the array)
			find_reg_formatting = tmp_array[len_input_script].find('$')  # search for '$' and hold the place value of the '$' in the current string, within the second dimension array

			if find_reg_formatting == 0:  # if a '$' was found and is at the beginning of the commands (to avoid conflict with hex value commands)
				tmp_array[len_input_script] = tmp_array[len_input_script][find_reg_formatting + 1:]  # remove the '$' formatting
				tmp_array[len_input_script] = registers[int(tmp_array[len_input_script])]  # use the register commands as a reference in the 'registers' array and replace with the corresponding binary number

			else:  # if not a register value ($*), assume it's a decimal number
				if tmp_array[len_input_script].isdigit() and tmp_array[len_input_script] != '00000':  # check if the command is indeed only digits
					# C value default bit length is 16
					if output_syntax[len_input_script:len_input_script+1] == 'C' and len(tmp_array) != 1:
						current_bit_length = 16
					# C value special bit length is 26 (in this case, it will be the only value besides the instruction)
					elif len(tmp_array) == 1:
						current_bit_length = 26
					# H value only bit length is 5
					elif output_syntax[len_input_script:len_input_script+1] == 'H':
						current_bit_length = 5

					if  convert(current_bit_length, int(tmp_array[len_input_script])) == 'badnum':  # if the convert fails, throw error
						print('Invalid Bit length or Value: BADNUM. Bit length = ' + str(current_bit_length) + ', Decimal Value = ' + tmp_array[len_input_script] ) # Error message
						sys.exit(0) # End Script
					tmp_array[len_input_script] =  convert(current_bit_length, int(tmp_array[len_input_script]))

		for len_input_script in range(0, len(tmp_array)):
			commands[command_arrays][len_input_script + 1] = tmp_array[len_input_script]
		#print('Converting... ', str(command_arrays + 1), '/', str(len(commands)))
	return

def condense_line():
	for c in range(0, len(commands)):
		tmp_string = ''.join(commands[c])  # join the array, with nothing ('') between each array place value.
		if len(tmp_string) != 32: #if the string is not a perfect 32 bits long adds '0's to the end until it is
			while len(tmp_string) < 32:  # while the string isn't 32 bits long
				tmp_string += '0'  # add zero to the end, if the string has a immediate value it will already be 32 bits, else fill the end because the rest won't matter
		commands[c] = tmp_string  # add the new string in place of the old array
		#print(tmp_string)
		#print('Condensing...', str(c + 1), '/', str(len(commands)))




def mips_main(filepath):
	#create_asm(int(input("Number of examples to test?: ")))

	file_name = filepath#str(input("Name of file to compile? (*.txt): "))
	if file_name == '':
		"""
		file_name = "samples/examples.asm"  # For testing purposes, making runs faster to test.
		print('No file chosen, reverting to default. (samples\examples_asm)')
		time.sleep(3);
		"""
		raise Exception("No File Specified!")


	with open(file_name, 'r') as asmFile:  # Open file
		tmp_int = 0;
		for line in asmFile.read().splitlines():  # For lines in ams file pull string data
			#print('Reading...', str(tmp_int))
			tmp_int += 1;

			index = line.find('#')  # check for comment formatting
			if index != 0 and line != '':  # if comment formatting not found at the beginning of the line
				splice_file_input(line)  # pull the commands out of the input

	to_binary_converter()  # Start the hex value conversion process

	opcode_conversion()  # Start the opcode conversion for the encoder commands from ascii to binary

	condense_line()  # condense the array of commands in a single string

	for c in range(0, len(commands)):  # check bit lengths for each of the lines of commands
		total_bit_length = 0
		for sc in range(0, len(commands[c])):
			total_bit_length += len(commands[c][sc])
		if total_bit_length != 32:
			print('Error, bad bit length. Check Syntax!')
			print('Bit length - ', total_bit_length)
			print('Binary string - ', commands[c])

	# Default rule - hex value must be 4 long after '0x'  (implemented)
	# rule  # 1 - sll & srl must have a hexValue that starts with 0x1* or 0x0*, where * stands for one more single hex value (implemented)
	# rule  # 2 - j & jal must have a hexValue (check this before doing conversions)
	#output file name *_bin
	if not os.path.exists("output"):
		os.makedirs("output")

	with open('output/' + ntpath.basename(os.path.splitext(file_name)[0]) + '_bin', 'w+') as asmFile:  # Open file
		for c in range(0, len(commands)):
				asmFile.write(str(commands[c]) + '\n')  # For lines in ams file pull string data
				#print('Writing...', str(c + 1), '/', str(len(commands)))

	#time.sleep(10)
	#input('Press Enter to Continue')

	return
