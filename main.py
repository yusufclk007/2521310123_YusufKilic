from m1_port_scan import port_tara
from m5_port_monitor import port_izle
from ai_analyzer import ai_analiz_et
from report_generator import rapor_olustur

hedef_ip = input("Hedef IP adresini girin: ")

print("\nM1 - Port tarama basliyor...")
port_sonuclari = port_tara(hedef_ip)

print("\nM5 - Port izleme basliyor...")
monitor_sonuclari = port_izle(hedef_ip, kontrol_suresi=10, tekrar=3)

print("\nAI analizi basliyor...")
ai_analiz = ai_analiz_et(port_sonuclari, monitor_sonuclari)

print("\nRapor olusturuluyor...")
rapor_olustur(hedef_ip, port_sonuclari, monitor_sonuclari, ai_analiz)

print("\nIslem tamamlandi! rapor.html dosyasini acabilirsiniz.")
