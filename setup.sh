#!/usr/bin/env bash

echo "[+] Setting up virtual environment..."

if command -v hostpad >/dev/null 2>&1; then
    echo "[!] 'hostapd not installed"
    echo "[!] Install hostapd and retry"
    exit 1
else:
    echo "[+] 'hostapd' is present moving on..."
fi

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

chmod +x cane_pole.py
echo "[+] Setup Complete! Run tool with 'sudo ./can_pole.py"
