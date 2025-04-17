import os

def apply():
    print("\n[+] Aplicando hardening básico:")
    os.system("sudo apt install unattended-upgrades -y")
    os.system("sudo dpkg-reconfigure --priority=low unattended-upgrades")
    os.system("sudo ufw default deny incoming")
    os.system("sudo ufw allow 22/tcp")
    print("\n[!] Firewall configurado e atualizações automáticas ativadas.")
