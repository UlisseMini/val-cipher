#!/usr/bin/python3
# Val cipher by valvate
# Use generate.py to generate a key for yourself then replace the following:

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
key =      'wenKOT60gYRszjQCqm58ZJPELV7iUoh9INkXyvuMt3clSpWB2x4fHFAba1GrDd'

# Hex encoder #
from base64 import b16decode, b16encode 

def hexencode(data):
    data = data.encode('utf-8')
    encrypted = b16encode(data)
    encrypted = encrypted.decode('utf-8')
    return encrypted

def hexdecode(data):
    # Python hates lowercase in base16
    data = data.upper()
    data = data.encode('utf-8')
    decrypted = b16decode(data)
    decrypted = decrypted.decode('utf-8')
    return decrypted

# Mono cipher #
def encrypt(data):
    # Encodes data into base16
    data = hexencode(data)
    indexVals = [alphabet.index(char.lower()) for char in data]
    return ''.join(key[indexKey] for indexKey in indexVals)

def decrypt(data):
    indexVals = [key.index(char) for char in data]
    deciphered = ''.join(alphabet[indexKey] for indexKey in indexVals)
    deciphered = hexdecode(deciphered)
    return deciphered
