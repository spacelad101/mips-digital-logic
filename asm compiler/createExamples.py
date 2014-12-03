__author__ = 'Tecnoman5000'
from random import randint

# Defines syntax for operation codes
opcode_syntax = {'addi': 'dsC', 'addu': 'dst', 'addiu': 'dsC', 'divu': 'st', 'div': 'st', 'multu': 'st', 'mult': 'st', 'subu': 'dst', 'sub': 'dst', 'andi': 'dsC', 'and': 'dst', 'nandi': 'dsC', 'nand': 'dst', 'ori': 'dst', 'or': 'dst', 'nori': 'dsC', 'nor': 'dst',
				 'xori': 'dsC', 'xor': 'dst', 'xnori': 'dsC', 'xnor': 'dst', 'sll': 'dsH', 'srl': 'dsH', 'lui': 'dC', 'slti': 'dsC', 'sltu': 'dst', 'sltiu': 'dsC', 'beq': 'stC', 'bgezal': 'sC-', 'bgtz': 'sC-', 'blez': 'sC-', 'bltzal': 'sC-', 'bltz': 'sC-', 'bne': 'stC',
				 'jal': 'C', 'jr': 's', 'j': 'C', 'lb': 'dCs', 'lh': 'dCs', 'lw': 'dCs', 'sb': 'tCs', 'sh': 'tCs', 'sw': 'tCs', 'mfhi': 'd', 'mflo': 'd', 'mthi': 's', 'mtlo': 's', 'noop': '', 'add': 'dst', 'bgez': 'sC-', 'slt': 'dst', 'sra': 'dsH', 'sllv': 'dts',
				 'srlv': 'dts', 'srav': 'dts'}
instruction = []
for key, value in opcode_syntax.items():
	instruction.append(key)

examples = []

def create_asm(number):
	# take in number of examples wanted
	for n in range(0, number):
		tmp_dict = {}
		syntax = opcode_syntax[instruction[n]]
		print(syntax)
		examples.append(n)

		for l in range(0, len(syntax)):
			if syntax[l:l+1] == 'd' or syntax[l:l+1] == 's' or syntax[l:l+1] == 't':
				tmp_dict[syntax[l:l+1]] = '$' + str(randint(1, 31))
			if syntax[l:l+1] == 'C':
				tmp_dict[syntax[l:l+1]] = str(randint(1, 65535))
			if syntax[l:l+1] == 'C' and len(syntax) == 1:
				tmp_dict[syntax[l:l+1]] = str(randint(1, 67108864))
			if syntax[l:l+1] == 'H':
				tmp_dict[syntax[l:l+1]] = str(randint(1, 31))
			if syntax[l:l+1] == '-':
				syntax = syntax[:l]
		print(tmp_dict)

		tmp_string = ''
		for l in range(0, len(syntax)):
			tmp_string += tmp_dict[syntax[l:l+1]]
			if l < len(syntax) - 1:
				tmp_string += ','
			examples[n] = instruction[n] + ' ' + tmp_string

		print(examples[n])
	print(examples)

create_asm(14)