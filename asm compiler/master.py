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
	
	time_started = time.time()
	#Convert the assembly into binary
	mips_main(file_path)
	#define output path to store everything in
	output = 'output/' + ntpath.basename(os.path.splitext(file_path)[0])
	#Convert the binary to hex
	convert_hex(output)
	hex_name= output + "_hex"
	#Ask for output name
	#rom_name=str(input("output name for hex to rom file?: "))
	rom_name = output + "_rom"
	#Pass the name and hex file into the rom generator
	rom_main(rom_name,hex_name)
	#Put the rom generator function here when its done

	time_ended = time.time()
	total_time = time_ended - time_started
	print(time_started)
	print(time_ended)
	print(total_time)
	if total_time <= 0:
		print('Time elapsed: under a second ('+total_time+')')
	elif total_time > 60:
		total_time /= 60
		total_time_int = int(total_time)
		print('Time Elapsed: ', total_time_int, ' minutes')
	else:
		total_time_int = int(total_time)
		print('Time Elapsed: ', total_time_int, ' seconds')

convert_all(str(input("Path of assembly file to compile?: ")))