import os

# Dosya yolları
input_path = 'index.m3u'
output_path = 'tr-vavoo.m3u'

def filtrele():
    if not os.path.exists(input_path):
        print(f"Hata: {input_path} dosyası bulunamadı! Lütfen önce ana listenin indiğinden emin olun.")
        return

    print(f"{input_path} taranıyor, sadece Türkiye kanalları ayıklanıyor...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_path, 'w', encoding='utf-8') as f:
        # M3U Dosya Başlığı
        f.write("#EXTM3U\n")
        
        tr_kanal_sayisi = 0
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # 1. Adım: Türkiye grubuna ait bir kanal başlığı bul
            if line.startswith('#EXTINF') and 'group-title="Turkey"' in line:
                # Başlık satırını yaz (VAVOO/1.0 varsa 2.6 ile güncelle)
                f.write(line.replace('VAVOO/1.0', 'VAVOO/2.6') + '\n')
                
                # 2. Adım: Altındaki tüm ayar ve link satırlarını tara
                i += 1
                while i < len(lines):
                    next_line = lines[i].strip()
                    
                    # Eğer yeni bir kanal başlığına geldiysek bu döngüden çık
                    if next_line.startswith('#EXTINF'):
                        # i değerini artırmıyoruz ki ana döngü bu yeni kanalı işleyebilsin
                        break
                    
                    # Ayar satırlarını veya yayın linkini yaz
                    if next_line:
                        # User-Agent güncellemesi yap ve satırı yaz
                        f.write(next_line.replace('VAVOO/1.0', 'VAVOO/2.6') + '\n')
                        
                        # Eğer bu bir yayın linkiyse (http ile başlıyorsa), bu kanal bloğu bitmiştir
                        if next_line.startswith('http'):
                            tr_kanal_sayisi += 1
                            i += 1
                            break
                    i += 1
                continue # Ana döngüye dön ve i'nin kaldığı yerden devam et
            i += 1

    print(f"İşlem tamamlandı! {tr_kanal_sayisi} adet TR kanalı '{output_path}' dosyasına başarıyla aktarıldı.")

if __name__ == "__main__":
    filtrele()
                        
