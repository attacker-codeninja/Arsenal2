# Payload Shortcut Generator

This tool creates OS-specific shortcuts (`.lnk` for Windows, `.desktop` for Linux) that download and execute a file from a given URL. It's designed for educational purposes in testing payload delivery mechanisms across Windows and Linux environments.

## Features
- **Cross-Platform**: Generates shortcuts for both Windows and Linux.
- **Automatic Encoding**: Encodes payload commands in Base64 for stealth and reliability.
- **Unique Filenames**: Randomly generates filenames for downloaded files to avoid detection.

## How It Works
- For **Windows**, it creates a `.lnk` file that uses PowerShell to download and execute the target file.
- For **Linux**, it creates a `.desktop` file to achieve the same effect using `bash` and `wget`.

## Requirements
- Python 3
- `win32com.client` module (only on Windows)
- Administrator/root privileges may be required for execution in certain environments.


## Install dependencies (Windows only):

`pip3 install pywin32`

## Usage

Run the script and enter the URL of the file you wish to create a payload shortcut for.

`python3 payload_shortcut.py`

Enter the URL: The URL should link to the file you want to download and execute.
Shortcut Creation: The script generates a `.lnk` file on Windows or a `.desktop` file on Linux on the user’s Desktop.
Execution: Opening the shortcut initiates the download and execution of the specified file.

Code Structure

    create_windows_shortcut: Creates a .lnk file on Windows, specifying the payload command with PowerShell.
    create_linux_shortcut: Generates a .desktop file on Linux with an encoded bash command.
    generate_encoded_command: Encodes the download-and-execute command in Base64.
    main: Determines the OS, prompts for the URL, and calls the appropriate shortcut creation function.

Warnings

    For educational purposes only: Use responsibly in authorized environments.
    Do not run: Running unauthorized payloads is illegal and unethical.
    Detection: Generated shortcuts may trigger antivirus software.