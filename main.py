# Konversi Mata Uang App

# Mata Uang : 'IND', 'US', 'JPY', 'THA', 'TUR', 'CNY', 'SGD', 'KOR'
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
# * ============================================================================
    # Operasi Pilihan Pertama
    if(pilihan == 1):
        kodeNegara = input("Masukkan Kode Negara :")
        # * ==================================================
        if kodeNegara == 'IND' or kodeNegara == 'ind':
            jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
            INDkeUS = jumlahUang // 14000
            print(f"({listMataUang[1]})\t=> US${INDkeUS:.2f}")

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
            
            INDkeKOR = jumlahUang * 0.088
            print(f"({listMataUang[7]})\t=> ₩{INDkeKOR:.2f}")            
            
        # * ==================================================
        elif kodeNegara == 'US' or kodeNegara == 'us':
            jumlahUang = int(input("Masukkan Jumlah Uang : $"))
            USkeIND = jumlahUang * 14000
            print(f"({listMataUang[0]})\t=> RP{USkeIND:.2f}")

            USkeJPY = jumlahUang * 146.31
            print(f"({listMataUang[2]})\t=> ¥{USkeJPY:.2f}")

            USkeTHA = jumlahUang * 37.21
            print(f"({listMataUang[3]})\t=> ฿{USkeTHA:.2f}") 

            USkeTUR = jumlahUang * 18.61
            print(f"({listMataUang[4]})\t=> ₺{USkeTUR:.2f}")

            USkeCNY = jumlahUang * 7.25
            print(f"({listMataUang[5]})\t=> ¥{USkeCNY:.2f}")

            USkeSGD = jumlahUang * 1.40
            print(f"({listMataUang[6]})\t=> S${USkeSGD:.2f}")
            
            USkeKOR = jumlahUang * 1378.09
            print(f"({listMataUang[7]})\t=> ₩{USkeKOR:.2f}")
        # * ==================================================
        elif kodeNegara == 'JPY' or kodeNegara == 'jpy':
            jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
            JPYkeIND = jumlahUang * 106.97
            print(f"({listMataUang[0]})\t=> RP{JPYkeIND:.2f}")

            JPYkeUS = jumlahUang * 0.0068
            print(f"({listMataUang[1]})\t=> US${JPYkeUS:.2f}")

            JPYkeTHA = jumlahUang * 0.25
            print(f"({listMataUang[3]})\t=> ฿{JPYkeTHA:.2f}") 

            JPYkeTUR = jumlahUang * 0.13
            print(f"({listMataUang[4]})\t=> ₺{JPYkeTUR:.2f}")

            JPYkeCNY = jumlahUang * 0.050
            print(f"({listMataUang[5]})\t=> ¥{JPYkeCNY:.2f}")

            JPYkeSGD = jumlahUang * 0.0096
            print(f"({listMataUang[6]})\t=> S${JPYkeSGD:.2f}")
            
            JPYkeKOR = jumlahUang * 9.41
            print(f"({listMataUang[7]})\t=> ₩{JPYkeKOR:.2f}")
        # * ==================================================
        else:
            print(47*"=")
            print("Kode Negara Tidak Ada Silahkan Pilih Yang Ada")
