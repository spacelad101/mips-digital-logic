from mipsCompiler import main
from bth import convert_hex
import os
import ntpath

def convert_all(filepath):
	#Convert the assembly into binary
	main(filepath)
	#define output path to store everything in
	output = 'output/' + ntpath.basename(os.path.splitext(filepath)[0])
	#Convert the binary to hex
	convert_hex(output)
	#Ask for output name
	rom_name=str(input("Path of file to compile?: "))
	#Pass the name and hex file into the rom generator
	#Put the rom generator function here when its done
convert_all(str(input("Path of file to compile?: ")))