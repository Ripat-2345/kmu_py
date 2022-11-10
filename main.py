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
    pilihan = float(input("=>"))
# * ============================================================================
    # Operasi Pilihan Pertama
    if(pilihan == 1):
        kodeNegara = input("Masukkan Kode Negara :")
        # * ==================================================
        if kodeNegara == 'IND' or kodeNegara == 'ind':
            masukkan = input("Masukkan Jumlah Uang : RP")
            if type(masukkan) != float or type(masukkan) != int:
                print(47*"=")
                print("Maaf Masukkan Hanya Angka!")
            else:
                jumlahUang = float(masukkan)
                print(47*"=")
                INDkeUS = jumlahUang / 14000
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
            masukkan = input("Masukkan Jumlah Uang : $")
            if type(masukkan) != float or type(masukkan) != int:
                print(47*"=")
                print("Maaf Masukkan Hanya Angka!")
            else:
                jumlahUang = float(masukkan)            
                print(47*"=")
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
            masukkan = input("Masukkan Jumlah Uang : ¥")
            if type(masukkan) != float or type(masukkan) != int:
                print(47*"=")
                print("Maaf Masukkan Hanya Angka!")
            else:
                jumlahUang = float(masukkan)              
                print(47*"=")
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
        elif kodeNegara == 'THA' or kodeNegara == 'tha':
            masukkan = input("Masukkan Jumlah Uang : ฿")
            if type(masukkan) != float or type(masukkan) != int:
                print(47*"=")
                print("Maaf Masukkan Hanya Angka!")
            else:
                jumlahUang = float(masukkan)  
                print(47*"=")
                THAkeIND = jumlahUang * 420.42
                print(f"({listMataUang[0]})\t=> RP{THAkeIND:.2f}")

                THAkeUS = jumlahUang * 0.027
                print(f"({listMataUang[1]})\t=> US${THAkeUS:.2f}")

                THAkeJPY = jumlahUang * 3.93
                print(f"({listMataUang[2]})\t=> ¥{THAkeJPY:.2f}") 

                THAkeTUR = jumlahUang * 0.50
                print(f"({listMataUang[4]})\t=> ₺{THAkeTUR:.2f}")

                THAkeCNY = jumlahUang * 0.19
                print(f"({listMataUang[5]})\t=> ¥{THAkeCNY:.2f}")

                THAkeSGD = jumlahUang * 0.038
                print(f"({listMataUang[6]})\t=> S${THAkeSGD:.2f}")
                
                THAkeKOR = jumlahUang * 36.97
                print(f"({listMataUang[7]})\t=> ₩{THAkeKOR:.2f}")
        # * ==================================================
        elif kodeNegara == 'TUR' or kodeNegara == 'tur':
            masukkan = input("Masukkan Jumlah Uang : ₺")
            if type(masukkan) != float or type(masukkan) != int:
                print(47*"=")
                print("Maaf Masukkan Hanya Angka!")
            else:
                jumlahUang = float(masukkan)  
                print(47*"=")
                TURkeIND = jumlahUang * 840.060
                print(f"({listMataUang[0]})\t=> RP{TURkeIND:.2f}")

                TURkeUS = jumlahUang * 0.054
                print(f"({listMataUang[1]})\t=> US${TURkeUS:.2f}")
                
                TURkeJPY = jumlahUang * 7.86
                print(f"({listMataUang[2]})\t=> ₺{TURkeJPY:.2f}")

                TURkeTHA = jumlahUang * 2.00
                print(f"({listMataUang[3]})\t=> ฿{TURkeTHA:.2f}") 

                TURkeCNY = jumlahUang * 0.39
                print(f"({listMataUang[5]})\t=> ¥{TURkeCNY:.2f}")

                TURkeSGD = jumlahUang * 0.075
                print(f"({listMataUang[6]})\t=> S${TURkeSGD:.2f}")
                
                TURkeKOR = jumlahUang * 79.93
                print(f"({listMataUang[7]})\t=> ₩{TURkeKOR:.2f}")
        # * ==================================================
        elif kodeNegara == 'CNY' or kodeNegara == 'cny':
            masukkan = input("Masukkan Jumlah Uang : ¥")
            if type(masukkan) != float or type(masukkan) != int:
                print(47*"=")
                print("Maaf Masukkan Hanya Angka!")
            else:
                jumlahUang = float(masukkan)  
                print(47*"=")
                CNYkeIND = jumlahUang * 2156.65
                print(f"({listMataUang[0]})\t=> RP{CNYkeIND:.2f}")

                CNYkeUS = jumlahUang * 0.14
                print(f"({listMataUang[1]})\t=> US${CNYkeUS:.2f}")

                CNYkeJPY = jumlahUang * 20.16
                print(f"({listMataUang[2]})\t=> ¥{CNYkeJPY:.2f}")
                
                CNYkeTHA = jumlahUang * 5.13
                print(f"({listMataUang[3]})\t=> ฿{CNYkeTHA:.2f}") 

                CNYkeTUR = jumlahUang * 2.56
                print(f"({listMataUang[4]})\t=> ₺{CNYkeTUR:.2f}")

                CNYkeSGD = jumlahUang * 0.19
                print(f"({listMataUang[6]})\t=> S${CNYkeSGD:.2f}")
                
                CNYkeKOR = jumlahUang * 189.64
                print(f"({listMataUang[7]})\t=> ₩{CNYkeKOR:.2f}")
        # * ==================================================
        elif kodeNegara == 'SGD' or kodeNegara == 'sgd':
            masukkan = input("Masukkan Jumlah Uang : S$")
            if type(masukkan) != float or type(masukkan) != int:
                print(47*"=")
                print("Maaf Masukkan Hanya Angka!")
            else:
                jumlahUang = float(masukkan)  
                print(47*"=")
                SGDkeIND = jumlahUang * 11152.14
                print(f"({listMataUang[0]})\t=> RP{SGDkeIND:.2f}")

                SGDkeUS = jumlahUang * 0.71
                print(f"({listMataUang[1]})\t=> US${SGDkeUS:.2f}")

                SGDkeJPY = jumlahUang * 104.18
                print(f"({listMataUang[2]})\t=> ¥{SGDkeJPY:.2f}")
                
                SGDkeTHA = jumlahUang * 26.52
                print(f"({listMataUang[3]})\t=> ฿{SGDkeTHA:.2f}") 

                SGDkeTUR = jumlahUang * 13.26
                print(f"({listMataUang[4]})\t=> ₺{SGDkeTUR:.2f}")

                SGDkeCNY = jumlahUang * 5.17
                print(f"({listMataUang[5]})\t=> ¥{SGDkeCNY:.2f}")
                
                SGDkeKOR = jumlahUang * 980.90
                print(f"({listMataUang[7]})\t=> ₩{SGDkeKOR:.2f}")
        # * ==================================================
        elif kodeNegara == 'KOR' or kodeNegara == 'kor':
            masukkan = input("Masukkan Jumlah Uang : ₩")
            if type(masukkan) != float or type(masukkan) != int:
                print(47*"=")
                print("Maaf Masukkan Hanya Angka!")
            else:
                jumlahUang = float(masukkan)             
                print(47*"=")
                KORkeIND = jumlahUang * 11.37
                print(f"({listMataUang[0]})\t=> RP{KORkeIND:.2f}")

                KORkeUS = jumlahUang * 0.00073
                print(f"({listMataUang[1]})\t=> US${KORkeUS:.2f}")

                KORkeJPY = jumlahUang * 0.11
                print(f"({listMataUang[2]})\t=> ¥{KORkeJPY:.2f}")
                
                KORkeTHA = jumlahUang * 0.027
                print(f"({listMataUang[3]})\t=> ฿{KORkeTHA:.2f}") 

                KORkeTUR = jumlahUang * 0.014
                print(f"({listMataUang[4]})\t=> ₺{KORkeTUR:.2f}")

                KORkeCNY = jumlahUang * 0.0053
                print(f"({listMataUang[5]})\t=> ¥{KORkeCNY:.2f}")

                KORkeSGD = jumlahUang * 0.0010
                print(f"({listMataUang[6]})\t=> S${KORkeSGD:.2f}")
        # * ==================================================
        else:
            print(47*"=")
            print("Kode Negara Tidak Ada Silahkan Pilih Yang Ada")
