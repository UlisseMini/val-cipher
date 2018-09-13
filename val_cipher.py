#!/usr/bin/python3
# Val cipher by valvate
# Use generate.py to generate a key for yourself then replace the following:

alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '
key =      'F7dJ89aph5r40Rw6yUAzoqm897Ht0CBviWSD5Esbg2M2VQXGxcOlT6fjPnkuL4e1Y1IZ33KN '

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
    # This works
    # Encodes data into base16
    data = hexencode(data)
    indexVals = [alphabet.index(char.lower()) for char in data]
    return ''.join(key[indexKey] for indexKey in indexVals)

def decrypt(data):
    # This does not
    indexVals = [key.index(char) for char in data]
    deciphered = ''.join(alphabet[indexKey] for indexKey in indexVals)
    deciphered = hexdecode(deciphered)
    return deciphered
