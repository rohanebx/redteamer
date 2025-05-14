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

def run_nmap_scan(ip):
    """Run Nmap with IDS/IPS evasion techniques on SMB & RPC ports."""
    ports = "135,137,138,139,445"
    
    command = [
        "nmap", "-p", ports,
        "-sS",  # Stealth SYN scan
        "--mtu", "16", "-f",  # Packet fragmentation
        "-D", "RND:10",  # Decoy scan with 10 random IPs
        "--data-length", "200",  # Add random data to packets
        "--spoof-mac", "00:11:22:33:44:55",  # Fake MAC address
        "--randomize-hosts",  # Randomize scan order
        "--scan-delay", "10s", "-T0"  # Slow and stealthy scan
    ]

    print(f"\nRunning Nmap stealth scan on {ip} for SMB & RPC ports...\n")
    subprocess.run(command + [ip])

def main():
    check_nmap_installed()
    target_ip = get_target_ip()
    run_nmap_scan(target_ip)

if __name__ == "__main__":
    main()
