#!/usr/bin/python3
# Val cipher by valvate
# Use generate.py to generate a key for yourself then replace the following:

alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890= '
key =      'F7dJ89aph5r40Rw6yUAzoqm897Ht0CBviWSD5Esbg2M2VQXGxcOlT6fjPnkuL4e1Y1IZ33KN= '

# Mono cipher #
def encrypt(data):
    indexVals = [alphabet.index(char.lower()) for char in data]
    return ''.join(key[indexKey] for indexKey in indexVals)

def decrypt(data):
    indexVals = [key.index(char) for char in data]
    return ''.join(alphabet[indexKey] for indexKey in indexVals)
