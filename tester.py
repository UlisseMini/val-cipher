#!/usr/bin/python3
import val_cipher
encrypted = val_cipher.encrypt("Hello world")
print(encrypted)

decrypted = val_cipher.decrypt(encrypted)
print(decrypted)
