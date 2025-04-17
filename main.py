from modules import log_analyzer, nmap_scanner, hardening
import os
if os.getenv('VPS_MENU_LOADED') == '2':
    exit()  # Previne loop
os.environ['VPS_MENU_LOADED'] = '2'

if __name__ == "__main__" and not os.getenv("VPS_MENU_LOADED"):
    os.environ["VPS_MENU_LOADED"] = "1"
    main()


def show_banner():
    print(r"""
 __     __ ____   ____      _     _   _  _____
 \ \   / /|  _ \ / ___|    / \   | \ | ||_   _|
  \ \ / / | |_) |\___ \   / _ \  |  \| |  | |
   \ V /  |  __/  ___) | / ___ \ | |\  |  | |
    \_/   |_|    |____/ /_/   \_\|_| \_|  |_|""")

def main():
    show_banner()
    while True:
        print("\n[1] Analisar logs de acesso")
        print("[2] Escanear portas (Nmap)")
        print("[3] Aplicar hardening")
        print("[4] Monitorar tráfego (tcpdump)")
        print("[5] Sair")
        
        choice = input("\nEscolha uma opção: ")
        
        if choice == "1":
            log_analyzer.analyze()
        elif choice == "2":
            target = input("Digite o IP ou domínio: ")
            nmap_scanner.scan(target)
        elif choice == "3":
            hardening.apply()
        elif choice == "4":
            os.system("sudo tcpdump -i eth0 -n -c 20")
        elif choice == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
