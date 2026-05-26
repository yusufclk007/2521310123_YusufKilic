import nmap
import time

def port_izle(hedef_ip, kontrol_suresi=10, tekrar=3):
    tarayici = nmap.PortScanner()
    print(f"[*] {hedef_ip} izleniyor... ({tekrar} kez kontrol edilecek)")
    
    onceki_portlar = set()
    degisiklikler = []

    for i in range(tekrar):
        print(f"\n[*] Tarama {i+1}/{tekrar}")
        tarayici.scan(hedef_ip, arguments='--top-ports 100')
        
        guncel_portlar = set()
        for host in tarayici.all_hosts():
            for proto in tarayici[host].all_protocols():
                for port in tarayici[host][proto].keys():
                    if tarayici[host][proto][port]['state'] == 'open':
                        guncel_portlar.add(port)

        if onceki_portlar:
            yeni_acilan = guncel_portlar - onceki_portlar
            kapanan = onceki_portlar - guncel_portlar

            if yeni_acilan:
                print(f"  [!] Yeni açılan portlar: {yeni_acilan}")
                degisiklikler.append(f"Tarama {i+1}: Yeni açılan portlar: {yeni_acilan}")
            if kapanan:
                print(f"  [!] Kapanan portlar: {kapanan}")
                degisiklikler.append(f"Tarama {i+1}: Kapanan portlar: {kapanan}")
            if not yeni_acilan and not kapanan:
                print("  [+] Değişiklik yok")
        
        onceki_portlar = guncel_portlar

        if i < tekrar - 1:
            print(f"  [*] {kontrol_suresi} saniye bekleniyor...")
            time.sleep(kontrol_suresi)

    return {
        'izlenen_ip': hedef_ip,
        'son_portlar': list(onceki_portlar),
        'degisiklikler': degisiklikler
    }
