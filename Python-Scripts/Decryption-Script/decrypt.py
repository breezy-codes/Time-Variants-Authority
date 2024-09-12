import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Function to derive a key from the code word
def derive_key(code_word, salt=b'salt_', iterations=100000):
    # Use PBKDF2 to derive a key from the code word
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=iterations, backend=default_backend())
    # Directly return the derived key without encoding it
    return kdf.derive(code_word.encode())

# Function to decrypt file data
def decrypt_file(file_path, key):
    try:
        # Read the encrypted file content
        with open(file_path, 'rb') as f: encrypted_data_with_iv = f.read()

        # The first 16 bytes are the IV, the rest is the encrypted data
        iv = encrypted_data_with_iv[:16]
        encrypted_data = encrypted_data_with_iv[16:]

        # Create the cipher object using the same key and IV
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt the data
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Remove padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()

        # Write the decrypted data back to the file
        with open(file_path, 'wb') as f: f.write(data)

        print(f"Decrypted {file_path}")
        return True
    except (ValueError, InvalidSignature):
        # If decryption fails, return False
        print(f"Failed to decrypt {file_path}. Possible incorrect key.")
        return False

# Function to decrypt all files in the folder
def decrypt_folder(folder_path, code_word):
    # Derive a key from the code word
    key = derive_key(code_word)

    # Walk through the folder and decrypt each file
    success = True
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            success = decrypt_file(file_path, key)
            if not success:
                return False  # If any file fails to decrypt, stop and return False
    return True

def display_title():
    print(r"""
██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    ██╗████████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝    ██║╚══██╔══╝
██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║       ██║   ██║   
██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║       ██║   ██║   
██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║        ██║       ██║   ██║   
╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝       ╚═╝   ╚═╝   

Welcome to Decrypt it! Your favourite decryption tool.
Enter the folder path to decrypt and the code word to decrypt the files.
Then sit back and relax while we decrypt your files.
Be warned... you only have 5 attempts to enter the correct code word.
          """)

if __name__ == "__main__":
    display_title()
    folder_to_decrypt = input("Enter the folder path to decrypt: ")

    max_attempts = 5
    attempts = 0

    # Allow up to 5 attempts for the user to input the correct code word
    while attempts < max_attempts:
        code_word = input(f"Attempt {attempts + 1}/{max_attempts} - Enter the code word: ")

        # Try to decrypt the folder with the provided code word
        if decrypt_folder(folder_to_decrypt, code_word):
            print("Decryption successful.")
            break
        else:
            attempts += 1
            print(f"Attempt {attempts} failed. Please try again.")
        
        # If the maximum number of attempts is reached
        if attempts == max_attempts:
            print("Maximum attempts reached. Decryption failed.")