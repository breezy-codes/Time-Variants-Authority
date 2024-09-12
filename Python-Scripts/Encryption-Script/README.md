```bash
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    ██╗████████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝    ██║╚══██╔══╝
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║       ██║   ██║   
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║       ██║   ██║   
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║       ██║   ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝       ╚═╝   ╚═╝  

Welcome to the Encryption Script! Enter the folder path to encrypt and a code word to encrypt the files. 
```

This project provides a Python-based tool to encrypt all files within a specified folder using AES (Advanced Encryption Standard) encryption. The files are securely encrypted with a key derived from a user-provided code word, making it an efficient way to protect sensitive data. The project makes use of the `cryptography` library and applies AES encryption in CBC (Cipher Block Chaining) mode.

## Disclaimer

This project was created for educational purposes as part of a HD project, and it should only be used in simulated environments for educational or research purposes. The use of phishing emails for malicious intent is illegal and unethical. As this was created for a HD project, it doesn't contain the proper level of security for real-world applications.

## Purpose

The primary purpose of this project is to encrypt all files in a given folder. The key for encryption is derived from a code word, which ensures that the files can only be decrypted using the same code word. The encryption algorithm used is AES, with padding applied to ensure the file data fits within block size constraints. The folder consists of a single Python file that handles key derivation, file encryption, and folder traversal to encrypt multiple files at once.

### Code Breakdown

- **Key Derivation:** The key for AES encryption is derived from a user-supplied code word using the PBKDF2 (Password-Based Key Derivation Function 2) method with the SHA-256 hashing algorithm. This process ensures the key is securely generated from the code word.
  
- **File Encryption:** AES encryption with CBC mode is applied to individual files. The encryption function first pads the data, generates an IV (Initialization Vector), and then encrypts the data. The IV is prepended to the encrypted data for use in decryption.

- **Folder Encryption:** The tool walks through all files in the specified folder and encrypts each one using the derived key.

### Functions

1. `derive_key(code_word, salt=b'salt_', iterations=100000)`:
   - **Purpose:** Generates a cryptographic key from the given code word using the PBKDF2HMAC function.
   - **Parameters:**
     - `code_word`: A string input from the user, used to derive the key.
     - `salt`: A byte string used to add randomness to the key derivation process (default is `b'salt_'`).
     - `iterations`: The number of iterations for the PBKDF2 function (default is 100,000).
   - **Returns:** A 32-byte key to be used for AES encryption.

2. `encrypt_file(file_path, key)`:
   - **Purpose:** Encrypts a single file using AES in CBC mode.
   - **Parameters:**
     - `file_path`: The path to the file to be encrypted.
     - `key`: The encryption key derived from the code word.
   - **Operation:**
     1. Reads the file and applies PKCS7 padding to the data.
     2. Generates a random IV and creates a cipher object with AES and CBC mode.
     3. Encrypts the padded data, prepends the IV, and writes the result back to the file.

3. `encrypt_folder(folder_path, code_word)`:
   - **Purpose:** Encrypts all files within the specified folder by calling the `encrypt_file()` function for each file.
   - **Parameters:**
     - `folder_path`: The path to the folder containing files to encrypt.
     - `code_word`: The user-provided string used to derive the encryption key.
   - **Operation:** Walks through all files in the folder and encrypts each one.

### Requirements

The project relies on the following Python libraries:

- `cryptography` library for AES encyption and key derivation.

```bash
pip install cryptography
```

### Example Usage

```bash
Enter the folder path to encrypt: /home/tva/Documents/Important_TVA_Files
Enter the code word: TVA_SECRET_KEY
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Project_Plan.txt
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Access_Credentials.txt
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Strategy_Report.docx
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Budget_2024.xlsx
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Internal_Memo.pdf
All files in the folder have been encrypted.
```

All files in `/home/tva/Documents/Important_TVA_Files` will be encrypted and saved back to their original locations.

### Example Encryption Output

Once the encryption is complete, files in the specified folder will no longer be readable in their original form. The IV is stored within the encrypted file, which ensures that the decryption process is deterministic when using the correct key.

> For All Time Always. 🕰️🌐

```shell
██████╗ ██████╗ ███████╗███████╗███████╗██╗   ██╗   
██╔══██╗██╔══██╗██╔════╝██╔════╝╚══███╔╝╚██╗ ██╔╝   
██████╔╝██████╔╝█████╗  █████╗    ███╔╝  ╚████╔╝    
██╔══██╗██╔══██╗██╔══╝  ██╔══╝   ███╔╝    ╚██╔╝     
██████╔╝██║  ██║███████╗███████╗███████╗   ██║   ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝
```
