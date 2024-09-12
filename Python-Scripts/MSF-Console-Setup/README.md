```bash
███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
███████╗██████╔╝██║     ██║   ██║██║   ██║   
╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
███████║██║     ███████╗╚██████╔╝██║   ██║   
╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
```

This script automates the process of setting up and starting a Metasploit handler for a reverse TCP payload targeting Android devices. The purpose of this script is to simplify the process of starting a Metasploit session with predefined parameters (`LHOST`, `LPORT`, and `PAYLOAD`). It automatically launches Metasploit, configures the multi/handler module, and starts listening for incoming connections on the specified `LHOST` and `LPORT`.

## How It Works

- **Predefined Variables**:
  - `PAYLOAD`: Specifies the Metasploit payload (`android/meterpreter/reverse_tcp`).
  - `LHOST` and `LPORT`: Define the local host IP address and port for the reverse TCP connection.
  
- **Automated Metasploit Console Setup**: The script launches `msfconsole`, configures the multi/handler exploit with the specified payload and network parameters, and starts the listener in the background.

### Example Output

```bash
███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
███████╗██████╔╝██║     ██║   ██║██║   ██║   
╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
███████║██║     ███████╗╚██████╔╝██║   ██║   
╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
Loading Metasploit and Setting up the Handler
Using PAYLOAD: android/meterpreter/reverse_tcp
Using LHOST: 192.168.1.124
Using LPORT: 4444
```

### Requirements

- **Metasploit Framework**: The script requires the Metasploit Framework to be installed on the system.

> For All Time Always. 🕰️🌐

```shell
██████╗ ██████╗ ███████╗███████╗███████╗██╗   ██╗   
██╔══██╗██╔══██╗██╔════╝██╔════╝╚══███╔╝╚██╗ ██╔╝   
██████╔╝██████╔╝█████╗  █████╗    ███╔╝  ╚████╔╝    
██╔══██╗██╔══██╗██╔══╝  ██╔══╝   ███╔╝    ╚██╔╝     
██████╔╝██║  ██║███████╗███████╗███████╗   ██║   ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝
```
