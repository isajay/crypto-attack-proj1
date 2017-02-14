from roots import *
from Crypto.Hash import SHA
import sys
import math

message = sys.argv[1]

# Your code to forge a signature goes here.
hex_string = "0001"
for i in range(0, 90):
	hex_string += "FF"
hex_string += "003021300906052B0E03021A05000414"
hex_string += SHA.new(message).hexdigest()
#print hex_string
for i in range(0, 128):
	hex_string += "01"
#print hex_string
dec = bytes_to_integer(hex_string.decode("hex"))
# print math.pow(2, 1024)
# dec *= math.pow(2, 1024)
# print dec

root, is_exact = integer_nthroot(dec, 3)
print integer_to_base64(root)
