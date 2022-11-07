# Konversi Mata Uang App

# Mata Uang : IND, US, JPY, THA, SBP
listMataUang = ['IND', 'US', 'JPY', 'THA', 'TUR', 'VNM', 'SGD', 'KOR']

while True:
    print(16*"=","DAFTAR NEGARA",16*"=")
    for i in range(len(listMataUang)):
        print(f"{listMataUang[i]}",end=" | ")
        
    print()
    print(47*"=")
    print(12*"=","PILIHAN MENU APLIKASI",12*"=")
    print(47*"=")
    print("1.Konversi Mata Uang Yang Tersedia")
    print("2.Konversi Ke Salah Satu Negara")
    print(47*"=")
    pilihan = int(input("=>"))
    
    # Operasi Pilihan Pertama
    if(pilihan == 1):
        mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
        dollarKeRupiah = mata_uang_sekarang // 14000
        print(f"Hasil Konversi\n=>(US)Dollar = {dollarKeRupiah}")

        yenKeRupiah = mata_uang_sekarang / 105.17
        print(f"Hasil Konversi {yenKeRupiah} Yen") 
 
        thaKeRupiah = mata_uang_sekarang / 409.76
        print(f"Hasil Konversi {thaKeRupiah} THA") 

        liraKeRupiah = mata_uang_sekarang / 841.44
        print(f"Hasil Konversi {liraKeRupiah} Lira")

        sgdKeRupiah = mata_uang_sekarang / 11043
        print(f"Hasil Konversi {sgdKeRupiah} SGD")
            
        vnmKeRupiah = mata_uang_sekarang / 0.63
        print(f"Hasil Konversi {vnmKeRupiah} VNM")
        
    # Operasi Pilihan Kedua
    elif(pilihan == 2):
        kode_mata_uang = input("Masukkan Kode Mata Uang : ")
        # Konversi ke US
        if(kode_mata_uang == 'US'):
            mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
            dollarKeRupiah = mata_uang_sekarang / 14000
            print(f"Hasil Konversi {dollarKeRupiah} Dollar")
        
        # Konversi ke JPY
        elif(kode_mata_uang == 'JPY'):
            mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
            yenKeRupiah = mata_uang_sekarang / 105.17
            print(f"Hasil Konversi {yenKeRupiah} Yen") 
        # Konversi ke THA
        elif(kode_mata_uang == 'THA'):
            mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
            thaKeRupiah = mata_uang_sekarang / 409.76
            print(f"Hasil Konversi {thaKeRupiah} THA") 
        # Konversi ke TUR
        elif(kode_mata_uang == 'TUR'):
            mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
            liraKeRupiah = mata_uang_sekarang / 841.44
            print(f"Hasil Konversi {liraKeRupiah} Lira")
        
        # Konversi ke SGD
        elif(kode_mata_uang == 'SGD'):
            mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
            sgdKeRupiah = mata_uang_sekarang / 11043
            print(f"Hasil Konversi {sgdKeRupiah} SGD")
            
        # Konversi ke VNM
        elif(kode_mata_uang == 'VNM'):
            mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
            vnmKeRupiah = mata_uang_sekarang / 0.63
            print(f"Hasil Konversi {vnmKeRupiah} VNM")
                        
    print(47*"=")
    isLanjut = input("Lanjut Konversi?(yes/no)\n=>")
    if isLanjut == 'yes' or isLanjut == 'YES':
        continue
    else:
        print(47*"=")
        print("Terima Kasih Telah Menggunakan Aplikasi Kami :)")
        print(47*"=")
        break