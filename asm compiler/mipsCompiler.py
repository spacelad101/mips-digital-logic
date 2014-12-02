import sys

file_name = str(input("Name of file to compile? (*.txt): "))
if file_name == '':
    file_name = "samples\example.txt"  # For testing purposes, making runs faster to test.
commands = []   # Master Command array, will hold arrays or commands

# Defines registers $0 - $31 as corresponding binary values
registers = ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011',
             '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111',
             '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']
# Defines binary values for hex characters
hexval = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
          'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
          'E': '1110', 'F': '1111'}
# Defines binary values for operation codes
opcode = {'addi': '000010', 'addu': '000011', 'addiu': '000100', 'divu': '000110', 'div': '000101', 'multu': '001000',
          'mult': '000111', 'subu': '001010', 'sub': '001001', 'andi': '001100', 'and': '001011', 'nandi': '001110',
          'nand': '001101', 'ori': '010000', 'or': '001111', 'nori': '010010', 'nor': '010001', 'xori': '010100', 'xor': '010011',
          'xnori': '010110', 'xnor': '010101', 'sll': '010111', 'srl': '011000', 'lui': '011001', 'slti': '011011',
          'sltu': '011100', 'sltiu': '011101', 'beq': '011110', 'bgezal': '100000', 'bgtz': '100001', 'blez': '100010',
          'bltzal': '100011', 'bltz': '100100', 'bne': '100101', 'jal': '100111', 'jr': '101000', 'j': '100110', 'lb': '101001',
          'lh': '101010', 'lw': '101011', 'sb': '101100', 'sh': '101101', 'sw': '101110', 'mfhi': '101111', 'mflo': '110000',
          'mthi': '110001', 'mtlo': '110010', 'noop': '000000', 'add': '000001', 'bgez': '011111', 'slt': '011010', 'sra': '110011',
          'sllv': '110100', 'srlv': '110101', 'srav': '110110'}
