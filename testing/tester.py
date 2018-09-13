#!/usr/bin/python3
import base64_cipher
encrypted = base64_cipher.encrypt("Hello world")
print(encrypted)

decrypted = base64_cipher.decrypt(encrypted)
print(decrypted)
