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

This project was created for educational purposes as part of a HD project, and it should only be used in simulated environments for educational or research purposes. As this was created for a HD project, it doesn't contain the proper level of security in the encryption for real-world applications.

## Purpose

The primary purpose of this is to encrypt all files in a given folder. The key for encryption is derived from a code word, which ensures that the files can only be decrypted using the same code word. The encryption algorithm used is AES, with padding applied to ensure the file data fits within block size constraints. The folder consists of a single Python file that handles key derivation, file encryption, and folder traversal to encrypt multiple files at once.

## Files

There are two versions of this script, the first one is the `encrypt.py` which has the interaction in terminal, as well as one involving no interaction that takes the arguments when running the file which is `encrypt_no_interact.py`.

### Code Breakdown

- **Key Derivation:** The key for AES encryption is derived from a user-supplied code word using the PBKDF2 (Password-Based Key Derivation Function 2) method with the SHA-256 hashing algorithm. This process ensures the key is securely generated from the code word.
  
- **File Encryption:** AES encryption with CBC mode is applied to individual files. The encryption function first pads the data, generates an IV (Initialisation Vector), and then encrypts the data. The IV is prepended to the encrypted data for use in decryption.

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

### Example Usage of `encrypt.py`

```bash
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    ██╗████████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝    ██║╚══██╔══╝
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║       ██║   ██║   
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║       ██║   ██║   
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║       ██║   ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝       ╚═╝   ╚═╝  

Welcome to the Encrypt it! Your favourite encryption tool.
Enter the folder path to encrypt and a code word to encrypt the files.
Then sit back and relax while we encrypt your files. 
Because this is totally safe and not at all suspicious...

Enter the folder path to encrypt: /home/tva/Documents/Important_TVA_Files
Enter the code word: TVA_SECRET_KEY

Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Project_Plan.txt
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Access_Credentials.txt
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Strategy_Report.docx
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Budget_2024.xlsx
Encrypted /home/tva/Documents/Important_TVA_Files/TVA_Internal_Memo.pdf
All files in the folder have been encrypted.
```

In this example, the user provides the folder path `/home/tva/Documents/Important_TVA_Files` and the code word `TVA_SECRET_KEY`.

### Example Usage of `encrypt_no_interact.py`

```bash
python encrypt_no_interact.py -l /home/tva/Documents/Important_TVA_Files -p TVA_SECRET_KEY
```

Which gives
  
```bash
All files in the folder have been encrypted.
```

All files in `/home/tva/Documents/Important_TVA_Files` will be encrypted and saved back to their original locations.

### Requirements

The project relies on the following Python libraries:

- `cryptography` library for AES encyption and key derivation.

```bash
pip install cryptography
```

---

> For All Time Always. 🕰️🌐

```shell
██████╗ ██████╗ ███████╗███████╗███████╗██╗   ██╗   
██╔══██╗██╔══██╗██╔════╝██╔════╝╚══███╔╝╚██╗ ██╔╝   
██████╔╝██████╔╝█████╗  █████╗    ███╔╝  ╚████╔╝    
██╔══██╗██╔══██╗██╔══╝  ██╔══╝   ███╔╝    ╚██╔╝     
██████╔╝██║  ██║███████╗███████╗███████╗   ██║   ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝
```