# Defines register aliases
reg_ali = {'$at': '$1', 'v0': '$2', 'v1': '$3', 'a0': '$4', 'a1': '$5', 'a2': '$6', 'a3': '$7',
           't0': '$8', 't1': '$9', 't2': '$10', 't3': '$11', 't4': '$12', 't5': '$13', 't6': '$14',
           't7': '$15', 's0': '$16', 's1': '$17', 's2': '$18', 's3': '$19', 's4': '$20', 's5': '$21',
           's6': '$22', 's7': '$23', 't8': '$24', 't9': '$25', 'k0': '$26', 'k1': '$27', '$kt0': '$26', '$kt1': '$27',
           'gp': '$28', '$gp': '$28', 'sp': '$29', '$sp': '$29', 'fp': '$30', '$fp': '$30', 'ra': '$31'}


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
                if commands[c][0] == 'j' or commands[c][0] == 'jal':  # If encoder is a jump instruction
                        for sc in range(1, len(commands[c])):  # runs for the number of commands in the second dimension array (start at one to avoid conflict with the encoder command)
                                # print('checking')
                                index = commands[c][sc].find('0x')  # search for hex value formatting
                                if index == -1:  # if none found display error message and end script
                                        print('Bad "' + commands[c][0] + '" formatting, on line ' + str(c + 1) + '. "' + commands[c][sc][:3] + '" is an invalid option. MUST BE CONTAIN A HEX VALUE!')  # Error message
                                        sys.exit(0)  # End Script

                for sc in range(0, len(commands[c])):  # runs for the number of commands in the second dimension array
                        index = commands[c][sc].find('$')  # search for '$' and hold the place value of the '$' in the current string, within the second dimension array
                        if index == 0:  # if a '$' was found and is at the beginning of the commands (to avoid conflict with hex value commands)
                                commands[c][sc] = commands[c][sc][index + 1:]  # remove the '$' formatting
                                commands[c][sc] = registers[int(commands[c][sc])]  # use the register commands as a reference in the 'registers' array and replace with the corresponding binary number
                        else:  # if not a register value ($*), check for hex value
                                index = commands[c][sc].find('0x')
                                if index == 0:
                                        commands[c][sc] = commands[c][sc][index + 2:]  # remove the '$' formatting
                                        if len(commands[c][sc]) == 4:  # if the hex value if the default length
                                                tmp_string_conv = ''  # Create a new string to be reference in the for loop, hold the converted command
                                                
                                                for hv in range(0, len(commands[c][sc])):  # run loop for the number of single hex value chars in the command
                                                        tmp_string = commands[c][sc][hv]   # the tmp_string holds the current single hex value to be converted
                                                        tmp_string_conv += hexval[tmp_string]  # Add the newly converted hex value to the rest of the converted values

                                                commands[c][sc] = tmp_string_conv  # add the converted command to the array
                                        elif len(commands[c][sc]) == 2:  # if the hex value has a length of 2
                                                if commands[c][0] == 'sll' or commands[c][0] == 'srl':  # check to see if rule  # 1 applies here
                                                        if commands[c][sc][0] == '0' or commands[c][sc][0] == '1':  # check to see if it starts with either a 0 or 1, to comply with rule  # 1
                                                                tmp_string_conv = ''  # Create a new string to be reference in the for loop, hold the converted command
                                                                
                                                                for hv in range(0, len(commands[c][sc])):  # run loop for the number of single hex value chars in the command
                                                                        tmp_string = commands[c][sc][hv]   # the tmp_string holds the current single hex value to be converted
                                                                        tmp_string_conv += hexval[tmp_string]  # Add the newly converted hex value to the rest of the converted values

                                                                commands[c][sc] = tmp_string_conv  # add the converted command to the array
                                                        else:  # if sll or srl encoder's hex value does not have the proper format. Post error message and end the script
                                                                print('Bad "' + commands[c][0] + '" formatting, on line ' + str(c + 1) + '. "' + commands[c][sc][0] + '" is an invalid option. MUST BE A "0" or "1"!')  # Error message
                                                                sys.exit(0)  # End Script
                                        elif len(commands[c][sc]) == 8:  # check to see if hex value is in '****($*)' format
                                                if commands[c][sc][4] == '(' and commands[c][sc][5] == '$' and commands[c][sc][7] == ')':  # register formatting found
                                                        tmp_string_reg = commands[c][sc][4:]  # tmp_string equals the register command
                                                        tmp_string_reg = tmp_string_reg.replace(commands[c][sc][5:6], '')  # remove the '$' before the register number
                                                        tmp_string_reg = tmp_string_reg.replace(commands[c][sc][6:7], registers[int(commands[c][sc][6:7])])  # replace the register number with the binary equivalent
                                                        
                                                        # Hex value conversion
                                                        tmp_string_conv = ''  # Create a new string to be reference in the for loop, hold the converted command
                                                        for hv in range(0, len(commands[c][sc]) - 4):  # run loop for the number of single hex value chars in the command
                                                                tmp_string = commands[c][sc][hv]   # the tmp_string holds the current single hex value to be converted
                                                                tmp_string_conv += hexval[tmp_string]  # Add the newly converted hex value to the rest of the converted values

                                                        commands[c][sc] = tmp_string_conv + tmp_string_reg  # add the converted command to the array
                                                        # print(commands)  # prints the newly converted commands
        return

with open(file_name, 'r') as asmFile:  # Open file
        for line in asmFile.read().splitlines():  # For lines in rmDict.txt file pull string data
                index = line.find('#')  # check for comment formatting
                if index != 0:  # if comment formatting not found at the beginning of the line
                    splice_file_input(line)  # pull the commands out of the input

to_binary_converter()  # Start the hex value conversion process
opcode_conversion()  # Start the opcode conversion for the encoder commands from ascii to binary


print(commands)

# Default rule - hex value must be 4 long after '0x'  (implemented)
# rule  # 1 - sll & srl must have a hexValue that starts with 0x1* or 0x0*, where * stands for one more single hex value (implemented)
# rule  # 2 - j & jal must have a hexValue (check this before doing conversions)
