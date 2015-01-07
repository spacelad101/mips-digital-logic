__author__ = 'Tecnoman5000'
__author__ = 'spacelad101'

from mipsCompiler import mips_main
from bth import convert_hex
from romCompiler import rom_main
import os
import ntpath
import time

def convert_all(file_path):

	#used for quick testing
	if file_path == '':
		print("Input was null, reverting to default (samples/example_asm)")
		file_path = 'samples/example_asm'
		time.sleep(1)

	print("Mips Assembler Started...")
	time_started = time.time()  # mark program start time

	#Convert the assembly into binary
	mips_main(file_path)

	#mark down mips assemble time
	time_ended = time.time()
	mips_time = time_ended - time_started

	print("Hex Conversion Started...")
	hex_time_start = time.time() # mark down start time of hex conversion

	#define output path to store everything in
	output = 'output/' + ntpath.basename(os.path.splitext(file_path)[0])
	#Convert the binary to hex
	convert_hex(output)
	hex_name= output + "_hex"

	# mark down hex conversion time
	time_ended = time.time()
	hex_time = time_ended - hex_time_start

	print("Rom Assembler Started...")
	rom_time_start = time.time() # mark down start time of rom assemble
	#Ask for output name
	#rom_name=str(input("output name for hex to rom file?: "))
	rom_name = output + "_rom"
	#Pass the name and hex file into the rom generator
	rom_main(rom_name,hex_name)

	# mark down rom assemble time
	time_ended = time.time()
	rom_time = time_ended - rom_time_start

	# mark down total time
	time_ended = time.time()
	total_time = time_ended - time_started

	display_time(mips_time,"Mips ")
	display_time(hex_time,"Hex ")
	display_time(rom_time,"Rom ")
	display_time(total_time,"")

def display_time(time_to_display, part):
	if int(time_to_display) <= 0:
		print(part+'Time elapsed: under a second ('+str(time_to_display)+')')
	elif time_to_display > 60:
		time_to_display /= 60
		time_to_display_int = int(time_to_display)
		print(part+'Time Elapsed: ', time_to_display_int, ' minutes')
	else:
		time_to_display_int = int(time_to_display)
		print(part+'Time Elapsed: ', time_to_display_int, ' seconds')

convert_all(str(input("Path of assembly file to compile?: ")))