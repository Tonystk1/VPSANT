import nmap
import json

def scan(target):
    scanner = nmap.PortScanner()
    print(f"\n[+] Escaneando {target}...")
    scanner.scan(target, arguments="-sV -T4 --script vulners")
    
    for host in scanner.all_hosts():
        print(f"\nRelatório para {host}:")
        for proto in scanner[host].all_protocols():
            print(f"\nProtocolo: {proto}")
            for port in scanner[host][proto].keys():
                service = scanner[host][proto][port]
                print(f"  Porta {port}: {service['state']} ({service['name']})")
                if 'script' in service:
                    print(f"  Vulnerabilidades: {service['script']}")
    
    with open(f"scan_{target}.json", "w") as f:
        json.dump(scanner[host], f, indent=4)
