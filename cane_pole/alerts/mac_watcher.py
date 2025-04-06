def check_mac(line, target_mac):
    if target_mac.lower() in line.lower():
       print("[!] Target device {target_mac.upper()} has connected.")
