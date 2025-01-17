import os
import subprocess

def change_network_config(ip_address, subnet_mask, gateway):
    """
    Change the network configuration of the system.
    """
    try:
        command = f"netsh interface ip set address \"Ethernet\" static {ip_address} {subnet_mask} {gateway}"
        subprocess.run(command, shell=True, check=True)
        print("Network configuration changed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to change network configuration: {e}")

def change_screen_resolution(width, height):
    """
    Change the screen resolution of the system.
    """
    try:
        command = f"powershell -command \"Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Size = New-Object System.Drawing.Size({width}, {height})\""
        subprocess.run(command, shell=True, check=True)
        print("Screen resolution changed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to change screen resolution: {e}")

def main():
    print("QuickConfig - Quick Settings Configuration Tool")
    print("1. Change Network Configuration")
    print("2. Change Screen Resolution")
    choice = input("Select an option: ")

    if choice == '1':
        ip_address = input("Enter IP Address: ")
        subnet_mask = input("Enter Subnet Mask: ")
        gateway = input("Enter Gateway: ")
        change_network_config(ip_address, subnet_mask, gateway)
    elif choice == '2':
        width = input("Enter Screen Width: ")
        height = input("Enter Screen Height: ")
        change_screen_resolution(width, height)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()