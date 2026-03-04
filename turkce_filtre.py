import os

input_path = 'index.m3u'
output_path = 'tr-vavoo.m3u'

if os.path.exists(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        satirlar = f.readlines()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for i in range(len(satirlar)):
            # "Turkey" grubunu bul
            if 'group-title="Turkey"' in satirlar[i]:
                # 1. User-Agent'ı 1.0'dan 2.6'ya yükselt
                duzeltilmis_inf = satirlar[i].replace('VAVOO/1.0', 'VAVOO/2.6')
                f.write(duzeltilmis_inf)
                
                # 2. Alt satırdaki linki kontrol et ve ekle
                if i + 1 < len(satirlar) and satirlar[i+1].startswith('http'):
                    f.write(satirlar[i+1])
    print("TR Listesi User-Agent 2.6 ile güncellendi!")
else:
    print("Dosya bulunamadı!")
    
