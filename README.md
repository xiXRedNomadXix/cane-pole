# Cane Pole

**Cane Pole** is a Python-based rogue access point (Evil Twin) tool designed for ethical hacking and wireless security research. It mimics a known Wi-Fi network and waits for devices to auto-connect, without using deauthentication or phishing techniques.

---

## ⚙️ Features

- Broadcasts a fake access point (SSID spoofing)
- Configurable SSID, channel, WPA2 passphrase, and interface
- Does **not** deauth or disrupt existing clients
- Fully compatible with `pipx` for safe, isolated CLI usage

---

## 🚀 Installation
**Install dependancies**
```bash
sudo apt install hostapd pipx
pipx install git+https://github.com/xiXRedNomadXix/cane-pole.git
