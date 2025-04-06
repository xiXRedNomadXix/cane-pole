#!/usr/bin/env python3

from scapy.all import *
import subprocess
import sys
import os
import pyroute2


# Starts an evil twin using a hostapd.conf file
# Should look something like this:
# interface=wlan0
# ssid=YourRealSSID
# channel=6
# hw_mode=g
# auth_algs=1
# wpa=2
# wpa_passphrase=YourWiFiPassword
# wpa_key_mgmt=WPA-PSK
# wpa_pairwise=TKIP CCMP
#
def get_user_input():
    print("=== Rogue Access Point Setup ===")
    interface = input("Enter the wireless interface (e.g., wlan0): ")
    ssid = input("Enter the SSID to broadcast: ")
    channel = input("Enter the channel to use (e.g., 6): ")
    passphrase = input("Enter the WPA2 passphrase: ")

    return interface, ssid, channel, passphrase
get_user_input()

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

def start_hostapd(conf_file='hostapd.conf'):
    try:
        print('[+] Starting hostapd...')
        subprocess.run(["hostapd", conf_file])
    except FileNotFoundError:
        print('[-] hostapd not found. Please install it with; sudo apt install hostapd')

if __name__ == '__main__':
    if os.geteuid() != 0:
            print("[-] This script must be run with sudo/root privileges.")
            sys.exit(1)

    interface, ssid, channel, passphrase = get_user_input()
    generate_hostapd_conf(interface, ssid, channel, passphrase)
    start_hostapd()
