# Yapay Zeka Destekli Ag Guvenlik Tarayicisi

## Ogrenci Bilgileri
Ad Soyad: Yusuf Kilic
Ogrenci No: 2521310123

## Proje Hakkinda
Bu proje bir ag uzerindeki acik portlari tespit eden ve yapay zeka ile analiz eden bir Python programidir.
Kali Linux uzerinde calisir. Nmap kullanarak port tarar, portlari izler ve Groq AI ile guvenlik raporu olusturur.

## Moduller
- M1: Nmap ile port tarama ve servis tespiti
- M5: Belirli aralikla port izleme ve degisiklik tespiti

## Kullanilan Yapay Zeka
Groq API - llama-3.3-70b-versatile modeli

## Nasil Kurulur
1. Kali Linux'a Nmap kurun
2. Virtual environment olusturun ve aktif edin
3. Gerekli kutuphaneleri yukleyin
4. .env dosyasina Groq API anahtarini yazin

## Nasil Calistirilir
sudo venv/bin/python3 main.py

Hedef IP sorulacak, Metasploitable IP adresini girin.
Program tarama yapacak ve rapor.html dosyasi olusturacak.
