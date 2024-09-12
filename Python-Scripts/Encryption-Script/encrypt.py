import os
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes 

# Take the code word and salt as bytes and the number of iterations as an integer
def derive_key(code_word, salt=b'salt_', iterations=100000):
    # Use PBKDF2 to derive a key from the code word
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=iterations, backend=default_backend())
    # Directly return the derived key without encoding it
    return kdf.derive(code_word.encode())

# Function to specify the file path and the key to encrypt the file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f: data = f.read()

    # Pad the data to be a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    iv = os.urandom(16)

    # Create the cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Prepend the IV to the encrypted data (needed for decryption)
    encrypted_data_with_iv = iv + encrypted_data

    # Write the encrypted data back to the file
    with open(file_path, 'wb') as f: f.write(encrypted_data_with_iv)

    print(f"Encrypted {file_path}")

# Function to encrypt all files in the folder
def encrypt_folder(folder_path, code_word):
    # Derive a key from the code word
    key = derive_key(code_word)

    # Walk through the folder and encrypt each file
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key)

    print("All files in the folder have been encrypted.")

def display_title():
    print(r"""
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    ██╗████████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝    ██║╚══██╔══╝
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║       ██║   ██║   
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║       ██║   ██║   
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║       ██║   ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝       ╚═╝   ╚═╝  

Welcome to the Encrypt it! Your favourite encryption tool.
Enter the folder path to encrypt and a code word to encrypt the files.
Then sit back and relax while we encrypt your files.
          """)

if __name__ == "__main__":
    display_title()
    folder_to_encrypt = input("Enter the folder path to encrypt: ")
    code_word = input("Enter the code word: ")
    encrypt_folder(folder_to_encrypt, code_word)