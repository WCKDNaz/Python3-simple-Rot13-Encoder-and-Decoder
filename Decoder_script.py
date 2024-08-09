#!/usr/bin/python3
## Decoder Code
import codecs
print ("Enter ROT-13 Cipher that you'd like to decode")
ciphertext = input()
decode = codecs.decode(ciphertext,'rot_13')
print ("Your decoded ciphertext is: ", decode)
