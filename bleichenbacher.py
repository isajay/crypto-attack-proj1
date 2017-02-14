from roots import *
from Crypto.Hash import SHA
import sys
import math

message = sys.argv[1]

# Your code to forge a signature goes here.
hex_string = "0001"
for i in range(0, 48):
	hex_string += "FF"
hex_string += "003021300906052B0E03021A05000414"
hex_string += SHA.new(message).hexdigest()

for i in range(0, 512 - len(hex_string)):
	hex_string += "F"
dec = bytes_to_integer(hex_string.decode("hex"))

root, is_exact = integer_nthroot(dec, 3)
print integer_to_base64(root)