# * ============================================================================
    # Operasi Pilihan Kedua
    elif(pilihan == 2):
        kodeNegaraTujuan = input("Masukkan Kode Negara Tujuan : ")
        # * ==================================================
        # Konversi ke IND
        if(kodeNegaraTujuan == 'IND' or kodeNegaraTujuan == 'ind'):
            isLanjut = True
            while isLanjut:
                kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                    isLanjut = False
                elif kodeNegaraAsal == 'US' or kodeNegaraAsal == 'us':
                    jumlahUang = int(input("Masukkan Jumlah Uang : RP"))
                    USkeIND = jumlahUang / 14000
                    print(f"=> ${USkeIND:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeJPY = jumlahUang / 14000
                    print(f"=> ${USkeJPY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ฿"))
                    USkeTHA = jumlahUang / 14000
                    print(f"=> ${USkeTHA:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ₺"))
                    USkeTUR = jumlahUang / 14000
                    print(f"=> ${USkeTUR:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeCNY = jumlahUang / 14000
                    print(f"=> ${USkeCNY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        # * ==================================================
        # Konversi ke US
        if(kodeNegaraTujuan == 'US' or kodeNegaraTujuan == 'us'):
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
                elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeJPY = jumlahUang / 14000
                    print(f"=> ${USkeJPY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ฿"))
                    USkeTHA = jumlahUang / 14000
                    print(f"=> ${USkeTHA:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ₺"))
                    USkeTUR = jumlahUang / 14000
                    print(f"=> ${USkeTUR:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeCNY = jumlahUang / 14000
                    print(f"=> ${USkeCNY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        # * ==================================================
        # Konversi ke JPY
        elif(kodeNegaraTujuan == 'JPY' or kodeNegaraTujuan == 'jpy'):
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
                elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeJPY = jumlahUang / 14000
                    print(f"=> ${USkeJPY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ฿"))
                    USkeTHA = jumlahUang / 14000
                    print(f"=> ${USkeTHA:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ₺"))
                    USkeTUR = jumlahUang / 14000
                    print(f"=> ${USkeTUR:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeCNY = jumlahUang / 14000
                    print(f"=> ${USkeCNY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        # * ==================================================
        # Konversi ke THA
        elif(kodeNegaraTujuan == 'THA' or kodeNegaraTujuan == 'tha'):
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
                elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeJPY = jumlahUang / 14000
                    print(f"=> ${USkeJPY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ฿"))
                    USkeTHA = jumlahUang / 14000
                    print(f"=> ${USkeTHA:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ₺"))
                    USkeTUR = jumlahUang / 14000
                    print(f"=> ${USkeTUR:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeCNY = jumlahUang / 14000
                    print(f"=> ${USkeCNY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        # * ==================================================
        # Konversi ke TUR
        elif(kodeNegaraTujuan == 'TUR' or kodeNegaraTujuan == 'tur'):
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
                elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeJPY = jumlahUang / 14000
                    print(f"=> ${USkeJPY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ฿"))
                    USkeTHA = jumlahUang / 14000
                    print(f"=> ${USkeTHA:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ₺"))
                    USkeTUR = jumlahUang / 14000
                    print(f"=> ${USkeTUR:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeCNY = jumlahUang / 14000
                    print(f"=> ${USkeCNY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        # * ==================================================
        # Konversi ke CNY
        elif(kodeNegaraTujuan == 'CNY' or kodeNegaraTujuan == 'cny'):
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
                elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeJPY = jumlahUang / 14000
                    print(f"=> ${USkeJPY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ฿"))
                    USkeTHA = jumlahUang / 14000
                    print(f"=> ${USkeTHA:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ₺"))
                    USkeTUR = jumlahUang / 14000
                    print(f"=> ${USkeTUR:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeCNY = jumlahUang / 14000
                    print(f"=> ${USkeCNY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        # * ==================================================
        # Konversi ke SGD
        elif(kodeNegaraTujuan == 'SGD' or kodeNegaraTujuan == 'sgd'):
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
                elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeJPY = jumlahUang / 14000
                    print(f"=> ${USkeJPY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ฿"))
                    USkeTHA = jumlahUang / 14000
                    print(f"=> ${USkeTHA:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ₺"))
                    USkeTUR = jumlahUang / 14000
                    print(f"=> ${USkeTUR:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeCNY = jumlahUang / 14000
                    print(f"=> ${USkeCNY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        # * ==================================================
        # Konversi Ke KOR
        elif(kodeNegaraTujuan == 'KOR' or kodeNegaraTujuan == 'kor'):
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
                elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeJPY = jumlahUang / 14000
                    print(f"=> ${USkeJPY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ฿"))
                    USkeTHA = jumlahUang / 14000
                    print(f"=> ${USkeTHA:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ₺"))
                    USkeTUR = jumlahUang / 14000
                    print(f"=> ${USkeTUR:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                    jumlahUang = int(input("Masukkan Jumlah Uang : ¥"))
                    USkeCNY = jumlahUang / 14000
                    print(f"=> ${USkeCNY:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                    jumlahUang = int(input("Masukkan Jumlah Uang : S$"))
                    USkeSGD = jumlahUang / 14000
                    print(f"=> ${USkeSGD:.2f}")
                    isLanjut = False
                else:
                    print(47*"=")
                    print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nSilahkan Ketik 'BACK' Untuk Keluar Dari Menu 2")
                    print(47*"=")
        # * ==================================================

# * ============================================================================
    # Operasi Pilihan Ketiga
    elif(pilihan == 3):
        print(47*"=")
        print("Terima Kasih Telah Menggunakan Aplikasi Kami :)")
        print(47*"=")
        break
# * ============================================================================
    # Operasi Pilihan Tidak Tersedia
    else:
        print(47*"=")
        print("Pilihan Tidak Tersedia Silahkan Pilih Yang Lain")
# * ============================================================================
    print(47*"=")
    lanjut = True
    while lanjut:
        isLanjut = input("Lanjut Konversi?(yes/no)\n=>")
        if isLanjut == 'yes' or isLanjut == 'YES':
            lanjut = False
        elif isLanjut == 'no' or isLanjut == 'NO':
            print(47*"=")
            print("Terima Kasih Telah Menggunakan Aplikasi Kami :)")
            print(47*"=")
            exit()
        else:
            print(47*"=")
            print("Pilihan Keyword Tidak Ada!")
            print(47*"=")
            continue