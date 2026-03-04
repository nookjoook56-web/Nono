import os

input_path = 'index.m3u'
output_path = 'tr-vavoo.m3u'

if os.path.exists(input_path):
    print(f"{input_path} dosyası işleniyor...")
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for i in range(len(lines)):
            # Sadece Türkiye grubunu bul
            if 'group-title="Turkey"' in lines[i]:
                # 1. Satır: Kanal Bilgisi (EXTINF)
                f.write(lines[i])
                
                # 2. Satır: Eğer varsa VLC Seçeneği (User-Agent düzeltmesi ile)
                if i + 1 < len(lines) and '#EXTVLCOPT' in lines[i+1]:
                    f.write(lines[i+1].replace('VAVOO/1.0', 'VAVOO/2.6'))
                    
                    # 3. Satır: Asıl Yayın Linki (Bu satır çok önemli!)
                    if i + 2 < len(lines) and lines[i+2].startswith('http'):
                        f.write(lines[i+2])
                
                # Alternatif: Eğer Seçenek satırı yoksa doğrudan linki al
                elif i + 1 < len(lines) and lines[i+1].startswith('http'):
                    f.write(lines[i+1])

    print(f"İşlem tamam! {output_path} artık linkleri de içeriyor.")
else:
    print("Hata: Kaynak dosya bulunamadı!")
