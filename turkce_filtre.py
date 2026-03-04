import os

input_path = 'index.m3u'
output_path = 'tr-vavoo.m3u'

if os.path.exists(input_path):
    print(f"{input_path} bulundu, işlem başlıyor...")
    with open(input_path, 'r', encoding='utf-8') as f:
        satirlar = f.readlines()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for i in range(len(satirlar)):
            # Sadece 'Turkey' grubuna ait olan başlık satırını bul
            if 'group-title="Turkey"' in satirlar[i]:
                # Eski User-Agent'ı yenisiyle (2.6) değiştirerek yaz
                yeni_inf = satirlar[i].replace('VAVOO/1.0', 'VAVOO/2.6')
                f.write(yeni_inf)
                
                # ÖNEMLİ: Başlık satırının hemen altındaki LİNK satırını al
                if i + 1 < len(satirlar):
                    f.write(satirlar[i+1])
    print(f"Bitti! {output_path} dosyası linklerle beraber oluşturuldu.")
else:
    print("Hata: index.m3u dosyası bulunamadı!")
    
