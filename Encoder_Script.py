#!/usr/bin/python3
## Encoder Code
import codecs
print ("Enter text that you'd like to encode in ROT-13")
plaintext = input()
ciphertext = codecs.encode(plaintext,'rot_13')
print ("Your cipher is: ", ciphertext)
