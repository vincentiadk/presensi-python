#import library 2 dimensi
import Dimensi2.segitiga as segitiga
import Dimensi2.segitiga as persegi
import Dimensi2.segitiga as persegi_panjang
import Dimensi2.lingkaran as lingkaran
import Dimensi2.trapesium as trapesium
import Dimensi2.jajar_genjang as jajar_genjang
#import library 3 dimensi
import Dimensi3.kubus as kubus
import Dimensi2.segitiga as limas
import Dimensi2.segitiga as prisma
import Dimensi3.bola as bola
import Dimensi3.tabung as tabung
import Dimensi3.balok as balok

import time

masterBangunRuang=[]
masterBangunRuang.append([segitiga,persegi,persegi_panjang,lingkaran,trapesium,jajar_genjang])
masterBangunRuang.append([kubus,limas,prisma,bola,tabung,balok])

print("=================================== \n||   CALCULATOR BANGUN RUANG     ||\n===================================")

def inputAttr(attr) :
    print("Masukkan "+attr+" : ", end="")
    return float(input())

exit = False
while (exit!=True):
    #Memilih jenis dimensi
    print("Pilih jenis dimensi(2D/3D):")
    jenisDimensi = input().upper()
    if(jenisDimensi == "2D"):
        print("\nBangunan 2D \n 1. Segitiga\n 2. Persegi\n 3. Persegi Panjang\n 4. Lingkaran\n 5. Trapesium\n 6. Jajar Genjang\nPilih nomor bangun ruang:", end=" ")
        bangunRuang = masterBangunRuang[0]
    elif(jenisDimensi=="3D"):
        print("\nBangunan 3D \n 1. Kubus\n 2. Limas Segi-n\n 3. Prisma Segi-n\n 4. Bola\n 5. Tabung\n 6. Balok \nPilih nomor bangun ruang:", end=" ")
        bangunRuang = masterBangunRuang[1]
    else:
        bangunRuang =[]
        print("Perintah yang Anda masukan salah, silakan coba kembali")
        continue
    
    #Memilih Jenis bangun ruang
    jenisBangunRuang = int(input())
    if(jenisBangunRuang>=0 and jenisBangunRuang<=6):
        bangunanTerpilih = bangunRuang[jenisBangunRuang-1]
        atributeBangunan = bangunanTerpilih.getAttributes()
        jumlahAtribut = len(atributeBangunan)
        inputUsers = []
        for atribut in atributeBangunan:
            input_ = inputAttr(atribut)
            while (input_ <= 0) :
                print(atribut + " tidak boleh kurang atau sama dengan 0.")
                input_ = inputAttr(atribut)
            inputUsers.append(input_)
                    

        if(jumlahAtribut==1):
            print(bangunanTerpilih.getHasil(inputUsers[0]))
        elif(jumlahAtribut==2):
            print(bangunanTerpilih.getHasil(inputUsers[0],inputUsers[1]))
        elif(jumlahAtribut==3):
            print(bangunanTerpilih.getHasil(inputUsers[0],inputUsers[1],inputUsers[2]))
        elif(jumlahAtribut==4):
            print(bangunanTerpilih.getHasil(inputUsers[0],inputUsers[1],inputUsers[2],inputUsers[3]))
        
        time.sleep(1)
        print("Apakah Anda sudah selesai menggunakan kalkulator?(Y/N)", end=" ")
        isSelesai = input().upper()
        if(isSelesai=="Y"):
            exit=True
    else:
        print("Perintah yang Anda masukan salah, silakan coba kembali")
        continue


