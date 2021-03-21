def tambahMundur():
    tempx = ""  #str kosong untuk membalik x jika syarat sudah terpenuhi
    tempy = ""  #str kosong untuk membalik y jika syarat sudah terpenuhi
    tempxy =""  #str kosong untuk membalik hasil tambah mundur
    x = input("Masukkan angka 1 : ")
    if x.isnumeric():   #cek jika inputan x berupa angka
        checkx = int(x) #menjadikan x sebagai integer agar bisa di cek tahap selanjutnya
        if checkx < 359999: #cek jika inputan x kurang dari 3599999
            y = input("Masukkan angka 2 : ")
            if y.isnumeric():   #cek jika inputan y berupa angka
                checky = int(y) #menjadikan y sebagai integer agar bisa di cek tahap selanjutnya
                if checky < 359999: #cek jika inputan y kurang dari 3599999
                    for i in range(len(x)-1,-1,-1): 
                        tempx += x[i]   #membalik karakter x dari belakang ke depan
                        intx = int(tempx)   #menjadikan tempx menjadi integer agar bisa dijumlahkan
                    for i in range(len(y)-1,-1,-1):
                        tempy += y[i]   #membalik karakter y dari belakang ke depan
                        inty = int(tempy)   #menjadikan tempy menjadi integer agar bisa dijumlahkan
                    jumlahxy = intx + inty  #jumlahkan x dan y yg sudah dibalik
                    strxy = str(jumlahxy)   #menjadikan hasil tambah mundur menjadi string agar bisa di cacah balik
                    for i in range(len(strxy)-1,-1,-1):
                        tempxy += strxy[i]  #membalik karakter hasil tambah mundur dari belakang ke depan
                        intxy = int(tempxy) #menjadikan hasil tambah mundur yang telah dibalik ke integer (sesuai permintaan soal)
                    print("Hasil tambah mundurnya : ",intxy)   
                else: 
                    print("Invalid Input!") #jika syarat y melebihi 359999
            else: 
                print("Invalid Input!") #jika syarat y bukan integer
        else: 
            print("Invalid Input!") #jika syarat x melebihi 359999
    else: 
        print("Invalid Input!") #jika syarat x bukan integer

tambahMundur()
