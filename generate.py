#!/usr/bin/python3
# Sciprt to generate random alphabet for ciphers
# Created by valvate / peep

from random import shuffle
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet = alphabet + alphabet.upper() + '1234567890'
print(alphabet)
alphabet = list(alphabet)

# Shuffles the alphabet array / list
shuffle(alphabet)

key = ''.join(alphabet)
print(key)
