#!/usr/bin/env python3

import subprocess
import sys
import os
from cane_pole.alerts.mac_watcher import check_mac
# === Dependency Check ===
try:
    from scapy.all import *
except ImportError:
    print("[!] scapy is not installed. Try: pip install scapy")
    exit(1)

# === User Input ===
def get_user_input():
    print("=== Rogue Access Point Setup ===")
    interface = input("Enter the wireless interface (e.g., wlan0): ")
    ssid = input("Enter the SSID to broadcast: ")
    channel = input("Enter the channel to use (e.g., 6): ")
    passphrase = input("Enter the WPA2 passphrase: ")
    target_mac = input("[!] (Optional) Target MAC Address: " )
    return interface, ssid, channel, passphrase, target_mac


# === Generate hostapd.conf ===
def generate_hostapd_conf(
    interface, ssid, channel, passphrase, conf_file="hostapd.conf"
):
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
    with open(conf_file, "w") as f:
        f.write(config.strip())
    print(f"[+] hostapd config written to {conf_file}")


# === Start hostapd ===
def start_hostapd(conf_file="hostapd.conf", target_mac=None):
    try:
        print("[+] Starting hostapd...")
        proc = subprocess.Popen(
            ["hostapd", conf_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )

        for line in proc.stdout:
            print("[hostapd] " + line.strip())
            if target_mac:
                check_mac(line, target_mac)

    except FileNotFoundError:
        print("[!] hostapd not found. Please install it with: sudo apt install hostapd")

# === Main Entry Point ===
def main():
    if os.geteuid() != 0:
        print("[-] This script must be run with sudo/root privileges.")
        sys.exit(1)

    interface, ssid, channel, passphrase, target_mac = get_user_input()
    generate_hostapd_conf(interface, ssid, channel, passphrase)
    start_hostapd()


# === Entry point for pipx or direct execution ===
def run():
    main()
