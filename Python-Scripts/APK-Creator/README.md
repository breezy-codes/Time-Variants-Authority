```bash
 █████╗ ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
███████║██████╔╝█████╔╝     ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██╔══██║██╔═══╝ ██╔═██╗     ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║     ██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

This project provides a bash script to automate the process of generating a reverse TCP payload in an Android APK using `msfvenom`, followed by signing and aligning the APK. This script simplifies the process by automating key steps, such as creating the payload, signing the APK, and aligning it for optimal performance.

## Disclaimer

This script was created for educational purposes as part of a HD project and should only be used in simulated environments for educational or research purposes. The use of malicious payloads, reverse shells, or APK signing for unethical or illegal purposes is strictly forbidden and punishable by law.

## Purpose

The purpose of this script is to automate the process of generating and signing an APK with a reverse TCP payload for my HD project. The APK is created using `msfvenom`, then signed with a custom keystore, and aligned for optimisation. This process aids in making the APK look more legitimate and bypass security checks on Android devices.

## Project Structure

The script is a single Bash file that handles APK generation, signing, and alignment.

### Code Breakdown

- **Payload Generation:** The script uses `msfvenom` to generate an Android APK embedded with a reverse TCP payload.
- **Keystore Creation:** If a keystore does not exist, the script will generate one with predefined values. This keystore is required to sign the APK.
- **APK Signing:** The script uses `jarsigner` to sign the generated APK with the keystore, making it valid for installation on an Android device.
- **APK Alignment:** The APK is aligned using `zipalign` for optimal performance on the target device.

### Script Breakdown

All the variables are set at the beginning of the file, allowing for an easy change of IP address or port and that sort of thing. It also contains all the information of the "company" thats being used for the APK signing.

1. **Set Variables**:
   - `LHOST` and `LPORT`: The local host and port for the reverse TCP payload.
   - `APK_NAME` and `OUTPUT_APK_NAME`: File names for the generated and final APK.
   - `KEYSTORE`, `ALIAS`, `KEYALG`, `KEYSIZE`, `VALIDITY`, `KEYPASS`, and `APKPASS`: Parameters for the keystore and signing process.
   - `DESKTOP_PATH`: The path where the APK and other files will be stored.
2. **Generate APK with Reverse TCP Payload**:
   - The script generates the APK using `msfvenom` with the specified `LHOST` and `LPORT`.
   - If the APK generation fails, the script exits with an error.
3. **Create Keystore (if not already present)**:
   - If the specified keystore file does not exist, it creates one using `keytool` with predefined information (organization, city, etc.).
4. **Sign the APK**:
   - The generated APK is signed using `jarsigner` with the custom keystore.
5. **Align the APK**:
   - The APK is aligned using `zipalign`, which optimizes it for performance on Android devices.

### Requirements

The script relies on several tools:

- `msfvenom` for generating the reverse TCP payload and APK.
- `keytool` for generating the keystore.
- `jarsigner` for signing the APK.
- `zipalign` for aligning the APK.

### Example Output

```bash
Enter the folder path to encrypt: /home/tva/Desktop
 █████╗ ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
███████║██████╔╝█████╔╝     ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██╔══██║██╔═══╝ ██╔═██╗     ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║     ██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Generating APK with reverse TCP payload...
Created: /home/Desktop/malware.apk

Creating keystore...
Keystore generation complete.

Signing APK...
Signed: /home/tva/Desktop/malware.apk

Aligning APK...
Aligned APK is: /home/Desktop/JetSki-App.apk

Done. Signed and aligned APK is: /home/Desktop/JetSki-App.apk
```

> For All Time Always. 🕰️🌐

```shell
██████╗ ██████╗ ███████╗███████╗███████╗██╗   ██╗   
██╔══██╗██╔══██╗██╔════╝██╔════╝╚══███╔╝╚██╗ ██╔╝   
██████╔╝██████╔╝█████╗  █████╗    ███╔╝  ╚████╔╝    
██╔══██╗██╔══██╗██╔══╝  ██╔══╝   ███╔╝    ╚██╔╝     
██████╔╝██║  ██║███████╗███████╗███████╗   ██║   ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝
```
