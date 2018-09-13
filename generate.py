#!/usr/bin/python3
# Sciprt to generate random alphabet for ciphers
# Created by valvate / peep

from random import shuffle
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
alphabet = alphabet + alphabet.upper()
print(alphabet)
alphabet = list(alphabet)

# Shuffles the alphabet array / list
shuffle(alphabet)

key = ''.join(alphabet)
print(key)
