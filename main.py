# Konversi Mata Uang App

# Mata Uang : IND, US, JPY, THA, SBP
listMataUang = ['IND', 'US', 'JPY', 'THA', 'TUR', 'CNY', 'SGD', 'KOR']

while True:
    print(13*"=","DAFTAR KODE NEGARA",14*"=")
    for i in range(len(listMataUang)):
        print(f"|{listMataUang[i]}|",end=" ")
        
    print()
    print(47*"=")
    print(12*"=","PILIHAN MENU APLIKASI",12*"=")
    print(47*"=")
    print("1.Konversi Ke Banyak Negara")
    print("2.Konversi Ke Satu Negara")
    print("3.Keluar")
    print(47*"=")
    pilihan = int(input("=>"))
    
    # Operasi Pilihan Pertama
    if(pilihan == 1):
        kodeNegara = input("Masukkan Kode Negara :")
        if kodeNegara == 'IND' or kodeNegara == 'ind':
            jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
            INDkeUS = jumlahUang // 14000
            print(f"({listMataUang[1]})\t=> ${INDkeUS:.2f}")

            INDkeJPY = jumlahUang / 105.17
            print(f"({listMataUang[2]})\t=> ¥{INDkeJPY:.2f}")

            INDkeTHA = jumlahUang / 409.76
            print(f"({listMataUang[3]})\t=> ฿{INDkeTHA:.2f}") 

            INDkeTUR = jumlahUang / 841.44
            print(f"({listMataUang[4]})\t=> ₺{INDkeTUR:.2f}")

            INDkeCNY = jumlahUang / 2167.98
            print(f"({listMataUang[5]})\t=> ¥{INDkeCNY:.2f}")

            INDkeSGD = jumlahUang / 11043
            print(f"({listMataUang[6]})\t=> S${INDkeSGD:.2f}")

        elif kodeNegara == 'US' or kodeNegara == 'us':
            jumlahUang = int(input("Masukkan Jumlah Uang : $"))
            USkeIND = jumlahUang * 14000
            print(f"({listMataUang[0]})\t=> RP{USkeIND:.2f}")

            USkeJPY = jumlahUang * 146.55
            print(f"({listMataUang[2]})\t=> ¥{USkeJPY:.2f}")

            USkeTHA = jumlahUang / 409.76
            print(f"({listMataUang[3]})\t=> ฿{USkeTHA:.2f}") 

            USkeTUR = jumlahUang / 841.44
            print(f"({listMataUang[4]})\t=> ₺{USkeTUR:.2f}")

            USkeCNY = jumlahUang / 2167.98
            print(f"({listMataUang[5]})\t=> ¥{USkeCNY:.2f}")

            USkeSGD = jumlahUang / 11043
            print(f"({listMataUang[6]})\t=> S${USkeSGD:.2f}")

        else:
            print(47*"=")
            print("Kode Negara Tidak Ada Silahkan Pilih Yang Ada")
    # Operasi Pilihan Kedua
    elif(pilihan == 2):
        kodeNegaraTujuan = input("Masukkan Kode Negara Tujuan : ")
        # Konversi ke US
        if(kodeNegaraTujuan == 'US'):
            isLanjut = True
            while isLanjut:
                kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                    isLanjut = False
                elif kodeNegaraAsal == 'IND' or kodeNegaraAsal == 'ind':
                    jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
                    USkeIND = jumlahUang / 14000
                    print(f"=> ${USkeIND:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        
        # Konversi ke JPY
        elif(kodeNegaraTujuan == 'JPY'):
            jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
            JPYKeIND = jumlahUang / 105.17
            print(f"=> ¥{JPYKeIND:.2f}") 
        # Konversi ke THA
        elif(kodeNegaraTujuan == 'THA'):
            jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
            THAkeIND = jumlahUang / 409.76
            print(f"=> ฿{THAkeIND:.2f}") 
        # Konversi ke TUR
        elif(kodeNegaraTujuan == 'TUR'):
            jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
            TURkeIND = jumlahUang / 841.44
            print(f"=> ₺{TURkeIND:.2f}")
        
        # Konversi ke CNY
        elif(kodeNegaraTujuan == 'CNY'):
            jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
            CNYkeIND = jumlahUang / 2167.98
            print(f"=> ¥{CNYkeIND:.2f}")

        # Konversi ke SGD
        elif(kodeNegaraTujuan == 'SGD'):
            jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
            SGDkeIND = jumlahUang / 11043
            print(f"=> S${SGDkeIND:.2f}")
        
        # Konversi Ke KOR
    # Operasi Pilihan Ketiga
    elif(pilihan == 3):
        print(47*"=")
        print("Terima Kasih Telah Menggunakan Aplikasi Kami :)")
        print(47*"=")
        break
    # Operasi Pilihan Tidak Tersedia
    else:
        print(47*"=")
        print("Pilihan Tidak Tersedia Silahkan Pilih Yang Lain")

    print(47*"=")
    isLanjut = input("Lanjut Konversi?(yes/no)\n=>")
    if isLanjut == 'yes' or isLanjut == 'YES':
        continue
    else:
        print(47*"=")
        print("Terima Kasih Telah Menggunakan Aplikasi Kami :)")
        print(47*"=")
        break