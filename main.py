# Konversi Mata Uang App

# Mata Uang : IND, US, JPY, THA, SBP
list_mata_uang = ['IND', 'US', 'JPY', 'THA', 'TUR']

while True:
    print(35*"=")
    print(f"Mata Uang Yang Tersedia\n{list_mata_uang}")
    print(10*"=","PILIHAN MENU APLIKASI",10*"=")
    print("1.Konversi keseluruh mata uang yang tersedia")
    print("2.Konversi ke salah satu mata uang")
    pilihan = int(input("=>"))
    
    # Operasi Pilihan Pertama
    if(pilihan == 1):
        mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
        dollarKeRupiah = mata_uang_sekarang // 14000
        print(f"Hasil Konversi\n=>(US)Dollar = {dollarKeRupiah}\n=>(JPY)Jepang = {dollarKeRupiah}")
    # Operasi Pilihan Kedua
    elif(pilihan == 2):
        kode_mata_uang = input("Masukkan Kode Mata Uang : ")
        # Konversi ke US
        if(kode_mata_uang == 'US'):
            mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
            dollarKeRupiah = mata_uang_sekarang / 14000
            print(f"Hasil Konversi {dollarKeRupiah} Dollar")
        
        # Konversi ke JPY

        # Konversi ke THA

        # Konversi ke TUR
        if(kode_mata_uang == 'TUR'):
            mata_uang_sekarang = int(input("Masukkan Mata Uang Sekarang : Rp."))
            LIRAKeRupiah = mata_uang_sekarang / 841.44
            print(f"Hasil Konversi {LIRAKeRupiah} LIRA")
        

    print(35*"=")
    isSelesai = input("Apakah Sudah Selesai\n1.yes\n2.no\n=>")
    if int(isSelesai) == 1:
        break