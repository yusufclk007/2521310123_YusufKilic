import requests
import os
from dotenv import load_dotenv

load_dotenv()

def ai_analiz_et(port_sonuclari, monitor_sonuclari):
    api_key = os.getenv("API_KEY")
    
    port_bilgisi = ""
    for p in port_sonuclari:
        port_bilgisi += "- Port " + str(p['port']) + "/" + p['protokol'] + ": " + p['servis'] + " " + p['versiyon'] + "\n"
    
    monitor_bilgisi = ""
    if monitor_sonuclari['degisiklikler']:
        for d in monitor_sonuclari['degisiklikler']:
            monitor_bilgisi += "- " + d + "\n"
    else:
        monitor_bilgisi = "- Izleme surecinde port degisikligi gozlemlenmedi.\n"

    prompt = "Asagida bir ag guvenlik taramasinin sonuclari verilmistir. Sen deneyimli bir siber guvenlik uzmanisın. Her acik port icin kisa bir risk degerlendirmesi yap, port izleme bulgularini yorumla, kapatilmasi veya guncellenmesi gereken servisler icin somut oneriler sun ve genel bir guvenlik ozeti yaz. Cevabini Turkce ver.\n\nACIK PORTLAR VE SERVISLER:\n" + port_bilgisi + "\nPORT IZLEME BULGULARI:\n" + monitor_bilgisi

    yanit = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={"Content-Type": "application/json", "Authorization": "Bearer " + api_key},
    json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}]}
)

    sonuc = yanit.json()
    print(sonuc)
    analiz = sonuc['choices'][0]['message']['content']
    print("AI analizi tamamlandi")
    return analiz
