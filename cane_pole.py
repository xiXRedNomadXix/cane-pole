#!/usr/bin/env python3

import subprocess
import sys
import os

# === Dependency Check ===
try:
    from scapy.all import *
except ImportError:
    print("[!] scapy is not installed. Try: pip install scapy")
    exit(1)

try:
    import pyroute2
except ImportError:
    print("[!] pyroute2 is not installed. Try: pip install pyroute2")
    exit(1)

# === User Input ===
def get_user_input():
    print("=== Rogue Access Point Setup ===")
    interface = input("Enter the wireless interface (e.g., wlan0): ")
    ssid = input("Enter the SSID to broadcast: ")
    channel = input("Enter the channel to use (e.g., 6): ")
    passphrase = input("Enter the WPA2 passphrase: ")
    return interface, ssid, channel, passphrase

# === Generate hostapd.conf ===
def generate_hostapd_conf(interface, ssid, channel, passphrase, conf_file='hostapd.conf'):
    config = f"""
interface={interface}
driver=nl80211
ssid={ssid}
hw_mode=g
channel={channel}
auth_algs=1
wpa=2
wpa_passphrase={passphrase}
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP CCMP
ignore_broadcast_ssid=0
"""
    with open(conf_file, 'w') as f:
        f.write(config.strip())
    print(f"[+] hostapd config written to {conf_file}")

# === Start hostapd ===
def start_hostapd(conf_file='hostapd.conf'):
    try:
        print('[+] Starting hostapd...')
        subprocess.run(["hostapd", conf_file])
    except FileNotFoundError:
        print('[-] hostapd not found. Please install it with: sudo apt install hostapd')

# === Main Entry Point ===
def main():
    if os.geteuid() != 0:
        print("[-] This script must be run with sudo/root privileges.")
        sys.exit(1)

    interface, ssid, channel, passphrase = get_user_input()
    generate_hostapd_conf(interface, ssid, channel, passphrase)
    start_hostapd()

# Entry point for pipx or direct execution
if __name__ == "__main__":
    main()
    #!/usr/bin/env python3

    import subprocess
    import sys
    import os

    # === Dependency Check ===
    try:
        from scapy.all import *
    except ImportError:
        print("[!] scapy is not installed. Try: pip install scapy")
        exit(1)

    try:
        import pyroute2
    except ImportError:
        print("[!] pyroute2 is not installed. Try: pip install pyroute2")
        exit(1)

    # === User Input ===
    def get_user_input():
        print("=== Rogue Access Point Setup ===")
        interface = input("Enter the wireless interface (e.g., wlan0): ")
        ssid = input("Enter the SSID to broadcast: ")
        channel = input("Enter the channel to use (e.g., 6): ")
        passphrase = input("Enter the WPA2 passphrase: ")
        return interface, ssid, channel, passphrase

    # === Generate hostapd.conf ===
    def generate_hostapd_conf(interface, ssid, channel, passphrase, conf_file='hostapd.conf'):
        config = f"""
    interface={interface}
    driver=nl80211
    ssid={ssid}
    hw_mode=g
    channel={channel}
    auth_algs=1
    wpa=2
    wpa_passphrase={passphrase}
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP CCMP
    ignore_broadcast_ssid=0
    """
        with open(conf_file, 'w') as f:
            f.write(config.strip())
        print(f"[+] hostapd config written to {conf_file}")

    # === Start hostapd ===
    def start_hostapd(conf_file='hostapd.conf'):
        try:
            print('[+] Starting hostapd...')
            subprocess.run(["hostapd", conf_file])
        except FileNotFoundError:
            print('[-] hostapd not found. Please install it with: sudo apt install hostapd')

    # === Main Entry Point ===
    def main():
        if os.geteuid() != 0:
            print("[-] This script must be run with sudo/root privileges.")
            sys.exit(1)

        interface, ssid, channel, passphrase = get_user_input()
        generate_hostapd_conf(interface, ssid, channel, passphrase)
        start_hostapd()

    # Entry point for pipx or direct execution
    if __name__ == "__main__":
        main()
