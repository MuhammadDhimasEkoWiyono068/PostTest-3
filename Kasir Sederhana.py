menu="ya"
while menu=="ya" or menu=="Ya":
    print("=============================================")
    print("~~~~~~~~~~~Warung Bakso Mas Dhimas~~~~~~~~~~~")
    print("---------------------------------------------")
    print("                  List Menu                  ")

    harga=0
    diskon=0
    totalharga=0
    JenisMakanan=""
    porsi=0

    def daftarmenu():
        global harga
        global diskon
        global totalharga
        global JenisMakanan
        global porsi
        print("=============================================")
        print("| No |   Nama Menu         | Harga | Diskon |")
        print("---------------------------------------------")
        print("| 1  | Bakso Biasa         | 18000 |  10%   |")
        print("| 2  | Bakso Special       | 25000 |  10%   |")
        print("| 3  | Bakso Jumbo         | 50000 |  10%   |")
        print("| 4  | Bakso Jumbo Special | 80000 |  25%   |")
        print("=============================================")
        pilih=int(input("Masukkan angka sesuai dengan menu yang tersedia = "))
        if pilih==1:
            porsi=int(input("Jumlah dibeli = "))
            JenisMakanan="Bakso Biasa"
            harga=int(porsi*18000)
            diskon=int(harga*0.1)
            totalharga=int(harga-diskon)
            print(porsi,"Porsi Bakso Biasa     = RP.",harga)
            print("Potongan Harga 10%      = Rp.",diskon)
            print("Harga Akhir             = Rp.",totalharga)
        elif pilih==2:
            porsi=int(input("Jumlah dibeli = "))
            JenisMakanan="Bakso Special"
            harga=int(porsi*25000)
            diskon=int(harga*0.1)
            totalharga=int(harga-diskon)
            print(porsi,"Porsi Bakso Biasa     = RP.",harga)
            print("Potongan Harga 10%      = Rp.",diskon)
            print("Harga Akhir             = Rp.",totalharga)
        elif pilih==3:
            porsi=int(input("Jumlah dibeli = "))
            JenisMakanan="Bakso Jumbo"
            harga=int(porsi*50000)
            diskon=int(harga*0.1)
            totalharga=int(harga-diskon)
            print(porsi,"Porsi Bakso Biasa     = RP.",harga)
            print("Potongan Harga 10%      = Rp.",diskon)
            print("Harga Akhir             = Rp.",totalharga)
        elif pilih==4:
            porsi=int(input("Jumlah dibeli = "))
            JenisMakanan="Bakso Jumbo Special"
            harga=int(porsi*80000)
            diskon=int(harga*0.25)
            totalharga=int(harga-diskon)
            print(porsi,"Porsi Bakso Biasa     = RP.",harga)
            print("Potongan Harga 25%      = Rp.",diskon)
            print("Harga Akhir             = Rp.",totalharga)
        else:
            print("Pilihan tidak ada, silahkan masukan lagi!!!")
            daftarmenu()

    daftarmenu()
    
    uang=int(input("Uang Tunai Pembeli      = Rp. "))
    kembalian=int(uang-totalharga)
    print("======================================")
    print("Nama Pesanan     :", JenisMakanan)
    print("Jumlah Pesanan   :", porsi)
    print("Harga            : Rp.",harga)
    print("Potongan Harga   : Rp.",diskon)
    print("--------------------------------------")
    print("Total Pembayaran : Rp.",totalharga)
    print("Pembayaran Tunai : Rp.",uang)
    print("Kembalian        : Rp.",kembalian)
    print("======================================")
    menu=(input("Ingin Mengulang Program ? [Ya/Tidak] : "))