import os

# Dosya yolları
input_path = 'index.m3u'
output_path = 'tr-vavoo.m3u'

def filtrele():
    if not os.path.exists(input_path):
        print(f"Hata: {input_path} bulunamadı!")
        return

    print(f"{input_path} işleniyor, sadece TR kanalları süzülüyor...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_path, 'w', encoding='utf-8') as f:
        # M3U Başlığı
        f.write("#EXTM3U\n")
        
        counter = 0
        for i in range(len(lines)):
            # 1. Adım: Sadece 'Turkey' grubuna ait olan satırı yakala
            if '#EXTINF' in lines[i] and 'group-title="Turkey"' in lines[i]:
                # Başlık satırını yaz (VAVOO/1.0 varsa 2.6 yap)
                f.write(lines[i].replace('VAVOO/1.0', 'VAVOO/2.6'))
                
                # 2. Adım: Altındaki EXTVLCOPT satırlarını kontrol et ve yaz
                current_idx = i + 1
                while current_idx < len(lines) and lines[current_idx].startswith('#EXTVLCOPT'):
                    f.write(lines[current_idx].replace('VAVOO/1.0', 'VAVOO/2.6'))
                    current_idx += 1
                
                # 3. Adım: Altındaki KODIPROP satırlarını kontrol et ve yaz
                while current_idx < len(lines) and lines[current_idx].startswith('#KODIPROP'):
                    f.write(lines[current_idx].replace('VAVOO/1.0', 'VAVOO/2.6'))
                    current_idx += 1

                # 4. Adım: EXTHTTP satırını kontrol et ve yaz
                if current_idx < len(lines) and lines[current_idx].startswith('#EXTHTTP'):
                    f.write(lines[current_idx].replace('VAVOO/1.0', 'VAVOO/2.6'))
                    current_idx += 1

                # 5. Adım: ASIL YAYIN LİNKİNİ (https://...) yakala ve yaz
                if current_idx < len(lines) and lines[current_idx].startswith('http'):
                    f.write(lines[current_idx])
                    counter += 1

    print(f"İşlem bitti! Toplam {counter} TR kanalı 'tr-vavoo.m3u' dosyasına kaydedildi.")

if __name__ == "__main__":
    filtrele()
                
