import os
import subprocess

def check_nmap_installed():
    """Check if Nmap is installed."""
    try:
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        print("Error: Nmap is not installed. Install it using 'sudo apt install nmap' (Linux) or download it from https://nmap.org/download.html (Windows).")
        exit(1)

def get_target_ip():
    """Prompt the user for the target IP address."""
    ip = input("Enter the target IP address: ").strip()
    return ip

def choose_target_os():
    """Prompt the user to choose a target OS."""
    print("\nChoose target OS:")
    print("1 - Android")
    print("2 - Windows")
    
    choice = input("Enter choice (1 or 2): ").strip()
    if choice == "1":
        return "android"
    elif choice == "2":
        return "windows"
    else:
        print("Invalid choice. Please select 1 or 2.")
        return choose_target_os()

def run_nmap_scan(ip, os_type):
    """Run the appropriate Nmap scan based on the OS type."""
    if os_type == "android":
        ports = "20,21,22,25,80,443,110,143,445,500,587,993,995,1194,1433,5060,5222,554,1900,3799"
    else:  # Windows
        ports = "21,25,53,80,110,135,137,138,139,143,443,445,3389,631,389,636,3268,3269,514,3306,5900,6379,27017,8080,8000"

    command = [
        "nmap", "-p", ports,
        "-sV", "--source-port", "53", "--scan-delay", "5s", "-T2", ip
    ]

    print("\nRunning Nmap scan on", ip, "for", os_type, "services...\n")
    subprocess.run(command)

def main():
    check_nmap_installed()
    target_ip = get_target_ip()
    os_type = choose_target_os()
    run_nmap_scan(target_ip, os_type)

if __name__ == "__main__":
    main()
