#!/usr/bin/python3

# Ops Challenge 06
# Dylan Dempsey
# 04/24/23
# Encryption

# Main

# Install Cryptography library
pip install cryptography

# Import necessary libraries and modules
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
from cryptography.hazmat.backends import default_backend
import base64
import getpass


# Function to generate a Fernet key based on a user-provided password
def generate_key():
    # Prompt the user for a password
    password = getpass.getpass("Enter password: ")
    # Encode the password as bytes
    password = password.encode()

    # Create a key derivation function using the ConcatKDFHash method
    kdf = ConcatKDFHash(
        algorithm=hashes.SHA256(),
        length=32,
        otherinfo=None,
        backend=default_backend(),
    )

    # Derive the key from the password and encode it in URL-safe base64 format
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


# Function to encrypt a file
def encrypt_file(filepath, key):
    # Create a Fernet object with the provided key
    fernet = Fernet(key)
    # Read the file's content
    with open(filepath, "rb") as file:
        content = file.read()

    # Encrypt the content
    encrypted_content = fernet.encrypt(content)

    # Write the encrypted content back to the file
    with open(filepath, "wb") as file:
        file.write(encrypted_content)


# Function to decrypt a file
def decrypt_file(filepath, key):
    # Create a Fernet object with the provided key
    fernet = Fernet(key)
    # Read the encrypted file's content
    with open(filepath, "rb") as file:
        encrypted_content = file.read()

    # Decrypt the content
    content = fernet.decrypt(encrypted_content)

    # Write the decrypted content back to the file
    with open(filepath, "wb") as file:
        file.write(content)


# Function to encrypt a message
def encrypt_message(message, key):
    # Create a Fernet object with the provided key
    fernet = Fernet(key)
    # Encrypt the message
    encrypted_message = fernet.encrypt(message.encode())
    # Print the encrypted message
    print("Encrypted message:", encrypted_message.decode())


# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    # Create a Fernet object with the provided key
    fernet = Fernet(key)
    # Decrypt the message
    message = fernet.decrypt(encrypted_message.encode())
    # Print the decrypted message
    print("Decrypted message:", message.decode())


# Main function to run the program
def main():
    # Generate the Fernet key
    key = generate_key()

    # Print the available modes
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    # Prompt the user to enter a mode number
    mode = int(input("Enter the mode number: "))

    # Perform actions based on the selected mode
    if mode in [1, 2]:
        # Prompt the user for the file path
        filepath = input("Enter the filepath: ")

        # Encrypt or decrypt the file based on the selected mode
        if mode == 1:
            encrypt_file(filepath, key)
            print("
