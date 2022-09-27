# username admin = adminkomc
# passowrd admin = admin123

# library
import msvcrt as m
import os
import shutil

# clearscreen
os.system("cls")

# file needed
source = "data.txt"
pindah = "coba.txt"

# function for checking mahsiswa
def mahasiswaCheck(nama, umur, nim):
    # open source file
    check = open(source)

    for col, data in enumerate(check):
        if nama in data and umur in data and nim in data:
            # return True if all data are same
            return True
    
    # else return False
    return False

# function for choose the status (mahasiswa / admin)
def pilihStatus():
    status = 0

    # checking status must be 1 or 2
    while status != 1 and status != 2:
        # clearscreen
        os.system("cls")

        print("================================")
        print("|   Database Mahasiswa Kom C   |")
        print("================================")
        print("| 1. Admin                     |")
        print("| 2. Mahasiswa/mahasiswi       |")
        print("--------------------------------")
        status = int(input("Masukkan status Anda[1/2] : "))
        print("--------------------------------")

        # checking status not 1 and 2
        if status != 1 and status != 2 :
            print("Inputan Anda salah, silahkan tekan \"Enter\"")
            # to make user press any key
            m.getch()    

    # getting status from pilihStatus
    return status # 1

# function for checking the status
def checkStatus(status):
    # if status is admin
    if status == 1:
        username_admin = password_admin = " "

        # checking username_admin and password_admin
        while username_admin != "adminkomc" or password_admin != "admin123":
            os.system("cls")

            print("==================================")
            print("   SELAMAT DATANG ADMIN KOM C")
            print("==================================")
            username_admin = input("Masukkan username     : ")
            password_admin = input("Massukkan password    : ")

            if username_admin != "adminkomc" or password_admin != "admin123":
                print("----------------------------------")
                print("Username atau password Anda salah")
                print("Silahkan tekan \"Enter\"")
                m.getch()
        
        ulang = True

        while ulang:
            # clearscreen
            os.system("cls")

            print("================================")
            print("             PILIH       ")
            print("================================")
            print("1. Lihat semua data")
            print("2. Cari data")
            print("3. Hapus data")

            print("--------------------------------")
            admin_pilih = int(input("Input pilihan Anda : "))            
            print("--------------------------------")

            if admin_pilih == 1:
                ulang = False
                os.system("cls")

                judul_nama = 'nama'.center(20)
                judul_umur = 'umur'.center(6)
                judul_nim = 'nim'.center(14)

                print("="*40)
                print("|" +  "Data Kom C".center(38) + "|")
                print("="*40)
                
                print(judul_nama + judul_umur + judul_nim)
                print("-"*40)

                with open(source) as file:
                    print(file.read())

            elif admin_pilih == 2:
                ulang = False
                nama = input("Masukkan nama yang dicari : ")

                # open source file
                database = open(source)
                count = batas = 0
                # int count, batas;

                for col, data in enumerate(database):
                    batas += 1
                    if nama in data:
                        cari = data.split()
                        os.system("cls")

                        # spliting nama, umur, nim from list 
                        nama = " ".join(cari[:-2])
                        umur = cari[-2]
                        nim = cari [-1]

                        print("-"*30)
                        print("Data".center(30))
                        print("-"*30)
                        print(f"Nama : {nama}")
                        print(f"Umur : {umur}")
                        print(f"Nim  : {nim}")
                        print("-"*30)

                    else:
                        count += 1

                if count == batas:
                    print('--------------------------------')
                    print("Hasil : Data tidak ditemukan")
                    print("================================")

            elif admin_pilih == 3:
                ulang = False
                yes = True

                while yes:
                    with open(pindah, "w") as file:
                        file.write("")

                    hapus = input("Masukkan nama : ")

                    count = batas = 0
                    database = open(source)
                    
                    for col, data in enumerate(database):
                        batas += 1
                        if hapus in data:
                            continue
                        else:
                            with open(pindah, "a") as file:
                                file.write(data)
                                count += 1
                    
                    # checking if batas equal count
                    if count == batas :
                        print(f"{hapus} tidak terdaftar di kom C")
                        print("Tekan \"Enter\" untuk menginput ulang")
                        m.getch()
                    
                    else:
                        yes = False
                        with open(source, "w") as file:
                            file.write("")

                        # copying pindah to source
                        shutil.copyfile(pindah, source)

                        # clearscreen
                        os.system("cls")

                        judul_nama = 'nama'.ljust(20)
                        judul_umur = 'umur'.center(6)
                        judul_nim = 'nim'.center(14)

                        print("="*40)
                        print("|" + "Data Baru Kom C".center(38) + "|")
                        print("="*40)
                        
                        # creating table title
                        print(judul_nama + judul_umur + judul_nim)
                        print("-"*40)

                        with open(source) as file:
                            # reading source file
                            print(file.read())

            else:
                print("Pilihan Anda salah, tekan \"Enter\" untuk input ulang")
                m.getch()

    # if user is mahasiswa
    elif status == 2:
        # clearscreen
        os.system("cls")

        print("================================")
        print("             PILIH       ")
        print("================================")
        print("1. Daftar ")
        print("2. Update data")
        
        print("--------------------------------")
        mahasiswa_pilih = int(input("Input pilihan Anda : "))            
        print("--------------------------------")    

        if mahasiswa_pilih == 1:
            mahasiswa_nama = input("Nama : ")[:20]
            mahasiswa_umur = input("umur : ")[:2]
            mahasiswa_nim = input("Nim  : ")[:12]

            # appending source file
            with open(source, "a") as file:
                # unite all splitting data
                tambah = f"{mahasiswa_nama.ljust(20)}{mahasiswa_umur.center(6)}{mahasiswa_nim.center(14)}\n"
                file.write(tambah)

            print("==========================================")
            print(f"Selamat datang di Kom C {mahasiswa_nama} !!!")
            print("==========================================")

        elif mahasiswa_pilih == 2:
            mahasiswa_nama = input("Nama : ")
            mahasiswa_umur = input("Umur : ")
            mahasiswa_nim = input("Nim  : ")

            # checking data in kom c or nah
            hasil = mahasiswaCheck(mahasiswa_nama, mahasiswa_umur, mahasiswa_nim)

            if hasil:
                # clearscreeen
                os.system("cls")

                print("================================")
                print("             PILIH       ")
                print("================================")
                print("1. update nama ")
                print("2. Update umur")
                print("--------------------------------")
                mahasiswa_update = int(input("Input pilihan Anda : "))            
                print("--------------------------------")    

                # selecting choosen menu
                if mahasiswa_update == 1:
                    mahasiswa_nama_baru = input("Nama baru : ")[:20]
                    hasil = f"{mahasiswa_nama_baru.ljust(20)}{mahasiswa_umur.center(6)}{mahasiswa_nim.center(14)}\n"
                
                elif mahasiswa_update == 2:
                    mahasiswa_umur_baru = input("Umur baru : ")[:2]
                    hasil = f"{mahasiswa_nama.ljust(20)}{mahasiswa_umur_baru.center(6)}{mahasiswa_nim.center(14)}\n"

                # deleting "coba.txt"'s content
                with open("coba.txt", 'w') as file:
                    file.write("")
                     
                # open source variable
                database = open(source)     

                for col, data in enumerate(database):
                    if mahasiswa_nama in data:
                        # appending pindah with changed data
                        with open(pindah, "a") as file:
                            file.write(hasil)
                    else:
                        with open(pindah, "a") as file:
                            file.write(data)

                # deleting source content
                with open(source, "w") as file:
                    file.write("")

                # coppying pindah to source
                shutil.copyfile(pindah, source)
                print("--------------------------------")    
                print("Data Anda sudah diperbaharui")
                print("================================")

            else:
                print("--------------------------------")    
                print("Maaf Anda belum terdaftar :(")
                print("================================")

# main code
status = pilihStatus()
checkStatus(status)