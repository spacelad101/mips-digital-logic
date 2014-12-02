#This shit that isnt in a function is temp debug shit
bl = int(input("Enter a bit length: "))  # Get a bit length
numb = int(input("Enter a number: "))  # Get a number
bin_result = convert(bl,numb)
print(bin_result)

"""
This adds one to the binary number stored in binary_arr.
This is to be used to sign a 2's compliment binary number.
"""
def add_one():
    carry = False
    for x in range(0, exponent):
        if (carry is False) & (binary_arr[x] == 0):
            binary_arr[x] = 1
            break
        elif (carry is False) & (binary_arr[x] == 1):
            binary_arr[x] = 0
            carry = True
        else:
            if (binary_arr[x] == 1) & (carry is True):
                binary_arr[x] = 0
            elif (binary_arr[x] == 0) & (carry is True):
                binary_arr[x] = 1
                break
    return

"""
If the number is greater than zero, check if the number is 
larger than the most significant bit and subtract 2^x if it is and insert a 1 in that bit position.
Otherwise, insert a 0 in that bit position check the next most significant bit and check then
subtract if smaller inserting either a 1 or a 0. Keep repeating with the next most significant
bit until there is nothing left to check (ie. until it has reached 2^0
"""

def greater_than_zero(gtz):
    for x in reversed(range(0, exponent)):
        if gtz >= 2 ** x:
            binary_arr[x] = 1
            gtz -= 2 ** x
        else:
            binary_arr[x] = 0
    return

"""
If the number is less than zero, convert it back into a positive number (x*-1) and pass to the 
"greater_than_zero()" function. When it gets the resulting binary number back from that function,
flip all of the bits and add 1 to the binary number to sign the now negative binary number
in two's compliment.
"""
def less_than_zero(ltz):
    greater_than_zero(ltz * -1)
    for x in reversed(range(0, exponent)):
        if binary_arr[x] == 1:
            binary_arr[x] = 0
        elif binary_arr[x] == 0:
            binary_arr[x] = 1
    add_one()
    return

def convert(bitlength,number):
	exponent = bitlength
	maxint = 2 ** exponent  # Calculates the maximum integer for the specified bit length to determine if good_num should be true
	good_num = False  # No number inputted yet, therefor false

	binary_arr = [None] * exponent  # Create an array the size of the bit length (variable: exponent)

	if (number < maxint) & (number > (maxint / -2)):
   		good_num = True
	else:
		return("badnum")

	if good_num is True:  # If good_num == True, determine how to create the binary number.
		if number > 0:  # If the base 10 number is > 0, call the function to create a positive unsigned binary number
			greater_than_zero(number)  # Pass the base 10 number to the function that does this
		elif number < 0:  # If the base 10 number is < 0, call the function to create a negative signed binary number
			less_than_zero(number)  # Pass the base 10 number to the function that does this
		elif number == 0:  # If the number is 0...
			binary_arr = [0] * exponent  # make the entire array that holds the binary number 0 also.

	for x in reversed(range(0, exponent)):
		print(binary_arr[x], end='')  # Print the array, all characters on the same line without stupid syntax included in the print.
	return(binary_arr)
