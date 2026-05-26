def rapor_olustur(hedef_ip, port_sonuclari, monitor_sonuclari, ai_analiz):

    port_satirlari = ""
    for p in port_sonuclari:
        port_satirlari += "<tr><td>" + str(p['port']) + "</td><td>" + p['protokol'] + "</td><td>" + p['servis'] + "</td><td>" + p['versiyon'] + "</td></tr>"

    degisiklik_satirlari = ""
    if monitor_sonuclari['degisiklikler']:
        for d in monitor_sonuclari['degisiklikler']:
            degisiklik_satirlari += "<li>" + d + "</li>"
    else:
        degisiklik_satirlari = "<li>Izleme surecinde degisiklik gozlemlenmedi.</li>"

    ai_html = ai_analiz.replace('\n', '<br>')

    html = """<!DOCTYPE html>
<html lang='tr'>
<head>
<meta charset='UTF-8'>
<title>Guvenlik Tarama Raporu</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    padding: 30px;
    max-width: 900px;
    margin: auto;
  }
  h1 {
    background-color: #2c3e50;
    color: white;
    padding: 15px;
    border-radius: 6px;
  }
  h2 {
    background-color: #34495e;
    color: white;
    padding: 10px;
    border-radius: 4px;
    margin-top: 30px;
  }
  p {
    font-size: 16px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    background-color: white;
    border-radius: 6px;
    overflow: hidden;
  }
  th {
    background-color: #2c3e50;
    color: white;
    padding: 10px;
    text-align: left;
  }
  td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  tr:hover {
    background-color: #f0f0f0;
  }
  ul {
    background-color: white;
    padding: 20px 30px;
    border-radius: 6px;
    list-style: disc;
  }
  li {
    margin-bottom: 6px;
  }
  .ai-box {
    background-color: white;
    padding: 20px;
    border-radius: 6px;
    border-left: 5px solid #2c3e50;
    line-height: 1.8;
  }
</style>
</head>
<body>

<h1>Ag Guvenlik Tarama Raporu</h1>
<p><strong>Hedef IP:</strong> """ + hedef_ip + """</p>

<h2>Port Tarama Sonuclari (M1)</h2>
<table>
  <tr>
    <th>Port</th>
    <th>Protokol</th>
    <th>Servis</th>
    <th>Versiyon</th>
  </tr>
  """ + port_satirlari + """
</table>

<h2>Port Izleme Sonuclari (M5)</h2>
<ul>""" + degisiklik_satirlari + """</ul>

<h2>Yapay Zeka Guvenlik Analizi</h2>
<div class='ai-box'>""" + ai_html + """</div>

</body>
</html>"""

    with open("rapor.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("rapor.html olusturuldu")
