import os

input_path = 'index.m3u'
output_path = 'tr-vavoo.m3u'

if os.path.exists(input_path):
    print("Dosya bulundu, temiz TR listesi oluşturuluyor...")
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dosyayı kanal bloklarına ayırıyoruz
    chunks = content.split('#EXTINF')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        
        for chunk in chunks:
            # Sadece Türkiye grubunu içeren blokları al
            if 'group-title="Turkey"' in chunk:
                # Blokları temizle ve User-Agent'ı 2.6 olarak güncelle
                cleaned_chunk = chunk.replace('VAVOO/1.0', 'VAVOO/2.6')
                
                # Bloğu geri birleştir ve yaz
                f.write('#EXTINF' + cleaned_chunk)
                
    print(f"İşlem Tamam! {output_path} hazır.")
else:
    print("Hata: index.m3u bulunamadı!")
    
