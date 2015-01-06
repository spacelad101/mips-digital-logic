from mipsCompiler import mips_main
from bth import convert_hex
from romCompiler import rom_main
import os
import ntpath

def convert_all(filepath):
	#Convert the assembly into binary
	mips_main(filepath)
	#define output path to store everything in
	output = 'output/' + ntpath.basename(os.path.splitext(filepath)[0])
	#Convert the binary to hex
	convert_hex(output)
	hex_name="example_asm_hex"
	#Ask for output name
	#rom_name=str(input("output name for hex to rom file?: "))
	rom_name = "example_asm_rom"
	#Pass the name and hex file into the rom generator
	rom_main(rom_name,hex_name)
	#Put the rom generator function here when its done
convert_all(str(input("Path of assembly file to compile?: ")))