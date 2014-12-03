from dtb import convert

def convert_hex(path):
	#filepath = "samples/bin_example.txt" #much debug, very wow

	filepath = path + "_bin"

	address = 0
	numlines=0

	bin_arr=[]
	binarytohex = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7',
				   '1000':'8','1001':'9','1010':'a','1011':'b','1100':'c','1101':'d','1110':'e','1111':'f'}
	with open(filepath, 'r') as binFile:  # Open file
		for line in binFile.read().splitlines():  # For lines in ams file pull string data
			if line != '':
				bin_arr.append(line)
				numlines += 1
		print(bin_arr)

		hex_arr = ['']*numlines
		addr_arr = ['']*numlines
		final_addr_arr = ['']*numlines
		output_arr = ['']*numlines

		for x in range(0,len(bin_arr)): #This shit converts the binary instruction into hex decimal
			address += 4
			for y in range(0,8):
				hex_arr[x] += binarytohex[bin_arr[x][y*4:y*4+4]]
			addr_arr[x] = convert(24,address)
			if addr_arr[x] is "badnum":
				return "'badnum' error has occurred, check that your program isn't too big!"

		for x in range(0,len(addr_arr)): #This motherfucker makes fucking addresses for every instruction every 4th address space
			for y in range(0,6):
				final_addr_arr[x] += binarytohex[addr_arr[x][y*4:y*4+4]]

		with open(path + '_hex', 'w+') as hexFile: #Write this stupid shit to a new file
			for x in range(0,len(output_arr)): #This asshole smashed the instruction and address together.
				output_arr[x] = str(final_addr_arr[x] + ": " + hex_arr[x] + " ;")
				hexFile.write(str(output_arr[x]) + '\n')
				print(output_arr[x])


convert_hex(str(input('Path to file to compile?')))