# CTFtools
A collection of CTF tools for solving challs

## Running the scripts

Be in the root folder and run your desired script with the following command (without .py):
```shell
python -m <FOLDER_NAME>.<TOOL_NAME> <flags and arguments>
```

## TOOLS Overview

- **Network Recon**
  - Search_and_Sum_Ports.py

## TOOLS Explained

#### Network_Recon/Search_and_Sum_Ports.py
```shell
python -m Network_Recon.Search_and_Sum_Ports -u TARGET_URL -p TARGET_PORTRANGE
```

This tool uses *nmap* to check which ports are open in the port range specified at the target url specified. It uses TCP connections to achieve this. The open ports are summed up and outputed to screen as well as every open port and the service running on the port.

## Ideas for tools

Please create a New Issue and I'll have a crack at it when I have time.
https://github.com/fkihle/CTFtools/issues/new/choose


## Disclaimer

The tools provided are **ONLY** meant for use in official CTF events. ANY use of these outside of CTF events may be **illegal** and result in **fines** and/or **prison sentencing**. The author will **NOT** be held responsible for your actions. The tools do not have any form of use or target validation, so accidentaly breaching scope boundaries is on **YOU**. 

If your not absolutely sure of what your are doing: **DON'T USE THESE TOOLS**.

With that out of the way; Happy CTFing!