#!/usr/bin/python3
import val_cipher
print("""
        1: Encrypt
        2: Decrypt
        3: Exit""")
choices = ["1", "2", "3"]

choice = input("-> ")
while choice not in choices:
    choice = input("-> ")

if choice == "1":
    text = input("Text to encrypt\n-> ")
    encrypted = val_cipher.encrypt(text)
    print(encrypted)
if choice == "2":
    text = input("Text to decrypt\n-> ")
    decrypted = val_cipher.decrypt(text)
    print(decrypted)
