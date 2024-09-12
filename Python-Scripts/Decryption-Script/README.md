```bash
██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    ██╗████████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝    ██║╚══██╔══╝
██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║       ██║   ██║   
██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║       ██║   ██║   
██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║        ██║       ██║   ██║   
╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝       ╚═╝   ╚═╝   

Welcome to the Decryption Script! Enter the folder path that needs to be decrypted.
Beware, there is only 5 attempts to enter the correct code word.
```

This project provides a Python-based tool to decrypt all files within a specified folder using AES (Advanced Encryption Standard) decryption. The files are decrypted with a key derived from a user-provided code word, ensuring that the original data can only be restored with the correct key. The tool handles decryption with AES in CBC (Cipher Block Chaining) mode, and it allows the user multiple attempts to enter the correct code word.

## Disclaimer

This project was created for educational purposes as part of a HD project, and it should only be used in simulated environments for educational or research purposes. The use of decryption tools for malicious intent is illegal and unethical. As this was created for a HD project, it doesn't contain the proper level of security for real-world applications.

## Purpose

The primary purpose of this project is to decrypt all files in a given folder. The key for decryption is derived from a code word that must match the one used during encryption. The decryption algorithm used is AES in CBC mode, with padding removed to restore the original file data.

## Project Structure

The project consists of a single Python file that handles key derivation, file decryption, and folder traversal to decrypt multiple files at once.

### Code Breakdown

- **Key Derivation:** The decryption key is derived from a user-supplied code word using the PBKDF2 (Password-Based Key Derivation Function 2) method with the SHA-256 hashing algorithm. This ensures that the same code word used for encryption must be used for decryption.
  
- **File Decryption:** AES decryption with CBC mode is applied to individual files. The function first reads the IV (Initialization Vector) from the file, decrypts the data, and removes padding to restore the original file content.

- **Folder Decryption:** The tool walks through all files in the specified folder and decrypts each one using the derived key. The user is allowed up to 5 attempts to enter the correct code word.

### Functions

1. `derive_key(code_word, salt=b'salt_', iterations=100000)`:
   - **Purpose:** Generates a cryptographic key from the given code word using the PBKDF2HMAC function.
   - **Parameters:**
     - `code_word`: A string input from the user, used to derive the key.
     - `salt`: A byte string used to add randomness to the key derivation process (default is `b'salt_'`).
     - `iterations`: The number of iterations for the PBKDF2 function (default is 100,000).
   - **Returns:** A 32-byte key to be used for AES decryption.

2. `decrypt_file(file_path, key)`:
   - **Purpose:** Decrypts a single file using AES in CBC mode.
   - **Parameters:**
     - `file_path`: The path to the file to be decrypted.
     - `key`: The decryption key derived from the code word.
   - **Operation:**
     1. Reads the IV from the file (the first 16 bytes).
     2. Creates a cipher object using AES and CBC mode.
     3. Decrypts the data and removes padding to restore the original content.
     4. Writes the decrypted data back to the file.

3. `decrypt_folder(folder_path, code_word)`:
   - **Purpose:** Decrypts all files within the specified folder by calling the `decrypt_file()` function for each file.
   - **Parameters:**
     - `folder_path`: The path to the folder containing files to decrypt.
     - `code_word`: The user-provided string used to derive the decryption key.
   - **Operation:** Walks through all files in the folder and decrypts each one.

### Requirements

The project relies on the following Python libraries:

- `cryptography` library for AES decryption and key derivation.

```bash
pip install cryptography
```

### Example Usage

```bash
Enter the folder path to decrypt: /home/tva/Documents/Important_TVA_Files
Attempt 1/5 - Enter the code word: TVA_KEY_WRONG
Failed to decrypt /home/tva/Documents/Important_TVA_Files/TVA_Project_Plan.txt. Possible incorrect key.
Attempt 1 failed. Please try again.
Attempt 2/5 - Enter the code word: TVA_SECRET_KEY
Decrypted /home/tva/Documents/Important_TVA_Files/TVA_Project_Plan.txt
Decrypted /home/tva/Documents/Important_TVA_Files/TVA_Access_Credentials.txt
Decrypted /home/tva/Documents/Important_TVA_Files/TVA_Strategy_Report.docx
Decrypted /home/tva/Documents/Important_TVA_Files/TVA_Budget_2024.xlsx
Decrypted /home/tva/Documents/Important_TVA_Files/TVA_Internal_Memo.pdf
Decryption successful.
```

All files in `/home/tva/Documents/Important_TVA_Files` will be decrypted and restored to their original state.

### Example Decryption Output

Once the decryption is complete, files in the specified folder will be restored to their readable form, assuming the correct code word was provided.

> For All Time Always. 🕰️🌐
