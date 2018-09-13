#!/usr/bin/python3
import simple
encrypted = simple.encrypt("Hello world")
print(encrypted)

decrypted = simple.decrypt(encrypted)
print(decrypted)
