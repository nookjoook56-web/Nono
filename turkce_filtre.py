import os

# Bu repo genellikle 'VavooGen' klasörü içine index.m3u oluşturur
input_path = 'VavooGen/index.m3u'
output_path = 'tr-vavoo.m3u'

if os.path.exists(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        satirlar = f.readlines()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for i in range(len(satirlar)):
            # 'Turkey' veya 'TR' grubunu yakala
            if 'group-title="Turkey"' in satirlar[i] or 'group-title="TR"' in satirlar[i]:
                f.write(satirlar[i])      # Kanal bilgisi satırı
                if i + 1 < len(satirlar):
                    f.write(satirlar[i+1]) # Kanal link satırı
    print(f"Bitti! {output_path} dosyası başarıyla hazırlandı.")
else:
    print(f"Hata: {input_path} dosyası bulunamadı. Önce Actions çalışmalı.")
  
