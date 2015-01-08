__author__ = 'tecnoman5000'

import os
import ntpath

def stripper_main(file_name):
	with open('output/' + ntpath.basename(os.path.splitext(file_name)[0]) + '_asm', 'w+') as asm_file_tmp:  # Open file
		with open(file_name, 'r') as asm_file_orgi:  # Open file
			tmp_int = 0;
			for line in asm_file_orgi.read().splitlines():  # For lines in ams file pull string data
				#print('Reading...', str(tmp_int))
				tmp_int += 1
	
				"""""""""""""""""""""""""""""""""
				######## Comment Checks #########
				"""""""""""""""""""""""""""""""""
				index = line.find('#')  # check for comment formatting
				if index != 0 and line != '':  # if comment formatting not found at the beginning of the line
					while index < len(line):
						index = line.find('#',index)
						if index == -1:
							break
						line = line[:index]
						index += 1
	
					"""""""""""""""""""""""""""""""""
					###### Whitespace Checks ########
					"""""""""""""""""""""""""""""""""
	
					'''	Tab Check '''
					#remove tabs from right and left side
					line = line.lstrip()
					line = line.rstrip()
	
					#remove middle tabs and replace with a single pace
					number = 0
					tab_place = []
					tab_found = False
					while number < len(line):  # Find tabs in the supplied string
						number = line.find('\t', number)  # finds the desired character within the string, then places the place value at which the desired char was found in the 'index' var
						if number == -1:  # if the desired char is not found, the '.find()' command returns -1, then breaks the while loop (to avoid an infinite loop)
							break
						# print("Found a comma at %d" %(index))  # print location of ,s when found
						tab_place.append(number)  # adds the place value of the desired char in the array
						tab_found = True
						number += 1  # adds on to the place value of the desired char, so the next such for the char, starts after the initially found one. (to avoid an infinite loop of finding the initial desired char)
	
					# If a tab is found in the middle of the text, work to remove
					if tab_found:
						line = line.replace(line[tab_place[0]:tab_place[len(tab_place)-1]+1],' ')
	
					''' Space Check '''
					# check for multiple spaces, replace with single space
					if line.find('  ') != -1:
						line = line.replace('  ',' ')
	
					print(line)
					asm_file_tmp.write(line + '\n')

	asm_file_tmp.close()
	asm_file_orgi.close()

	#return 'output/' + ntpath.basename(os.path.splitext(file_name)[0]) + '_asm.tmp'
#stripper_main('/media/tecno/55CB-85FD/Optimized doubledabble assembly')