# * ============================================================================
    # Operasi Pilihan Kedua
    elif(pilihan == 2):
        while True:
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
                        try:
                            masukkan = input("Masukkan Jumlah Uang : $")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ¥")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ฿")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ₺")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ¥")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : S$")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ₩")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal.lower() == kodeNegaraTujuan.lower():
                        try:
                            masukkan = input("Masukkan Jumlah Uang : RP")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    else:
                        print(47*"=")
                        print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nAnda Bisa Ketik 'BACK' Untuk Keluar Dari Menu 2")
                        print(47*"=")
                break
            # * ==================================================
            # Konversi ke US
            if(kodeNegaraTujuan == 'US' or kodeNegaraTujuan == 'us'):
                isLanjut = True
                while isLanjut:
                    kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                    if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                        isLanjut = False
                    elif kodeNegaraAsal == 'IND' or kodeNegaraAsal == 'ind':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : RP")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ¥")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ฿")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ₺")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ¥")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : S$")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ₩")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal.lower() == kodeNegaraTujuan.lower():
                        try:
                            masukkan = input("Masukkan Jumlah Uang : US$")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    else:
                        print(47*"=")
                        print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nAnda Bisa Ketik 'BACK' Untuk Keluar Dari Menu 2")
                        print(47*"=")
                break
            # * ==================================================
            # Konversi ke JPY
            elif(kodeNegaraTujuan == 'JPY' or kodeNegaraTujuan == 'jpy'):
                isLanjut = True
                while isLanjut:
                    kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                    if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                        isLanjut = False
                    elif kodeNegaraAsal == 'IND' or kodeNegaraAsal == 'ind':
                        jumlahUang = float(input("Masukkan Jumlah Uang : RP"))
                        try:
                            masukkan = input("Masukkan Jumlah Uang : US$")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'US' or kodeNegaraAsal == 'us':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : US$")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ฿")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ₺")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ¥")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : S$")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ₩")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal.lower() == kodeNegaraTujuan.lower():
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ¥")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    else:
                        print(47*"=")
                        print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nAnda Bisa Ketik 'BACK' Untuk Keluar Dari Menu 2")
                        print(47*"=")
                break
            # * ==================================================
            # Konversi ke THA
            elif(kodeNegaraTujuan == 'THA' or kodeNegaraTujuan == 'tha'):
                isLanjut = True
                while isLanjut:
                    kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                    if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                        isLanjut = False
                    elif kodeNegaraAsal == 'IND' or kodeNegaraAsal == 'ind':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : RP")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ¥")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'US' or kodeNegaraAsal == 'us':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : US$")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ₺")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ¥")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : S$")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ₩")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal.lower() == kodeNegaraTujuan.lower():
                        try:
                            masukkan = input("Masukkan Jumlah Uang : ฿")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    else:
                        print(47*"=")
                        print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nAnda Bisa Ketik 'BACK' Untuk Keluar Dari Menu 2")
                        print(47*"=")
                break
            # * ==================================================
            # Konversi ke TUR
            elif(kodeNegaraTujuan == 'TUR' or kodeNegaraTujuan == 'tur'):
                isLanjut = True
                while isLanjut:
                    kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                    if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                        isLanjut = False
                    elif kodeNegaraAsal == 'IND' or kodeNegaraAsal == 'ind':
                        try:
                            masukkan = input("Masukkan Jumlah Uang : RP")
                            jumlahUang = float(masukkan)
                            INDkeTUR = jumlahUang / 841.44
                            print(f"=> ₺{INDkeTUR:.2f}")
                            isLanjut = False
                        except:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                    elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                        masukkan = input("Masukkan Jumlah Uang : ¥")
                        if type(masukkan) != float or type(masukkan) != int:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                        else:
                            jumlahUang = float(masukkan)
                            JPYkeTUR = jumlahUang * 0.13
                            print(f"=> ₺{JPYkeTUR:.2f}")
                            isLanjut = False
                    elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                        masukkan = input("Masukkan Jumlah Uang : ฿")
                        if type(masukkan) != float or type(masukkan) != int:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                        else:
                            jumlahUang = float(masukkan)
                            THAkeTUR = jumlahUang * 0.50
                            print(f"=> ₺{THAkeTUR:.2f}")
                            isLanjut = False
                    elif kodeNegaraAsal == 'US' or kodeNegaraAsal == 'us':
                        masukkan = input("Masukkan Jumlah Uang : US$")
                        if type(masukkan) != float or type(masukkan) != int:
                            print(47*"=")
                            print("Maaf Masukkan Hanya Angka!")
                            print(47*"=")
                        else:
                            jumlahUang = float(masukkan)
                            USkeTUR = jumlahUang * 18.61
                            print(f"=> ₺{USkeTUR:.2f}")
                            isLanjut = False
                    elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                        
                        jumlahUang = float(input("Masukkan Jumlah Uang : ¥"))
                        CNYkeTUR = jumlahUang * 2.56
                        print(f"=> ₺{CNYkeTUR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                        
                        jumlahUang = float(input("Masukkan Jumlah Uang : S$"))
                        SGDkeTUR = jumlahUang * 13.26
                        print(f"=> ₺{SGDkeTUR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                        
                        jumlahUang = float(input("Masukkan Jumlah Uang : ₩"))
                        KORkeTUR = jumlahUang * 0.014
                        print(f"=> ₺{KORkeTUR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal.lower() == kodeNegaraTujuan.lower():
                        
                        jumlahUang = float(input("Masukkan Jumlah Uang : ₺"))
                        print(f"=> ₺{jumlahUang:.2f}")
                        isLanjut = False
                    else:
                        print(47*"=")
                        print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nAnda Bisa Ketik 'BACK' Untuk Keluar Dari Menu 2")
                        print(47*"=")
                break
            # * ==================================================
            # Konversi ke CNY
            elif(kodeNegaraTujuan == 'CNY' or kodeNegaraTujuan == 'cny'):
                isLanjut = True
                while isLanjut:
                    kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                    if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                        isLanjut = False
                    elif kodeNegaraAsal == 'IND' or kodeNegaraAsal == 'ind':
                        jumlahUang = float(input("Masukkan Jumlah Uang : RP"))
                        print(47*"=")
                        INDkeCNY = jumlahUang / 2167.98
                        print(f"=> ¥{INDkeCNY:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ¥"))
                        print(47*"=")
                        JPYkeCNY = jumlahUang * 0.050
                        print(f"=> ¥{JPYkeCNY:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ฿"))
                        print(47*"=")
                        THAkeCNY = jumlahUang * 0.19
                        print(f"=> ¥{THAkeCNY:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ₺"))
                        print(47*"=")
                        TURkeCNY = jumlahUang * 0.39
                        print(f"=> ¥{TURkeCNY:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'US' or kodeNegaraAsal == 'us':
                        jumlahUang = float(input("Masukkan Jumlah Uang : US$"))
                        print(47*"=")
                        USkeCNY = jumlahUang * 7.25
                        print(f"=> ¥{USkeCNY:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                        jumlahUang = float(input("Masukkan Jumlah Uang : S$"))
                        print(47*"=")
                        SGDkeCNY = jumlahUang * 5.17
                        print(f"=> ¥{SGDkeCNY:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ₩"))
                        print(47*"=")
                        KORkeCNY = jumlahUang * 0.0053
                        print(f"=> ¥{KORkeCNY:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal.lower() == kodeNegaraTujuan.lower():
                        jumlahUang = float(input("Masukkan Jumlah Uang : ¥"))
                        print(47*"=")
                        print(f"=> ¥{jumlahUang:.2f}")
                        isLanjut = False
                    else:
                        print(47*"=")
                        print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nAnda Bisa Ketik 'BACK' Untuk Keluar Dari Menu 2")
                        print(47*"=")
                break
            # * ==================================================
            # Konversi ke SGD
            elif(kodeNegaraTujuan == 'SGD' or kodeNegaraTujuan == 'sgd'):
                isLanjut = True
                while isLanjut:
                    kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                    if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                        isLanjut = False
                    elif kodeNegaraAsal == 'IND' or kodeNegaraAsal == 'ind':
                        jumlahUang = float(input("Masukkan Jumlah Uang : RP"))
                        print(47*"=")
                        INDkeSGD = jumlahUang / 11043
                        print(f"=> S${INDkeSGD:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ¥"))
                        print(47*"=")
                        JPYkeSGD = jumlahUang * 0.0096
                        print(f"=> S${JPYkeSGD:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ฿"))
                        print(47*"=")
                        THAkeSGD = jumlahUang * 0.038
                        print(f"=> S${THAkeSGD:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ₺"))
                        print(47*"=")
                        TURkeSGD = jumlahUang * 0.075
                        print(f"=> S${TURkeSGD:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ¥"))
                        print(47*"=")
                        CNYkeSGD = jumlahUang * 0.19
                        print(f"=> S${CNYkeSGD:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'US' or kodeNegaraAsal == 'us':
                        jumlahUang = float(input("Masukkan Jumlah Uang : US$"))
                        print(47*"=")
                        USkeSGD = jumlahUang * 1.40
                        print(f"=> S${USkeSGD:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'KOR' or kodeNegaraAsal == 'kor':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ₩"))
                        print(47*"=")
                        KORkeSGD = jumlahUang * 0.0010
                        print(f"=> S${KORkeSGD:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal.lower() == kodeNegaraTujuan.lower():
                        jumlahUang = float(input("Masukkan Jumlah Uang : S$"))
                        print(47*"=")
                        print(f"=> S${jumlahUang:.2f}")
                        isLanjut = False
                    else:
                        print(47*"=")
                        print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nAnda Bisa Ketik 'BACK' Untuk Keluar Dari Menu 2")
                        print(47*"=")
                break
            # * ==================================================
            # Konversi Ke KOR
            elif(kodeNegaraTujuan == 'KOR' or kodeNegaraTujuan == 'kor'):
                isLanjut = True
                while isLanjut:
                    kodeNegaraAsal = input("Masukkan Kode Negara Anda : ")
                    if kodeNegaraAsal == 'BACK' or kodeNegaraAsal == 'back':
                        isLanjut = False
                    elif kodeNegaraAsal == 'IND' or kodeNegaraAsal == 'ind':
                        jumlahUang = float(input("Masukkan Jumlah Uang : RP"))
                        print(47*"=")
                        INDkeKOR = jumlahUang * 0.088
                        print(f"=> ₩{INDkeKOR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'JPY' or kodeNegaraAsal == 'jpy':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ¥"))
                        print(47*"=")
                        JPYkeKOR = jumlahUang * 9.41
                        print(f"=> ₩{JPYkeKOR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'THA' or kodeNegaraAsal == 'tha':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ฿"))
                        print(47*"=")
                        THAkeKOR = jumlahUang * 36.97
                        print(f"=> ₩{THAkeKOR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'TUR' or kodeNegaraAsal == 'tur':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ₺"))
                        print(47*"=")
                        TURkeKOR = jumlahUang * 79.93
                        print(f"=> ₩{TURkeKOR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'CNY' or kodeNegaraAsal == 'cny':
                        jumlahUang = float(input("Masukkan Jumlah Uang : ¥"))
                        print(47*"=")
                        CNYkeKOR = jumlahUang * 189.64
                        print(f"=> ₩{CNYkeKOR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'SGD' or kodeNegaraAsal == 'sgd':
                        jumlahUang = float(input("Masukkan Jumlah Uang : S$"))
                        print(47*"=")
                        SGDkeKOR = jumlahUang * 980.90
                        print(f"=> ₩{SGDkeKOR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal == 'US' or kodeNegaraAsal == 'us':
                        jumlahUang = float(input("Masukkan Jumlah Uang : US$"))
                        print(47*"=")
                        USkeKOR = jumlahUang * 1378.09
                        print(f"=> ₩{USkeKOR:.2f}")
                        isLanjut = False
                    elif kodeNegaraAsal.lower() == kodeNegaraTujuan.lower():
                        jumlahUang = float(input("Masukkan Jumlah Uang : ₩"))
                        print(47*"=")
                        print(f"=> ₩{jumlahUang:.2f}")
                        isLanjut = False
                    else:
                        print(47*"=")
                        print("Maaf Kode Negara Anda Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia\nAnda Bisa Ketik 'BACK' Untuk Keluar Dari Menu 2")
                        print(47*"=")
                break
            else:
                print(47*"=")
                print("Maaf Kode Negara Tidak Tersedia\nAnda Dapat Mencoba Kode Yang Tersedia")
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