import nmap

def port_tara(hedef_ip):
    tarayici = nmap.PortScanner()
    print(f"[*] {hedef_ip} taranıyor...")
    tarayici.scan(hedef_ip, arguments='-sV -sS -Pn --top-ports 100')
    
    sonuclar = []
    for host in tarayici.all_hosts():
        for proto in tarayici[host].all_protocols():
            portlar = tarayici[host][proto].keys()
            for port in portlar:
                servis = tarayici[host][proto][port]
                if servis['state'] == 'open':
                    sonuc = {
                        'port': port,
                        'protokol': proto,
                        'durum': servis['state'],
                        'servis': servis['name'],
                        'versiyon': servis['version']
                    }
                    sonuclar.append(sonuc)
                    print(f"  [+] Port {port}/{proto} - {servis['name']} {servis['version']}")
    
    return sonuclar
