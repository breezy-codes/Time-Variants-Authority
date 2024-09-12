```bash
███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
███████╗██████╔╝██║     ██║   ██║██║   ██║   
╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
███████║██║     ███████╗╚██████╔╝██║   ██║   
╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
```

These scripts automate the process of setting up and starting a Metasploit handler for reverse TCP payloads targeting Android, Windows, and Linux devices. The purpose of these scripts is to simplify the process of starting a Metasploit session with predefined parameters (`LHOST`, `LPORT`, and `PAYLOAD`). Each script automatically launches Metasploit, configures the multi/handler module, and starts listening for incoming connections on the specified `LHOST` and `LPORT` for their respective targets.

### Available Scripts

For all scripts the `LHOST` and `LPORT`: Define the local host IP address and port for the reverse TCP connection.

1. **Android Reverse TCP Handler Script**:
   - **Predefined Variables**:
     - `PAYLOAD`: Specifies the Metasploit payload (`android/meterpreter/reverse_tcp`).

2. **Windows Reverse TCP Handler Script**:
   - **Predefined Variables**:
     - `PAYLOAD`: Specifies the Metasploit payload (`windows/meterpreter/reverse_tcp`).
   
3. **Linux Reverse TCP Handler Script**:
   - **Predefined Variables**:
     - `PAYLOAD`: Specifies the Metasploit payload (`linux/x86/meterpreter/reverse_tcp` or `linux/x64/meterpreter/reverse_tcp` depending on the architecture).

### General Workflow

- **Automated Metasploit Console Setup**: Each script launches `msfconsole`, configures the multi/handler exploit with the appropriate payload and network parameters for the specific target platform (Android, Windows, or Linux), and starts the listener in the background. This automation ensures that the process of initiating a reverse TCP connection is fast and error-free across different platforms.

As each script has the `payload`, `LHOST`, and `LPORT` predefined, they can easily be modified before execution to suit the specific requirements of the user.

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
