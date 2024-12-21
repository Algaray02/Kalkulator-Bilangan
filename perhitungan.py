from colorama import Fore, Style
import time, os
  
def kondesbiner(n):
    hasil = bin(n)[2:]
    des = n
    print(Fore.LIGHTCYAN_EX+"==DESIMAL -> BINER=="+Style.RESET_ALL)
    while n > 0:
        hitung = n/2
        if n%2 == 0:
            if n >= 1000:
                print(f"{n} : 2    = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif n >= 100 and n < 1000 and hitung >= 100:
                print(f"{n} : 2     = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif n >= 100 and n < 1000 and hitung < 100:
                print(f"{n} : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif n >= 10 and n < 100 and hitung >= 10:
                print(f"{n}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif n >= 10 and n < 100 and hitung < 10:
                print(f"{n}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif n < 10:
                print(f"{n}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
        elif n%2 == 1:
            hitung -= 0.5
            if n >= 1000:
                print(f"{n} : 2   = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif n >= 100 and n < 1000 and hitung >= 100:
                print(f"{n} : 2     = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif n >= 100 and n < 1000 and hitung < 100:
                print(f"{n} : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif n >= 10 and n < 100 and hitung >= 10:
                print(f"{n}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif n >= 10 and n < 100 and hitung < 10:
                print(f"{n}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif n < 10:
                print(f"{n}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
        n = int(hitung)
    print(f"Bilangan Biner dari {des} =",Fore.GREEN+f"{hasil}"+Style.RESET_ALL)

def kondesoktal(n):
    hasil = oct(n)[2:]
    des = n
    os.system("cls")
    print(Fore.LIGHTCYAN_EX+"==DESIMAL -> OKTAL=="+Style.RESET_ALL)
    while n > 0:
        hitung = n/8
        if n >= 1000:
            print(f"{n} : 8    = {int(hitung)} sisa",Fore.GREEN+f"{n%8}"+Style.RESET_ALL)
        elif n >= 100 and n < 1000 and hitung >= 100:
            print(f"{n} : 8     = {int(hitung)} sisa",Fore.GREEN+f"{n%8}"+Style.RESET_ALL)
        elif n >= 100 and n < 1000 and hitung < 100:
            print(f"{n} : 8     = {int(hitung)}  sisa",Fore.GREEN+f"{n%8}"+Style.RESET_ALL)
        elif n >= 10 and n < 100 and hitung >= 10:
            print(f"{n}  : 8     = {int(hitung)}  sisa",Fore.GREEN+f"{n%8}"+Style.RESET_ALL)
        elif n >= 10 and n < 100 and hitung < 10:
            print(f"{n}  : 8     = {int(hitung)}   sisa",Fore.GREEN+f"{n%8}"+Style.RESET_ALL)
        elif n < 10:
            print(f"{n}   : 8     = {int(hitung)}   sisa",Fore.GREEN+f"{n%8}"+Style.RESET_ALL)
        n = int(hitung)
    print(f"Bilangan Oktal dari {des} =",Fore.GREEN+f"{hasil}"+Style.RESET_ALL)

def kondesheksa(n):
    hasil =  hex(n)[2:]
    des = n
    print(Fore.LIGHTCYAN_EX+"==DESIMAL -> HEKSA=="+Style.RESET_ALL)
    while n > 0:
        hitung = n/16
        if n%16 < 10:
            if n >= 1000:
                print(f"{n} : 16    = {int(hitung)} sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
            elif n >= 100 and n < 1000 and hitung >= 100:
                print(f"{n} : 16     = {int(hitung)} sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
            elif n >= 100 and n < 1000 and hitung < 100:
                print(f"{n} : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
            elif n >= 10 and n < 100 and hitung >= 10:
                print(f"{n}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
            elif n >= 10 and n < 100 and hitung < 10:
                print(f"{n}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
            elif n < 10 and int(hitung) > 0:
                print(f"{n}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
            elif n < 10 and n >= 5 and int(hitung) == 0:
                print(f"{n}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
            elif n < 10  and n < 5 and int(hitung) == 0:
                print(f"{n}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
        elif n%16 >= 10:
            if n%16 == 10: val = 'A'
            elif n%16 == 11: val = 'B'
            elif n%16 == 12: val = 'C'
            elif n%16 == 13: val = 'D'
            elif n%16 == 14: val = 'E'
            elif n%16 == 15: val = 'F'
            if n >= 1000:
                print(f"{n} : 16    = {int(hitung)} sisa",Fore.GREEN+f"{n%16}({val})"+Style.RESET_ALL)
            elif n >= 100 and n < 1000 and hitung >= 100:
                print(f"{n} : 16     = {int(hitung)} sisa",Fore.GREEN+f"{n%16}({val})"+Style.RESET_ALL)
            elif n >= 100 and n < 1000 and hitung < 100:
                print(f"{n} : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}({val})"+Style.RESET_ALL)
            elif n >= 10 and n < 100 and hitung >= 10:
                print(f"{n}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}({val})"+Style.RESET_ALL)
            elif n >= 10 and n < 100 and hitung < 10:
                print(f"{n}  : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{n%16}({val})"+Style.RESET_ALL)
            elif n < 10 and int(hitung) > 0:
                print(f"{n}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}({val})"+Style.RESET_ALL)
            elif n < 10  and n >= 5 and int(hitung) == 0:
                print(f"{n}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
            elif n < 10  and n < 5 and int(hitung) == 0:
                print(f"{n}   : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{n%16}"+Style.RESET_ALL)
        n = int(hitung)
    print(f"Bilangan Heksadesimal dari {des} =",Fore.GREEN+f"{hasil.upper()}"+Style.RESET_ALL)

def konheksades(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 16)
    for i in n:
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.LIGHTCYAN_EX+"==HEKSA -> DESIMAL=="+Style.RESET_ALL)
    for x in pangkat:
        pingkit = pow(16, x)
        if val[u] >= 10:
            if val[u] == 10: valu = 'A'
            elif val[u] == 11: valu = 'B'
            elif val[u] == 12: valu = 'C'
            elif val[u] == 13: valu = 'D'
            elif val[u] == 14: valu = 'E'
            elif val[u] == 15: valu = 'F'
            print(f"(16^{x}) x {val[u]}({valu})\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        else:
            print(f"(16^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)

        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL)

def konoktaldes(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 8)
    for i in n:
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.LIGHTCYAN_EX+"==OKTAL -> DESIMAL=="+Style.RESET_ALL)
    for x in pangkat:
        pingkit = pow(8, x)
        print(f"(8^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL)

def konbinerdes(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 2)
    for i in n:
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.LIGHTCYAN_EX+"==BINER -> DESIMAL=="+Style.RESET_ALL)
    for x in pangkat:
        pingkit = pow(2, x)
        print(f"(2^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL) 

def konbineroktal(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 2)
    for i in n:
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.CYAN+"==BINER -> OKTAL=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Biner Ke Desimal--"+Style.RESET_ALL)    
    for x in pangkat:
        pingkit = pow(2, x)
        print(f"(2^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL) 

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Desimal Ke Oktal--"+Style.RESET_ALL)  
    hasil2 = oct(hasil)[2:]
    des = hasil
    while hasil > 0:
        hitung = hasil/8
        if hasil >= 1000:
            print(f"{hasil} : 8    = {int(hitung)} sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil >= 100 and hasil < 1000 and hitung >= 100:
            print(f"{hasil} : 8     = {int(hitung)} sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil >= 100 and hasil < 1000 and hitung < 100:
            print(f"{hasil} : 8     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil >= 10 and hasil < 100 and hitung >= 10:
            print(f"{hasil}  : 8     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil >= 10 and hasil < 100 and hitung < 10:
            print(f"{hasil}  : 8     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil < 10:
            print(f"{hasil}   : 8     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        hasil = int(hitung)
    print(f"Bilangan Oktal dari {des} =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL)

def konbinerheksa(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 2)
    for i in n:
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.CYAN+"==BINER -> HEKSADESMAL=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Biner Ke Desimal--"+Style.RESET_ALL)     
    for x in pangkat:
        pingkit = pow(2, x)
        print(f"(2^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL) 

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Desimal Ke Heksa--"+Style.RESET_ALL)
    hasil2 =  hex(hasil)[2:]
    des = hasil
    while hasil > 0:
        hitung = hasil/16
        if hasil%16 < 10:
            if hasil >= 1000:
                print(f"{hasil} : 16    = {int(hitung)} sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung >= 100:
                print(f"{hasil} : 16     = {int(hitung)} sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung < 100:
                print(f"{hasil} : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung >= 10:
                print(f"{hasil}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung < 10:
                print(f"{hasil}  : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil < 10 and int(hitung) > 0:
                print(f"{hasil}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil < 10 and hasil >= 5 and int(hitung) == 0:
                print(f"{hasil}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil < 10  and hasil < 5 and int(hitung) == 0:
                print(f"{hasil}   : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
        elif hasil%16 >= 10:
            if hasil%16 == 10: val = 'A'
            elif hasil%16 == 11: val = 'B'
            elif hasil%16 == 12: val = 'C'
            elif hasil%16 == 13: val = 'D'
            elif hasil%16 == 14: val = 'E'
            elif hasil%16 == 15: val = 'F'
            if hasil >= 1000:
                print(f"{hasil} : 16    = {int(hitung)} sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung >= 100:
                print(f"{hasil} : 16     = {int(hitung)} sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung < 100:
                print(f"{hasil} : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung >= 10:
                print(f"{hasil}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung < 10:
                print(f"{hasil}  : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil < 10 and int(hitung) > 0:
                print(f"{hasil}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil < 10  and hasil >= 5 and int(hitung) == 0:
                print(f"{hasil}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil < 10  and hasil < 5 and int(hitung) == 0:
                print(f"{hasil}   : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
        hasil = int(hitung)
    print(f"Bilangan Heksadesimal dari {des} =",Fore.GREEN+f"{hasil2.upper()}"+Style.RESET_ALL)

def konoktalbiner(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 8)
    for i in n:
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.CYAN+"==OKTAL -> BINER=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Oktal Ke Desimal--"+Style.RESET_ALL)
    for x in pangkat:
        pingkit = pow(8, x)
        print(f"(8^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Desimal Ke Biner--"+Style.RESET_ALL)
    hasil2 = bin(hasil)[2:]
    des = hasil
    while hasil > 0:
        hitung = hasil/2
        if hasil%2 == 0:
            if hasil >= 1000:
                print(f"{hasil} : 2    = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung >= 100:
                print(f"{hasil} : 2     = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung < 100:
                print(f"{hasil} : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung >= 10:
                print(f"{hasil}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung < 10:
                print(f"{hasil}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil < 10:
                print(f"{hasil}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
        elif hasil%2 == 1:
            hitung -= 0.5
            if hasil >= 1000:
                print(f"{hasil} : 2   = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung >= 100:
                print(f"{hasil} : 2     = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung < 100:
                print(f"{hasil} : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung >= 10:
                print(f"{hasil}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung < 10:
                print(f"{hasil}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil < 10:
                print(f"{hasil}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
        hasil = int(hitung)
    print(f"Bilangan Biner dari {des} =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL)

def konoktalheksa(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 8)
    for i in n:
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.CYAN+"==OKTAL -> HEKSA=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Oktal Ke Desimal--"+Style.RESET_ALL)
    for x in pangkat:
        pingkit = pow(8, x)
        print(f"(8^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Desimal Ke Heksa--"+Style.RESET_ALL)
    hasil2 =  hex(hasil)[2:]
    des = hasil
    while hasil > 0:
        hitung = hasil/16
        if hasil%16 < 10:
            if hasil >= 1000:
                print(f"{hasil} : 16    = {int(hitung)} sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung >= 100:
                print(f"{hasil} : 16     = {int(hitung)} sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung < 100:
                print(f"{hasil} : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung >= 10:
                print(f"{hasil}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung < 10:
                print(f"{hasil}  : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil < 10 and int(hitung) > 0:
                print(f"{hasil}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil < 10 and hasil >= 5 and int(hitung) == 0:
                print(f"{hasil}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil < 10  and hasil < 5 and int(hitung) == 0:
                print(f"{hasil}   : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
        elif hasil%16 >= 10:
            if hasil%16 == 10: val = 'A'
            elif hasil%16 == 11: val = 'B'
            elif hasil%16 == 12: val = 'C'
            elif hasil%16 == 13: val = 'D'
            elif hasil%16 == 14: val = 'E'
            elif hasil%16 == 15: val = 'F'
            if hasil >= 1000:
                print(f"{hasil} : 16    = {int(hitung)} sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung >= 100:
                print(f"{hasil} : 16     = {int(hitung)} sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung < 100:
                print(f"{hasil} : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung >= 10:
                print(f"{hasil}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung < 10:
                print(f"{hasil}  : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil < 10 and int(hitung) > 0:
                print(f"{hasil}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}({val})"+Style.RESET_ALL)
            elif hasil < 10  and hasil >= 5 and int(hitung) == 0:
                print(f"{hasil}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
            elif hasil < 10  and hasil < 5 and int(hitung) == 0:
                print(f"{hasil}   : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%16}"+Style.RESET_ALL)
        hasil = int(hitung)
    print(f"Bilangan Heksadesimal dari {des} =",Fore.GREEN+f"{hasil2.upper()}"+Style.RESET_ALL)

def konheksabiner(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 16)
    for i in n:
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.CYAN+"==HEKSA -> BINER=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Heksa Ke Desimal--"+Style.RESET_ALL)
    for x in pangkat:
        pingkit = pow(16, x)
        if val[u] >= 10:
            if val[u] == 10: valu = 'A'
            elif val[u] == 11: valu = 'B'
            elif val[u] == 12: valu = 'C'
            elif val[u] == 13: valu = 'D'
            elif val[u] == 14: valu = 'E'
            elif val[u] == 15: valu = 'F'
            print(f"(16^{x}) x {val[u]}({valu})\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        else:
            print(f"(16^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)

        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Desimal Ke Biner--"+Style.RESET_ALL)
    hasil2 = bin(hasil)[2:]
    des = hasil
    while hasil > 0:
        hitung = hasil/2
        if hasil%2 == 0:
            if hasil >= 1000:
                print(f"{hasil} : 2    = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung >= 100:
                print(f"{hasil} : 2     = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung < 100:
                print(f"{hasil} : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung >= 10:
                print(f"{hasil}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung < 10:
                print(f"{hasil}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasil < 10:
                print(f"{hasil}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
        elif hasil%2 == 1:
            hitung -= 0.5
            if hasil >= 1000:
                print(f"{hasil} : 2   = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung >= 100:
                print(f"{hasil} : 2     = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil >= 100 and hasil < 1000 and hitung < 100:
                print(f"{hasil} : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung >= 10:
                print(f"{hasil}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil >= 10 and hasil < 100 and hitung < 10:
                print(f"{hasil}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasil < 10:
                print(f"{hasil}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
        hasil = int(hitung)
    print(f"Bilangan Biner dari {des} =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL)

def konheksaoktal(n):
    u = 0
    val = []
    pangkat = []
    hasil =  int(n, 16)
    for i in n:
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        val.append(int(i))
    for i in range(0, len(val)):
        pangkat.insert(0,int(i))
    os.system("cls")
    print(Fore.CYAN+"==HEKSA -> OKTAL=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Heksa Ke Desimal--"+Style.RESET_ALL)
    for x in pangkat:
        pingkit = pow(16, x)
        if val[u] >= 10:
            if val[u] == 10: valu = 'A'
            elif val[u] == 11: valu = 'B'
            elif val[u] == 12: valu = 'C'
            elif val[u] == 13: valu = 'D'
            elif val[u] == 14: valu = 'E'
            elif val[u] == 15: valu = 'F'
            print(f"(16^{x}) x {val[u]}({valu})\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)
        else:
            print(f"(16^{x}) x {val[u]}\t=",Fore.GREEN+f"{pingkit*val[u]}"+Style.RESET_ALL)

        u += 1
    print("-----------------------+")
    print(f"Desimal\t\t=",Fore.GREEN+f"{hasil}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Desimal Ke Oktal--"+Style.RESET_ALL)
    hasil2 = oct(hasil)[2:]
    des = hasil
    while hasil > 0:
        hitung = hasil/8
        if hasil >= 1000:
            print(f"{hasil} : 8    = {int(hitung)} sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil >= 100 and hasil < 1000 and hitung >= 100:
            print(f"{hasil} : 8     = {int(hitung)} sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil >= 100 and hasil < 1000 and hitung < 100:
            print(f"{hasil} : 8     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil >= 10 and hasil < 100 and hitung >= 10:
            print(f"{hasil}  : 8     = {int(hitung)}  sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil >= 10 and hasil < 100 and hitung < 10:
            print(f"{hasil}  : 8     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        elif hasil < 10:
            print(f"{hasil}   : 8     = {int(hitung)}   sisa",Fore.GREEN+f"{hasil%8}"+Style.RESET_ALL)
        hasil = int(hitung)
    print(f"Bilangan Oktal dari {des} =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL)


# Operasi Biner
def binerjum(f, g):
    hasdes = int(f, 2) + int(g, 2)
    hasbin = bin(hasdes)[2:]
    os.system("cls")
    print(Fore.CYAN+"==PENJUMLAHAN BINER=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Biner 1 Ke Desimal--"+Style.RESET_ALL)
    u1 = 0
    val1 = []
    pangkat1 = []
    hasil1 =  int(f, 2)
    for i in f:
        val1.append(int(i))
    for i in range(0, len(val1)):
        pangkat1.insert(0,int(i))    
    print(Fore.LIGHTBLACK_EX+f"Biner 1 : {f}"+Style.RESET_ALL)
    for x in pangkat1:
        pingkit1 = pow(2, x)
        print(f"(2^{x}) x {val1[u1]}\t=",Fore.GREEN+f"{pingkit1*val1[u1]}"+Style.RESET_ALL)
        u1 += 1
    print("-----------------------+")
    print(f"Desimal Biner 1 =",Fore.GREEN+f"{hasil1}"+Style.RESET_ALL) 

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Biner 2 Ke Desimal--"+Style.RESET_ALL)
    u2 = 0
    val2 = []
    pangkat2 = []
    hasil2 =  int(g, 2)
    for i in g:
        val2.append(int(i))
    for i in range(0, len(val2)):
        pangkat2.insert(0,int(i))    
    print(Fore.LIGHTBLACK_EX+f"Biner 2 : {g}"+Style.RESET_ALL)
    for x in pangkat2:
        pingkit1 = pow(2, x)
        print(f"(2^{x}) x {val2[u2]}\t=",Fore.GREEN+f"{pingkit1*val2[u2]}"+Style.RESET_ALL)
        u2 += 1
    print("-----------------------+")
    print(f"Desimal Biner 2 =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL) 

    print(Fore.LIGHTBLUE_EX+"\n--Tambahkan Desimal Biner 1 Dan Biner 2--"+Style.RESET_ALL)
    print(Fore.GREEN+f"{hasil1}"+Style.RESET_ALL,"+",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hasdes}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Hasil Pertambahan Ke Biner--"+Style.RESET_ALL)
    while hasdes > 0:
        hitung = hasdes/2
        if hasdes%2 == 0:
            if hasdes >= 1000:
                print(f"{hasdes} : 2    = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
                print(f"{hasdes} : 2     = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
                print(f"{hasdes} : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
                print(f"{hasdes}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung < 10:
                print(f"{hasdes}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes < 10:
                print(f"{hasdes}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
        elif hasdes%2 == 1:
            hitung -= 0.5
            if hasdes >= 1000:
                print(f"{hasdes} : 2   = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
                print(f"{hasdes} : 2     = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
                print(f"{hasdes} : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
                print(f"{hasdes}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung < 10:
                print(f"{hasdes}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes < 10:
                print(f"{hasdes}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
        hasdes = int(hitung)
    print(f"Hasil Pertambahan Biner 1 dan Biner 2 =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)

def binerkur(f, g):
    hasdes = int(f, 2) - int(g, 2)
    hasbin = bin(hasdes)[2:]
    os.system("cls")
    print(Fore.CYAN+"==PENGURANGAN BINER=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Biner 1 Ke Desimal--"+Style.RESET_ALL)
    u1 = 0
    val1 = []
    pangkat1 = []
    hasil1 =  int(f, 2)
    for i in f:
        val1.append(int(i))
    for i in range(0, len(val1)):
        pangkat1.insert(0,int(i))  
    print(Fore.LIGHTBLACK_EX+f"Biner 1 : {f}"+Style.RESET_ALL)  
    for x in pangkat1:
        pingkit1 = pow(2, x)
        print(f"(2^{x}) x {val1[u1]}\t=",Fore.GREEN+f"{pingkit1*val1[u1]}"+Style.RESET_ALL)
        u1 += 1
    print("-----------------------+")
    print(f"Desimal Biner 1 =",Fore.GREEN+f"{hasil1}"+Style.RESET_ALL) 

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Biner 2 Ke Desimal--"+Style.RESET_ALL)
    u2 = 0
    val2 = []
    pangkat2 = []
    hasil2 =  int(g, 2)
    for i in g:
        val2.append(int(i))
    for i in range(0, len(val2)):
        pangkat2.insert(0,int(i)) 
    print(Fore.LIGHTBLACK_EX+f"Biner 2 : {g}"+Style.RESET_ALL)  
    for x in pangkat2:
        pingkit1 = pow(2, x)
        print(f"(2^{x}) x {val2[u2]}\t=",Fore.GREEN+f"{pingkit1*val2[u2]}"+Style.RESET_ALL)
        u2 += 1
    print("-----------------------+")
    print(f"Desimal Biner 2 =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL) 

    print(Fore.LIGHTBLUE_EX+"\n--Kurangkan Desimal Biner 1 Dan Biner 2--"+Style.RESET_ALL)
    print(Fore.GREEN+f"{hasil1}"+Style.RESET_ALL,"-",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hasdes}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Hasil Pengurangan Ke Biner--"+Style.RESET_ALL)
    while hasdes > 0:
        hitung = hasdes/2
        if hasdes%2 == 0:
            if hasdes >= 1000:
                print(f"{hasdes} : 2    = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
                print(f"{hasdes} : 2     = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
                print(f"{hasdes} : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
                print(f"{hasdes}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung < 10:
                print(f"{hasdes}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes < 10:
                print(f"{hasdes}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
        elif hasdes%2 == 1:
            hitung -= 0.5
            if hasdes >= 1000:
                print(f"{hasdes} : 2   = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
                print(f"{hasdes} : 2     = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
                print(f"{hasdes} : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
                print(f"{hasdes}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung < 10:
                print(f"{hasdes}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes < 10:
                print(f"{hasdes}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
        hasdes = int(hitung)
    print(f"Hasil Pengurangan Biner 1 dan Biner 2 =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)

def binerkal(f, g):
    hasdes = int(f, 2) * int(g, 2)
    hasbin = bin(hasdes)[2:]
    os.system("cls")
    print(Fore.CYAN+"==PERKALIAN BINER=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Biner 1 Ke Desimal--"+Style.RESET_ALL)
    u1 = 0
    val1 = []
    pangkat1 = []
    hasil1 =  int(f, 2)
    for i in f:
        val1.append(int(i))
    for i in range(0, len(val1)):
        pangkat1.insert(0,int(i))
    print(Fore.LIGHTBLACK_EX+f"Biner 1 : {f}"+Style.RESET_ALL)    
    for x in pangkat1:
        pingkit1 = pow(2, x)
        print(f"(2^{x}) x {val1[u1]}\t=",Fore.GREEN+f"{pingkit1*val1[u1]}"+Style.RESET_ALL)
        u1 += 1
    print("-----------------------+")
    print(f"Desimal Biner 1 =",Fore.GREEN+f"{hasil1}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Biner 2 Ke Desimal--"+Style.RESET_ALL)
    u2 = 0
    val2 = []
    pangkat2 = []
    hasil2 =  int(g, 2)
    for i in g:
        val2.append(int(i))
    for i in range(0, len(val2)):
        pangkat2.insert(0,int(i))   
    print(Fore.LIGHTBLACK_EX+f"Biner 2 : {g}"+Style.RESET_ALL)
    for x in pangkat2:
        pingkit1 = pow(2, x)
        print(f"(2^{x}) x {val2[u2]}\t=",Fore.GREEN+f"{pingkit1*val2[u2]}"+Style.RESET_ALL)
        u2 += 1
    print("-----------------------+")
    print(f"Desimal Biner 2 =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL)  

    print(Fore.LIGHTBLUE_EX+"\n--Kalikan Desimal Biner 1 Dan Biner 2--"+Style.RESET_ALL)
    print(Fore.GREEN+f"{hasil1}"+Style.RESET_ALL,"x",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hasdes}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Hasil Perkalian Ke Biner--"+Style.RESET_ALL)
    while hasdes > 0:
        hitung = hasdes/2
        if hasdes%2 == 0:
            if hasdes >= 1000:
                print(f"{hasdes} : 2    = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
                print(f"{hasdes} : 2     = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
                print(f"{hasdes} : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
                print(f"{hasdes}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung < 10:
                print(f"{hasdes}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes < 10:
                print(f"{hasdes}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
        elif hasdes%2 == 1:
            hitung -= 0.5
            if hasdes >= 1000:
                print(f"{hasdes} : 2   = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
                print(f"{hasdes} : 2     = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
                print(f"{hasdes} : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
                print(f"{hasdes}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung < 10:
                print(f"{hasdes}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes < 10:
                print(f"{hasdes}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
        hasdes = int(hitung)
    print(f"Hasil Perkalian Biner 1 dan Biner 2 =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)
     
def binerbag(f, g):
    hasdes = int(int(f, 2) / int(g, 2))
    hasbin = bin(hasdes)[2:]
    os.system("cls")
    print(Fore.CYAN+"==PEMBAGIAN BINER=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Biner 1 Ke Desimal--"+Style.RESET_ALL)
    u1 = 0
    val1 = []
    pangkat1 = []
    hasil1 =  int(f, 2)
    for i in f:
        val1.append(int(i))
    for i in range(0, len(val1)):
        pangkat1.insert(0,int(i))   
    print(Fore.LIGHTBLACK_EX+f"Biner 1 : {f}"+Style.RESET_ALL) 
    for x in pangkat1:
        pingkit1 = pow(2, x)
        print(f"(2^{x}) x {val1[u1]}\t=",Fore.GREEN+f"{pingkit1*val1[u1]}"+Style.RESET_ALL)
        u1 += 1
    print("-----------------------+")
    print(f"Desimal Biner 1 =",Fore.GREEN+f"{hasil1}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Biner 2 Ke Desimal--"+Style.RESET_ALL)
    u2 = 0
    val2 = []
    pangkat2 = []
    hasil2 =  int(g, 2)
    for i in g:
        val2.append(int(i))
    for i in range(0, len(val2)):
        pangkat2.insert(0,int(i))   
    print(Fore.LIGHTBLACK_EX+f"Biner 2 : {g}"+Style.RESET_ALL) 
    for x in pangkat2:
        pingkit1 = pow(2, x)
        print(f"(2^{x}) x {val2[u2]}\t=",Fore.GREEN+f"{pingkit1*val2[u2]}"+Style.RESET_ALL)
        u2 += 1
    print("-----------------------+")
    print(f"Desimal Biner 2 =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL)  

    print(Fore.LIGHTBLUE_EX+"\n--Bagikan Desimal Biner 1 Dan Biner 2--"+Style.RESET_ALL)
    print(Fore.GREEN+f"{hasil1}"+Style.RESET_ALL,":",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hasdes}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Hasil Pembagian Ke Biner--"+Style.RESET_ALL)
    while hasdes > 0:
        hitung = hasdes/2
        if hasdes%2 == 0:
            if hasdes >= 1000:
                print(f"{hasdes} : 2    = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
                print(f"{hasdes} : 2     = {int(hitung)} sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
                print(f"{hasdes} : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
                print(f"{hasdes}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung < 10:
                print(f"{hasdes}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
            elif hasdes < 10:
                print(f"{hasdes}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"0"+Style.RESET_ALL)
        elif hasdes%2 == 1:
            hitung -= 0.5
            if hasdes >= 1000:
                print(f"{hasdes} : 2   = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
                print(f"{hasdes} : 2     = {int(hitung)} sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
                print(f"{hasdes} : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
                print(f"{hasdes}  : 2     = {int(hitung)}  sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes >= 10 and hasdes < 100 and hitung < 10:
                print(f"{hasdes}  : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
            elif hasdes < 10:
                print(f"{hasdes}   : 2     = {int(hitung)}   sisa",Fore.GREEN+"1"+Style.RESET_ALL)
        hasdes = int(hitung)
    print(f"Hasil Pembagian Biner 1 dan Biner 2 =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)


# Operasi Oktal
def oktaljum(d, g):
    okt1 = []
    okt2 = []
    simpan = 0
    hasdes = int(d, 8) + int(g, 8)
    hasbin = oct(hasdes)[2:]
    for i in d:
        okt1.insert(0, int(i))
    for i in g:
        okt2.insert(0, int(i))
    os.system("cls")
    print(Fore.CYAN+"==PENJUMLAHAN OKTAL=="+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Oktal 1 : {d}"+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Oktal 2 : {g}"+Style.RESET_ALL)
    for x in range(0, len(okt1)):
        if simpan == 0:
            if x+1 <= len(okt2): 
                if okt1[x] + okt2[x] <= 7:
                    simpan = 0
                    print(f"{okt1[x]} + {okt2[x]}\t\t=",Fore.GREEN+f"{okt1[x]+okt2[x]}"+Style.RESET_ALL)
                elif okt1[x] + okt2[x] > 7:
                    simpan = 1
                    print(f"{okt1[x]} + {okt2[x]}\t\t= {okt1[x]+okt2[x]} - 8 =",Fore.GREEN+f"{okt1[x]+okt2[x]-8}"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
            elif x+1 > len(okt2): 
                 print(f"{okt1[x]}\t\t=",Fore.GREEN+f"{okt1[x]}"+Style.RESET_ALL)
        elif simpan == 1:
            if x+1 <= len(okt2): 
                if okt1[x] + okt2[x] + 1 <= 7:
                    simpan = 0
                    print(f"{okt1[x]} + {okt2[x]} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{okt1[x]+okt2[x]+1}"+Style.RESET_ALL)
                elif okt1[x] + okt2[x] + 1 > 7:
                    simpan = 1
                    print(f"{okt1[x]} + {okt2[x]} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t= {okt1[x]+okt2[x]+1} - 8 =",Fore.GREEN+f"{okt1[x]+okt2[x]-7}"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
            elif x+1 > len(okt2): 
                if okt1[x] + 1 <= 7:
                    simpan = 0    
                    print(f"{okt1[x]} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t\t=",Fore.GREEN+f"{okt1[x]+1}"+Style.RESET_ALL)
                elif okt1[x] + 1 > 7:
                    simpan = 1
                    print(f"{okt1[x]} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t\t= {okt1[x]+1} - 8 =",Fore.GREEN+"0"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)

    if simpan == 0:
        print(f"Total Penjumlahan Oktal =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)
    if simpan == 1:
        print(Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t\t=",Fore.GREEN+"1"+Style.RESET_ALL)
        print(f"Total Penjumlahan Oktal =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)

def oktalkur(d, g):
    okt1 = []
    okt2 = []
    simpan = 0
    hasdes = int(d, 8) - int(g, 8)
    hasbin = oct(hasdes)[2:]
    for i in d:
        okt1.insert(0, int(i))
    for i in g:
        okt2.insert(0, int(i))
    os.system("cls")
    print(Fore.CYAN+"==PENGURANGAN OKTAL=="+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Oktal 1 : {d}"+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Oktal 2 : {g}"+Style.RESET_ALL)
    for x in range(0, len(okt1)):
        if simpan == 0:
            if x+1 <= len(okt2): 
                if okt1[x] - okt2[x] >= 0:
                    simpan = 0
                    print(f"{okt1[x]} - {okt2[x]}\t\t=",Fore.GREEN+f"{okt1[x]-okt2[x]}"+Style.RESET_ALL)
                elif okt1[x] - okt2[x] < 0:
                    simpan = 1
                    print(f"{okt1[x]} - {okt2[x]}\t\t= {okt1[x]} + (8-{okt2[x]}) =",Fore.GREEN+f"{okt1[x]+(8-okt2[x])}"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
            elif x+1 > len(okt2): 
                 print(f"{okt1[x]}\t\t=",Fore.GREEN+f"{okt1[x]}"+Style.RESET_ALL)
        elif simpan == 1:
            if x+1 <= len(okt2): 
                if okt1[x] - okt2[x] - 1 >= 0:
                    simpan = 0
                    print(f"{okt1[x]} - {okt2[x]} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{okt1[x]-okt2[x]-1}"+Style.RESET_ALL)
                elif okt1[x] - okt2[x] - 1 < 0:
                    simpan = 1
                    print(f"{okt1[x]} - {okt2[x]} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t= {okt1[x]} + (8-{okt2[x]}) -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"=",Fore.GREEN+f"{okt1[x]+(8-okt2[x])-1}"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
            elif x+1 > len(okt2): 
                 print(f"{okt1[x]} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t\t=",Fore.GREEN+f"{okt1[x]-1}"+Style.RESET_ALL)
    print(f"Total Pengurangan Oktal =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)

def oktalkal(d, g):
    okt1 = []
    okt2 = []
    kalian = []
    hasdes = int(d, 8) * int(g, 8)
    hasbin = oct(hasdes)[2:]
    for i in d:
        okt1.insert(0, int(i))
    for i in g:
        okt2.insert(0, int(i))
    os.system("cls")
    print(Fore.CYAN+"==PERKALIAN OKTAL=="+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Oktal 1 : {d}"+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Oktal 2 : {g}"+Style.RESET_ALL)
    for x in range(0, len(okt2)):
        print(Fore.LIGHTBLUE_EX+f"\nPengali : {okt2[x]}"+Style.RESET_ALL)
        smtr = ''
        save = 0
        for w in range(0, len(okt1)):
            if save == 0:
                if okt1[w] * okt2[x] > 7:
                    print(f"{okt1[w]} x {okt2[x]}\t= {okt1[w]*okt2[x]} : 8 =",Fore.LIGHTMAGENTA_EX+f"{int(okt1[w]*okt2[x]/8)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{okt1[w]*okt2[x]%8}"+Style.RESET_ALL)
                    smtr = str(okt1[w]*okt2[x]%8) + smtr
                    save = okt1[w] * okt2[x] / 8
                elif okt1[w] * okt2[x] <= 7:
                    print(f"{okt1[w]} x {okt2[x]}\t=",Fore.GREEN+f"{okt1[w]*okt2[x]}"+Style.RESET_ALL)
                    smtr = str(okt1[w]*okt2[x]) + smtr
            else:
                if okt1[w] * okt2[x] + int(save) > 7:
                    print(f"{okt1[w]} x {okt2[x]}\t= ({okt1[w]*okt2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL+") : 8 =",Fore.LIGHTMAGENTA_EX+f"{int((okt1[w]*okt2[x]+int(save))/8)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{(okt1[w]*okt2[x]+int(save))%8}"+Style.RESET_ALL)
                    smtr = str((okt1[w]*okt2[x]+int(save))%8) + smtr
                    save = (okt1[w]*okt2[x]+int(save))/8
                elif okt1[w] * okt2[x] + int(save) <= 7:
                    print(f"{okt1[w]} x {okt2[x]}\t= {okt1[w]*okt2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"=",Fore.GREEN+f"{okt1[w]*okt2[x]+int(save)}"+Style.RESET_ALL) 
                    smtr = str(okt1[w]*okt2[x]%8) + smtr
                    save = 0
        if int(save) > 0:
            print(Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{int(save)}"+Style.RESET_ALL)
            smtr = str(int(save)) + smtr
        print(f"Total Perkalian {x+1} =",Fore.GREEN+f"{smtr}"+Style.RESET_ALL)
        kalian.append(int(smtr))
    print(Fore.LIGHTBLUE_EX+"\n--Tambahkan Semua Perkalian--"+Style.RESET_ALL)
    o = 0
    p = len(kalian)
    for t in range(len(kalian)-1, -1, -1):
        if o > 0 and len(str(kalian[o])) < len(str(kalian[o-1])):
            spas = ' ' * (t)
            print(f"\t  {spas}{kalian[o]}")
            o += 1
        elif o > 0 and len(str(kalian[o])) > len(str(kalian[o-1])):
            spas = ' ' * (t)
            print(f"\t{spas}{kalian[o]}")
            o += 1
        elif o > 0 and len(str(kalian[o])) == len(str(kalian[o-1])):
            spas = ' ' * (t)
            print(f"\t  {spas}{kalian[o]}")
            o += 1
        else:
            spas = ' ' * (t)
            print(f"\t {spas}{kalian[o]}")
            o += 1
    strip = '-' * (p)
    print(f"\t----{strip}+")
    print(f"\t",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)
    print(f"Total Perkalian Oktal =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)

def oktalbag(d, g):
    hasdes = int(int(d, 8) / int(g, 8))
    hasbin = oct(hasdes)[2:]
    os.system("cls")
    print(Fore.CYAN+"==PEMBAGIAN OKTAL=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Oktal 1 Ke Desimal--"+Style.RESET_ALL)
    u1 = 0
    val1 = []
    pangkat1 = []
    hasil1 =  int(d, 8)
    for i in d:
        val1.append(int(i))
    for i in range(0, len(val1)):
        pangkat1.insert(0,int(i))
    print(Fore.LIGHTBLACK_EX+f"Oktal 1 : {d}"+Style.RESET_ALL)
    for x in pangkat1:
        pingkit = pow(8, x)
        print(f"(8^{x}) x {val1[u1]}\t=",Fore.GREEN+f"{pingkit*val1[u1]}"+Style.RESET_ALL)
        u1 += 1
    print("-----------------------+")
    print(f"Desimal Oktal 1 =",Fore.GREEN+f"{hasil1}"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"\n--Ubah Oktal 2 Ke Desimal--"+Style.RESET_ALL)
    u2 = 0
    val2 = []
    pangkat2 = []
    hasil2 =  int(g, 8)
    for i in g:
        val2.append(int(i))
    for i in range(0, len(val2)):
        pangkat2.insert(0,int(i))
    print(Fore.LIGHTBLACK_EX+f"Oktal 2 : {g}"+Style.RESET_ALL)
    for x in pangkat2:
        pingkit = pow(8, x)
        print(f"(8^{x}) x {val2[u2]}\t=",Fore.GREEN+f"{pingkit*val2[u2]}"+Style.RESET_ALL)
        u2 += 1
    print("-----------------------+")
    print(f"Desimal Oktal 2 =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"\n--Bagikan Desimal Oktal 1 Dan Oktal 2--"+Style.RESET_ALL)
    print(Fore.GREEN+f"{hasil1}"+Style.RESET_ALL,":",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hasdes}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Hasil Pembagian Ke Oktal--"+Style.RESET_ALL)
    while hasdes > 0:
        hitung = hasdes/8
        if hasdes >= 1000:
            print(f"{hasdes} : 8    = {int(hitung)} sisa",Fore.GREEN+f"{hasdes%8}"+Style.RESET_ALL)
        elif hasdes >= 100 and hasdes < 1000 and hitung >= 100:
            print(f"{hasdes} : 8     = {int(hitung)} sisa",Fore.GREEN+f"{hasdes%8}"+Style.RESET_ALL)
        elif hasdes >= 100 and hasdes < 1000 and hitung < 100:
            print(f"{hasdes} : 8     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%8}"+Style.RESET_ALL)
        elif hasdes >= 10 and hasdes < 100 and hitung >= 10:
            print(f"{hasdes}  : 8     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%8}"+Style.RESET_ALL)
        elif hasdes >= 10 and hasdes < 100 and hitung < 10:
            print(f"{hasdes}  : 8     = {int(hitung)}   sisa",Fore.GREEN+f"{hasdes%8}"+Style.RESET_ALL)
        elif hasdes < 10:
            print(f"{hasdes}   : 8     = {int(hitung)}   sisa",Fore.GREEN+f"{hasdes%8}"+Style.RESET_ALL)
        hasdes = int(hitung)
    print(f"Hasil Pembagian Oktal 1 dan Oktal 2 =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)


# Operasi Heksadesimal
def heksajum(d, g):
    hex1 = []
    hex2 = []
    hur1 = []
    hur2 = []
    simpan = 0
    hasdes = int(d, 16) + int(g, 16)
    hasbin = hex(hasdes)[2:]
    for i in d:
        hur1.insert(0, i)
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        hex1.insert(0, int(i))
    for i in g:
        hur2.insert(0, i)
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        hex2.insert(0, int(i))
    os.system("cls")
    print(Fore.CYAN+"==PENJUMLAHAN HEKSA=="+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Heksa 1 : {d}"+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Heksa 2 : {g}"+Style.RESET_ALL)
    for x in range(0, len(hex1)):
        if simpan == 0:
            if x+1 <= len(hex2): 
                if hex1[x] >= 10 and hex2[x] < 10: S = f"({hur1[x]})"; H = ''
                elif hex1[x] < 10 and hex2[x] >= 10: S = ''; H = f"({hur2[x]})"
                elif hex1[x] >= 10 and hex2[x] >= 10: S = f"({hur1[x]})"; H = f"({hur2[x]})"
                elif hex1[x] < 10 and hex2[x] < 10: S = ''; H = ''
                if hex1[x] + hex2[x] <= 15:
                    simpan = 0
                    jumhex = hex1[x] + hex2[x]
                    if jumhex >= 10:
                        if jumhex== 10: jumhex= 'A'
                        elif jumhex== 11: jumhex= 'B'
                        elif jumhex== 12: jumhex= 'C'
                        elif jumhex== 13: jumhex= 'D'
                        elif jumhex== 14: jumhex= 'E'
                        elif jumhex== 15: jumhex= 'F'
                        print(f"{hex1[x]}{S} + {hex2[x]}{H}\t=",Fore.GREEN+f"{hex1[x]+hex2[x]}({jumhex})"+Style.RESET_ALL)
                    elif jumhex < 10:
                        print(f"{hex1[x]}{S} + {hex2[x]}{H}\t=",Fore.GREEN+f"{hex1[x]+hex2[x]}"+Style.RESET_ALL)
                elif hex1[x] + hex2[x] > 15:
                    simpan = 1
                    jumhex = hex1[x] + hex2[x] - 16
                    if jumhex >= 10:
                        if jumhex== 10: jumhex= 'A'
                        elif jumhex== 11: jumhex= 'B'
                        elif jumhex== 12: jumhex= 'C'
                        elif jumhex== 13: jumhex= 'D'
                        elif jumhex== 14: jumhex= 'E'
                        elif jumhex== 15: jumhex= 'F'
                        print(f"{hex1[x]}{S} + {hex2[x]}{H}\t= {hex1[x]+hex2[x]} - 16 =",Fore.GREEN+f"{hex1[x]+hex2[x]-16}({jumhex})",Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
                    elif jumhex < 10:
                        print(f"{hex1[x]}{S} + {hex2[x]}{H}\t= {hex1[x]+hex2[x]} - 16 =",Fore.GREEN+f"{hex1[x]+hex2[x]-16}"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
            elif x+1 > len(hex2): 
                if hex1[x] >= 10:
                    dek = hex1[x]
                    if dek== 10: dek= 'A'
                    elif dek== 11: dek= 'B'
                    elif dek== 12: dek= 'C'
                    elif dek== 13: dek= 'D'
                    elif dek== 14: dek= 'E'
                    elif dek== 15: dek= 'F'
                    print(f"{hex1[x]}({dek})\t\t=",Fore.GREEN+f"{hex1[x]}({dek})"+Style.RESET_ALL)
                elif hex1[x] < 10:
                    print(f"{hex1[x]}\t\t=",Fore.GREEN+f"{hex1[x]}"+Style.RESET_ALL)
        elif simpan == 1:
            if x+1 <= len(hex2): 
                if hex1[x] >= 10 and hex2[x] < 10: S = f"({hur1[x]})"; H = ''
                elif hex1[x] < 10 and hex2[x] >= 10: S = ''; H = f"({hur2[x]})"
                elif hex1[x] >= 10 and hex2[x] >= 10: S = f"({hur1[x]})"; H = f"({hur2[x]})"
                elif hex1[x] < 10 and hex2[x] < 10: S = ''; H = ''
                if hex1[x] + hex2[x] + 1 <= 15:
                    simpan = 0
                    jumhex = hex1[x] + hex2[x] + 1
                    if jumhex >= 10:
                        if jumhex== 10: jumhex= 'A'
                        elif jumhex== 11: jumhex= 'B'
                        elif jumhex== 12: jumhex= 'C'
                        elif jumhex== 13: jumhex= 'D'
                        elif jumhex== 14: jumhex= 'E'
                        elif jumhex== 15: jumhex= 'F'
                        print(f"{hex1[x]}{S} + {hex2[x]}{H} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{hex1[x]+hex2[x]+1}({jumhex})"+Style.RESET_ALL)
                    elif jumhex < 10:
                        print(f"{hex1[x]}{S} + {hex2[x]}{H} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{hex1[x]+hex2[x]+1}"+Style.RESET_ALL)
                elif hex1[x] + hex2[x] + 1 > 15:
                    simpan = 1
                    jumhex = hex1[x] + hex2[x] - 15
                    if jumhex >= 10:
                        if jumhex== 10: jumhex= 'A'
                        elif jumhex== 11: jumhex= 'B'
                        elif jumhex== 12: jumhex= 'C'
                        elif jumhex== 13: jumhex= 'D'
                        elif jumhex== 14: jumhex= 'E'
                        elif jumhex== 15: jumhex= 'F'
                        print(f"{hex1[x]}{S} + {hex2[x]}{H} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t= {hex1[x]+hex2[x]+1} - 16 =",Fore.GREEN+f"{hex1[x]+hex2[x]-15}({jumhex})"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
                    elif jumhex < 10:
                        print(f"{hex1[x]}{S} + {hex2[x]}{H} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t= {hex1[x]+hex2[x]+1} - 16 =",Fore.GREEN+f"{hex1[x]+hex2[x]-15}"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
            elif x+1 > len(hex2): 
                if hex1[x] + 1 <= 15:
                    if hex1[x] + 1 >= 10:
                        simpan = 0    
                        dek = hex1[x]
                        if dek== 10: dek= 'A'
                        elif dek== 11: dek= 'B'
                        elif dek== 12: dek= 'C'
                        elif dek== 13: dek= 'D'
                        elif dek== 14: dek= 'E'
                        elif dek== 15: dek= 'F'
                        print(f"{hex1[x]}({dek}) +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{hex1[x]+1}({dek})"+Style.RESET_ALL)
                    elif hex1[x] + 1 < 10:
                        simpan = 0
                        print(f"{hex1[x]} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{hex1[x]+1}"+Style.RESET_ALL)
                elif hex1[x] + 1 > 15:
                    simpan = 1     
                    print(f"{hex1[x]}{S} +",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t= {hex1[x]+1} - 16 =",Fore.GREEN+"0"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
    if simpan == 0:
        print(f"Total Penjumlahan Heksadesimal =",Fore.GREEN+f"{hasbin.upper()}"+Style.RESET_ALL)
    if simpan == 1:
        print(Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t\t=",Fore.GREEN+"1"+Style.RESET_ALL)
        print(f"Total Penjumlahan Heksadesimal =",Fore.GREEN+f"{hasbin.upper()}"+Style.RESET_ALL)

def heksakur(d, g):
    hex1 = []
    hex2 = []
    hur1 = []
    hur2 = []
    simpan = 0
    hasdes = int(d, 16) - int(g, 16)
    hasbin = hex(hasdes)[2:]
    for i in d:
        hur1.insert(0, i)
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        hex1.insert(0, int(i))
    for i in g:
        hur2.insert(0, i)
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        hex2.insert(0, int(i))
    os.system("cls")
    print(Fore.CYAN+"==PENGURANGAN HEKSA=="+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Heksa 1 : {d}"+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Heksa 2 : {g}"+Style.RESET_ALL)
    for x in range(0, len(hex1)):
        if simpan == 0:
            if x+1 <= len(hex2): 
                if hex1[x] >= 10 and hex2[x] < 10: S = f"({hur1[x]})"; H = ''
                elif hex1[x] < 10 and hex2[x] >= 10: S = ''; H = f"({hur2[x]})"
                elif hex1[x] >= 10 and hex2[x] >= 10: S = f"({hur1[x]})"; H = f"({hur2[x]})"
                elif hex1[x] < 10 and hex2[x] < 10: S = ''; H = ''
                if hex1[x] - hex2[x] >= 0:
                    simpan = 0
                    jumhex = hex1[x] - hex2[x]
                    if jumhex >= 10:
                        if jumhex== 10: jumhex= 'A'
                        elif jumhex== 11: jumhex= 'B'
                        elif jumhex== 12: jumhex= 'C'
                        elif jumhex== 13: jumhex= 'D'
                        elif jumhex== 14: jumhex= 'E'
                        elif jumhex== 15: jumhex= 'F'
                        print(f"{hex1[x]}{S} - {hex2[x]}{H}\t=",Fore.GREEN+f"{hex1[x]-hex2[x]}({jumhex})"+Style.RESET_ALL)
                    elif jumhex < 10:
                        print(f"{hex1[x]}{S} - {hex2[x]}{H}\t=",Fore.GREEN+f"{hex1[x]-hex2[x]}"+Style.RESET_ALL)
                elif hex1[x] - hex2[x] < 0:
                    simpan = 1
                    jumhex = hex1[x] + (16 - hex2[x])
                    if jumhex >= 10:
                        if jumhex== 10: jumhex= 'A'
                        elif jumhex== 11: jumhex= 'B'
                        elif jumhex== 12: jumhex= 'C'
                        elif jumhex== 13: jumhex= 'D'
                        elif jumhex== 14: jumhex= 'E'
                        elif jumhex== 15: jumhex= 'F'
                        print(f"{hex1[x]}{S} - {hex2[x]}{H}\t= {hex1[x]} (16-{hex2[x]}) =",Fore.GREEN+f"{hex1[x]+(16-hex2[x])}({jumhex})"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
                    elif jumhex < 10:
                        print(f"{hex1[x]}{S} - {hex2[x]}{H}\t= {hex1[x]} (16-{hex2[x]}) =",Fore.GREEN+f"{hex1[x]+(16-hex2[x])}"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
            elif x+1 > len(hex2): 
                if hex1[x] >= 10:
                    dek = hex1[x]
                    if dek== 10: dek= 'A'
                    elif dek== 11: dek= 'B'
                    elif dek== 12: dek= 'C'
                    elif dek== 13: dek= 'D'
                    elif dek== 14: dek= 'E'
                    elif dek== 15: dek= 'F'
                    print(f"{hex1[x]}({dek})\t\t=",Fore.GREEN+f"{hex1[x]}({dek})"+Style.RESET_ALL)
                elif hex1[x] < 10:
                    print(f"{hex1[x]}\t\t=",Fore.GREEN+f"{hex1[x]}"+Style.RESET_ALL)
        elif simpan == 1:
            if x+1 <= len(hex2): 
                if hex1[x] >= 10 and hex2[x] < 10: S = f"({hur1[x]})"; H = ''
                elif hex1[x] < 10 and hex2[x] >= 10: S = ''; H = f"({hur2[x]})"
                elif hex1[x] >= 10 and hex2[x] >= 10: S = f"({hur1[x]})"; H = f"({hur2[x]})"
                elif hex1[x] < 10 and hex2[x] < 10: S = ''; H = ''
                if hex1[x] - hex2[x] - 1 >= 0:
                    simpan = 0
                    jumhex = hex1[x] - hex2[x] - 1
                    if jumhex >= 10:
                        if jumhex== 10: jumhex= 'A'
                        elif jumhex== 11: jumhex= 'B'
                        elif jumhex== 12: jumhex= 'C'
                        elif jumhex== 13: jumhex= 'D'
                        elif jumhex== 14: jumhex= 'E'
                        elif jumhex== 15: jumhex= 'F'
                        print(f"{hex1[x]}{S} - {hex2[x]}{H} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{hex1[x]-hex2[x]-1}({jumhex})"+Style.RESET_ALL)
                    elif jumhex < 10:
                        print(f"{hex1[x]}{S} - {hex2[x]}{H} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{hex1[x]-hex2[x]-1}"+Style.RESET_ALL)
                elif hex1[x] - hex2[x] - 1 < 0:
                    simpan = 1
                    jumhex = hex1[x] - (16 - hex2[x])
                    if jumhex >= 10:
                        if jumhex== 10: jumhex= 'A'
                        elif jumhex== 11: jumhex= 'B'
                        elif jumhex== 12: jumhex= 'C'
                        elif jumhex== 13: jumhex= 'D'
                        elif jumhex== 14: jumhex= 'E'
                        elif jumhex== 15: jumhex= 'F'
                        print(f"{hex1[x]}{S} - {hex2[x]}{H} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t= {hex1[x]} + (16-{hex2[x]}) -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL,"=",Fore.GREEN+f"{hex1[x]+(16-hex2[x])-1}({jumhex})"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"")
                    elif jumhex < 10:
                        print(f"{hex1[x]}{S} - {hex2[x]}{H} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t= {hex1[x]} + (16-{hex2[x]}) -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL,"=",Fore.GREEN+f"{hex1[x]+(16-hex2[x])-1}"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"")
            elif x+1 > len(hex2): 
                if hex1[x] - 1 >= 0:
                    if hex1[x] - 1 >= 10:
                        simpan = 0    
                        dek = hex1[x]
                        if dek== 10: dek= 'A'
                        elif dek== 11: dek= 'B'
                        elif dek== 12: dek= 'C'
                        elif dek== 13: dek= 'D'
                        elif dek== 14: dek= 'E'
                        elif dek== 15: dek= 'F'
                        print(f"{hex1[x]}({dek}) -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{hex1[x]-1}({dek})"+Style.RESET_ALL)
                    elif hex1[x] - 1 < 10:
                        simpan = 0
                        print(f"{hex1[x]} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t=",Fore.GREEN+f"{hex1[x]-1}"+Style.RESET_ALL)
                elif hex1[x] - 1 < 0:
                    simpan = 1     
                    print(f"{hex1[x]}{S} -",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+f"\t= {hex1[x]} + (16-"+Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+") =",Fore.GREEN+"15"+Style.RESET_ALL,"SIMPAN",Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL)
    if simpan == 0:
        print(f"Total Pengurangan Heksadesimal = {hasbin.upper()}")
    if simpan == 1:
        print(Fore.LIGHTMAGENTA_EX+"1"+Style.RESET_ALL+"\t\t=",Fore.GREEN+"1"+Style.RESET_ALL)
        print(f"Total Pengurangan Heksadesimal =",Fore.GREEN+f"{hasbin.upper()}"+Style.RESET_ALL)

def heksakal(d, g):
    hex1 = []
    hex2 = []
    hur1 = []
    hur2 = []
    kalian = []
    hasdes = int(d, 16) * int(g, 16)
    hasbin = hex(hasdes)[2:]
    for i in d:
        hur1.insert(0, i)
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        hex1.insert(0, int(i))
    for i in g:
        hur2.insert(0, i)
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        hex2.insert(0, int(i))
    os.system("cls")
    print(Fore.CYAN+"==PERKALIAN HEKSA=="+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Heksa 1 : {d}"+Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX+f"Bilangan Heksa 2 : {g}"+Style.RESET_ALL)
    for x in range(0, len(hex2)):
        if hex2[x] >= 10:
            print(Fore.LIGHTBLUE_EX+f"\nPengali : {hex2[x]}({hur2[x]})"+Style.RESET_ALL)
        elif hex2[x] < 10:
            print(Fore.LIGHTBLUE_EX+f"\nPengali : {hex2[x]}"+Style.RESET_ALL)
        smtr = ''
        save = 0
        for w in range(0, len(hex1)):
            if hex1[w] >= 10 and hex2[x] < 10: S = f"({hur1[w]})"; H = ''
            elif hex1[w] < 10 and hex2[x] >= 10: S = ''; H = f"({hur2[x]})"
            elif hex1[w] >= 10 and hex2[x] >= 10: S = f"({hur1[w]})"; H = f"({hur2[x]})"
            elif hex1[w] < 10 and hex2[x] < 10: S = ''; H = ''
            if hex1[w] < 10 and hex2[x] < 10:
                if save == 0:
                    if hex1[w] * hex2[x] > 15:
                        save = hex1[w] * hex2[x] / 16
                        jumhex = hex1[w]*hex2[x]%16
                        if jumhex >= 10:
                            if jumhex== 10: jumhex= 'A'
                            elif jumhex== 11: jumhex= 'B'
                            elif jumhex== 12: jumhex= 'C'
                            elif jumhex== 13: jumhex= 'D'
                            elif jumhex== 14: jumhex= 'E'
                            elif jumhex== 15: jumhex= 'F'
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t\t= {hex1[w]*hex2[x]} : 16 =",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{hex1[w]*hex2[x]%16}({jumhex})"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                        elif jumhex < 10:
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t\t= {hex1[w]*hex2[x]} : 16 =",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{hex1[w]*hex2[x]%16}"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                    elif hex1[w] * hex2[x] <= 15:
                        jumhex = hex1[w] * hex2[x]
                        if jumhex >= 10:
                            if jumhex== 10: jumhex= 'A'
                            elif jumhex== 11: jumhex= 'B'
                            elif jumhex== 12: jumhex= 'C'
                            elif jumhex== 13: jumhex= 'D'
                            elif jumhex== 14: jumhex= 'E'
                            elif jumhex== 15: jumhex= 'F'
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t\t=",Fore.GREEN+f"{hex1[w]*hex2[x]}({jumhex})"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                        elif jumhex < 10:
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t\t=",Fore.GREEN+f"{hex1[w]*hex2[x]}"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                else:
                    if hex1[w] * hex2[x] + int(save) > 15:
                        jumhex = (hex1[w]*hex2[x]+int(save))%16
                        if jumhex >= 10:
                            if jumhex== 10: jumhex= 'A'
                            elif jumhex== 11: jumhex= 'B'
                            elif jumhex== 12: jumhex= 'C'
                            elif jumhex== 13: jumhex= 'D'
                            elif jumhex== 14: jumhex= 'E'
                            elif jumhex== 15: jumhex= 'F'
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t\t= ({hex1[w]*hex2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL+") : 16 =",Fore.LIGHTMAGENTA_EX+f"{int((hex1[w]*hex2[x]+int(save))/16)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{(hex1[w]*hex2[x]+int(save))%16}({jumhex})"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                            save = (hex1[w]*hex2[x]+int(save))/16
                        elif jumhex < 10:
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t\t= ({hex1[w]*hex2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL+") : 16 =",Fore.LIGHTMAGENTA_EX+f"{int((hex1[w]*hex2[x]+int(save))/16)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{(hex1[w]*hex2[x]+int(save))%16}"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                            save = (hex1[w]*hex2[x]+int(save))/16
                    elif hex1[w] * hex2[x] + int(save) <= 15:
                        jumhex = hex1[w] * hex2[x] + int(save)
                        if jumhex >= 10:
                            if jumhex== 10: jumhex= 'A'
                            elif jumhex== 11: jumhex= 'B'
                            elif jumhex== 12: jumhex= 'C'
                            elif jumhex== 13: jumhex= 'D'
                            elif jumhex== 14: jumhex= 'E'
                            elif jumhex== 15: jumhex= 'F'
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t\t= {hex1[w]*hex2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hex1[w]*hex2[x]+int(save)}({jumhex})"+Style.RESET_ALL) 
                            smtr = str(jumhex) + smtr
                            save = 0
                        elif jumhex < 10:
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t\t= {hex1[w]*hex2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hex1[w]*hex2[x]+int(save)}"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                            save = 0
            else:
                if save == 0:
                    if hex1[w] * hex2[x] > 15:
                        save = hex1[w] * hex2[x] / 16
                        jumhex = hex1[w]*hex2[x]%16
                        if jumhex >= 10:
                            if jumhex== 10: jumhex= 'A'
                            elif jumhex== 11: jumhex= 'B'
                            elif jumhex== 12: jumhex= 'C'
                            elif jumhex== 13: jumhex= 'D'
                            elif jumhex== 14: jumhex= 'E'
                            elif jumhex== 15: jumhex= 'F'
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t= {hex1[w]*hex2[x]} : 16 =",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{hex1[w]*hex2[x]%16}({jumhex})"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                        elif jumhex < 10:
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t= {hex1[w]*hex2[x]} : 16 =",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{hex1[w]*hex2[x]%16}"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                    elif hex1[w] * hex2[x] <= 15:
                        jumhex = hex1[w] * hex2[x]
                        if jumhex >= 10:
                            if jumhex== 10: jumhex= 'A'
                            elif jumhex== 11: jumhex= 'B'
                            elif jumhex== 12: jumhex= 'C'
                            elif jumhex== 13: jumhex= 'D'
                            elif jumhex== 14: jumhex= 'E'
                            elif jumhex== 15: jumhex= 'F'
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t=",Fore.GREEN+f"{hex1[w]*hex2[x]}({jumhex})"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                        elif jumhex < 10:
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t=",Fore.GREEN+f"{hex1[w]*hex2[x]}"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                else:
                    if hex1[w] * hex2[x] + int(save) > 15:
                        jumhex = (hex1[w]*hex2[x]+int(save))%16
                        if jumhex >= 10:
                            if jumhex== 10: jumhex= 'A'
                            elif jumhex== 11: jumhex= 'B'
                            elif jumhex== 12: jumhex= 'C'
                            elif jumhex== 13: jumhex= 'D'
                            elif jumhex== 14: jumhex= 'E'
                            elif jumhex== 15: jumhex= 'F'
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t= ({hex1[w]*hex2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL+") : 16 =",Fore.LIGHTMAGENTA_EX+f"{int((hex1[w]*hex2[x]+int(save))/16)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{(hex1[w]*hex2[x]+int(save))%16}({jumhex})"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                            save = (hex1[w]*hex2[x]+int(save))/16
                        elif jumhex < 10:
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t= ({hex1[w]*hex2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL+") : 16 =",Fore.LIGHTMAGENTA_EX+f"{int((hex1[w]*hex2[x]+int(save))/16)}"+Style.RESET_ALL,"Sisa",Fore.GREEN+f"{(hex1[w]*hex2[x]+int(save))%16}"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                            save = (hex1[w]*hex2[x]+int(save))/16
                    elif hex1[w] * hex2[x] + int(save) <= 15:
                        jumhex = hex1[w] * hex2[x] + int(save)
                        if jumhex >= 10:
                            if jumhex== 10: jumhex= 'A'
                            elif jumhex== 11: jumhex= 'B'
                            elif jumhex== 12: jumhex= 'C'
                            elif jumhex== 13: jumhex= 'D'
                            elif jumhex== 14: jumhex= 'E'
                            elif jumhex== 15: jumhex= 'F'
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t= {hex1[w]*hex2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hex1[w]*hex2[x]+int(save)}({jumhex})"+Style.RESET_ALL) 
                            smtr = str(jumhex) + smtr
                            save = 0
                        elif jumhex < 10:
                            print(f"{hex1[w]}{S} x {hex2[x]}{H}\t= {hex1[w]*hex2[x]} +",Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hex1[w]*hex2[x]+int(save)}"+Style.RESET_ALL)
                            smtr = str(jumhex) + smtr
                            save = 0
        if int(save) > 0:
            jumhex = int(save)
            if jumhex >= 10:
                if jumhex== 10: jumhex= 'A'
                elif jumhex== 11: jumhex= 'B'
                elif jumhex== 12: jumhex= 'C'
                elif jumhex== 13: jumhex= 'D'
                elif jumhex== 14: jumhex= 'E'
                elif jumhex== 15: jumhex= 'F'
                print(Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL+"\t\t=",Fore.GREEN+f"{int(save)}({jumhex})"+Style.RESET_ALL)
                smtr = str(jumhex) + smtr
            elif jumhex < 10:
                print(Fore.LIGHTMAGENTA_EX+f"{int(save)}"+Style.RESET_ALL+"\t\t=",Fore.GREEN+f"{int(save)}"+Style.RESET_ALL)
                smtr = str(jumhex) + smtr
        print(f"Total Perkalian {x+1} =",Fore.GREEN+f"{smtr}"+Style.RESET_ALL)
        kalian.append(smtr)
    print(Fore.LIGHTBLUE_EX+"\n--Tambahkan Semua Perkalian--"+Style.RESET_ALL)
    o = 0
    p = len(kalian)
    for t in range(len(kalian)-1, -1, -1):
        if o > 0 and len(str(kalian[o])) < len(str(kalian[o-1])):
            spas = ' ' * (t)
            print(f"\t  {spas}{kalian[o]}")
            o += 1
        elif o > 0 and len(str(kalian[o])) > len(str(kalian[o-1])):
            spas = ' ' * (t)
            print(f"\t{spas}{kalian[o]}")
            o += 1
        elif o > 0 and len(str(kalian[o])) == len(str(kalian[o-1])):
            spas = ' ' * (t)
            print(f"\t {spas}{kalian[o]}")
            o += 1
        else:
            spas = ' ' * (t)
            print(f"\t {spas}{kalian[o]}")
            o += 1
    strip = '-' * (p)
    print(f"\t----{strip}+")
    print(f"\t",Fore.GREEN+f"{hasbin.upper()}"+Style.RESET_ALL)
    print(f"Total Perkalian Heksadesimal =",Fore.GREEN+f"{hasbin.upper()}"+Style.RESET_ALL)

def heksabag(d, g):
    hasdes = int(int(d, 16) / int(g, 16))
    hasbin = hex(hasdes)[2:]
    os.system("cls")
    print(Fore.CYAN+"==PEMBAGIAN HEKSA=="+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"--Ubah Heksa 1 Ke Desimal--"+Style.RESET_ALL)
    u1 = 0
    val1 = []
    pangkat1 = []
    hasil1 =  int(d, 16)
    for i in d:
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        val1.append(int(i))
    for i in range(0, len(val1)):
        pangkat1.insert(0,int(i))
    for x in pangkat1:
        pingkit1 = pow(16, x)
        if val1[u1] >= 10:
            if val1[u1] == 10: valu1 = 'A'
            elif val1[u1] == 11: valu1 = 'B'
            elif val1[u1] == 12: valu1 = 'C'
            elif val1[u1] == 13: valu1 = 'D'
            elif val1[u1] == 14: valu1 = 'E'
            elif val1[u1] == 15: valu1 = 'F'
            print(f"(16^{x}) x {val1[u1]}({valu1})\t=",Fore.GREEN+f"{pingkit1*val1[u1]}"+Style.RESET_ALL)
        else:
            print(f"(16^{x}) x {val1[u1]}\t=",Fore.GREEN+f"{pingkit1*val1[u1]}"+Style.RESET_ALL)
        u1 += 1
    print("-----------------------+")
    print(f"Desimal Heksa 1 =",Fore.GREEN+f"{hasil1}"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"\n--Ubah Heksa 2 Ke Desimal--"+Style.RESET_ALL)
    u2 = 0
    val2 = []
    pangkat2 = []
    hasil2 =  int(g, 16)
    for i in g:
        if i == 'A': i = 10
        elif i == 'B': i = 11
        elif i == 'C': i = 12
        elif i == 'D': i = 13
        elif i == 'E': i = 14
        elif i == 'F': i = 15
        val2.append(int(i))
    for i in range(0, len(val2)):
        pangkat2.insert(0,int(i))
    for x in pangkat2:
        pingkit2 = pow(16, x)
        if val2[u2] >= 10:
            if val2[u2] == 10: valu2 = 'A'
            elif val2[u2] == 11: valu2 = 'B'
            elif val2[u2] == 12: valu2 = 'C'
            elif val2[u2] == 13: valu2 = 'D'
            elif val2[u2] == 14: valu2 = 'E'
            elif val2[u1] == 15: valu2 = 'F'
            print(f"(16^{x}) x {val2[u2]}({valu2})\t=",Fore.GREEN+f"{pingkit2*val2[u2]}"+Style.RESET_ALL)
        else:
            print(f"(16^{x}) x {val2[u2]}\t=",Fore.GREEN+f"{pingkit1*val2[u2]}"+Style.RESET_ALL)
        u2 += 1
    print("-----------------------+")
    print(f"Desimal Heksa 2 =",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"\n--Bagikan Desimal Heksa 1 Dan Heksa 2--"+Style.RESET_ALL)
    print(Fore.GREEN+f"{hasil1}"+Style.RESET_ALL,":",Fore.GREEN+f"{hasil2}"+Style.RESET_ALL,"=",Fore.GREEN+f"{hasdes}"+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"\n--Ubah Hasil Pembagian Ke Heksa--"+Style.RESET_ALL)
    while hasdes> 0:
        hitung = hasdes/16
        if hasdes%16 < 10:
            if hasdes>= 1000:
                print(f"{hasdes} : 16    = {int(hitung)} sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
            elif hasdes>= 100 and hasdes< 1000 and hitung >= 100:
                print(f"{hasdes} : 16     = {int(hitung)} sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
            elif hasdes>= 100 and hasdes< 1000 and hitung < 100:
                print(f"{hasdes} : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
            elif hasdes>= 10 and hasdes< 100 and hitung >= 10:
                print(f"{hasdes}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
            elif hasdes>= 10 and hasdes< 100 and hitung < 10:
                print(f"{hasdes}  : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
            elif hasdes < 10 and int(hitung) > 0:
                print(f"{hasdes}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
            elif hasdes < 10 and hasdes>= 5 and int(hitung) == 0:
                print(f"{hasdes}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
            elif hasdes < 10  and hasdes< 5 and int(hitung) == 0:
                print(f"{hasdes}   : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
        elif hasdes%16 >= 10:
            if hasdes%16 == 10: val = 'A'
            elif hasdes%16 == 11: val = 'B'
            elif hasdes%16 == 12: val = 'C'
            elif hasdes%16 == 13: val = 'D'
            elif hasdes%16 == 14: val = 'E'
            elif hasdes%16 == 15: val = 'F'
            if hasdes>= 1000:
                print(f"{hasdes} : 16    = {int(hitung)} sisa",Fore.GREEN+f"{hasdes%16}({val})"+Style.RESET_ALL)
            elif hasdes>= 100 and hasdes< 1000 and hitung >= 100:
                print(f"{hasdes} : 16     = {int(hitung)} sisa",Fore.GREEN+f"{hasdes%16}({val})"+Style.RESET_ALL)
            elif hasdes>= 100 and hasdes< 1000 and hitung < 100:
                print(f"{hasdes} : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%16}({val})"+Style.RESET_ALL)
            elif hasdes>= 10 and hasdes< 100 and hitung >= 10:
                print(f"{hasdes}  : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%16}({val})"+Style.RESET_ALL)
            elif hasdes>= 10 and hasdes< 100 and hitung < 10:
                print(f"{hasdes}  : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasdes%16}({val})"+Style.RESET_ALL)
            elif hasdes < 10 and int(hitung) > 0:
                print(f"{hasdes}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%16}({val})"+Style.RESET_ALL)
            elif hasdes < 10  and hasdes>= 5 and int(hitung) == 0:
                print(f"{hasdes}   : 16     = {int(hitung)}  sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
            elif hasdes < 10  and hasdes< 5 and int(hitung) == 0:
                print(f"{hasdes}   : 16     = {int(hitung)}   sisa",Fore.GREEN+f"{hasdes%16}"+Style.RESET_ALL)
        hasdes= int(hitung)
    print(f"Hasil Pembagian Heksa 1 dan Heksa 2 =",Fore.GREEN+f"{hasbin}"+Style.RESET_ALL)



# Tampilan
put = 0
while put != 999:
    try:
        pit = 1
        os.system("cls")
        print(Fore.LIGHTBLUE_EX+"===KALKULATOR BILANGAN==="+Style.RESET_ALL)
        print("1. Konversi Desimal Ke Bilangan Lain")
        print("2. Konversi Bilangan Lain Ke Desimal")
        print("3. Konversi Bilangan Lain ke Bilangan Lain")
        print("4. Operasi Bilangan Lain")
        print("999. Keluar")
        print(Fore.LIGHTBLACK_EX+"Note :"+Style.RESET_ALL,Fore.GREEN+"Bilangan Lain (Biner, Oktal, Heksadesimal)"+Style.RESET_ALL)
        put = int(input("Pilih Opsi : "))
    except ValueError:
        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL); time.sleep(1.5)
        continue
    if put not in range(1, 5) and put != 999:
        print(Fore.RED+"Opsi Yang Dimasukkan Salah!!"+Style.RESET_ALL); time.sleep(1.5)
        continue
    elif put == 1:
        while pit != 0 and pit != 999:
            try:
                os.system("cls")
                print(Fore.LIGHTYELLOW_EX+"==KONVERSI DESIMAL=="+Style.RESET_ALL)
                print("1. Desimal -> Biner")
                print("2. Desimal -> Oktal")
                print("3. Desimal -> Heksadesimal")
                print("0. Kembali")
                print("999. Keluar")
                pit = int(input("Pilih Opsi : "))
            except ValueError:
                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL); time.sleep(1.5)
                continue
            if pit not in range(0, 4) and pit != 999:
                print(Fore.RED+"Opsi Yang Dimasukkan Salah!!"+Style.RESET_ALL); time.sleep(1.5)
                continue
            elif pit == 1:
                while True:
                    try:
                        desimal = int(input("Masukkan Angka Desimal : "))
                        os.system("cls")
                        kondesbiner(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                        continue
            elif pit == 2:
                while True:
                    try:
                        desimal = int(input("Masukkan Angka Desimal : "))
                        kondesoktal(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                        continue
            elif pit == 3:
                while True:
                    try:
                        desimal = int(input("Masukkan Angka Desimal : "))
                        os.system("cls")
                        kondesheksa(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                        continue
            elif pit == 0:
                print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(0.5)
                break
            elif pit == 999:
                print(Fore.GREEN+"Keluar Dari Program"+Style.RESET_ALL); time.sleep(1)
                put = 999
                break
    elif put == 2:
        while pit != 0 and pit != 999:
            try:
                os.system("cls")
                print(Fore.LIGHTYELLOW_EX+"==KONVERSI KE DESIMAL=="+Style.RESET_ALL)
                print("1. Biner -> Desimal")
                print("2. Oktal -> Desimal")
                print("3. Heksa -> Desimal")
                print("0. Kembali")
                print("999. Keluar")
                pit = int(input("Pilih Opsi : "))
            except ValueError:
                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL); time.sleep(1.5)
                continue
            if pit not in range(0, 4) and pit != 999:
                print(Fore.RED+"Opsi Yang Dimasukkan Salah!!"+Style.RESET_ALL); time.sleep(1.5)
                continue
            elif pit == 1:
                while True:
                    try:
                        desimal = input("Masukkan Angka Biner : ")
                        konbinerdes(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Biner(1 Atau 0)!!"+Style.RESET_ALL)
                        continue
            elif pit == 2:
                while True:
                    try:
                        desimal = input("Masukkan Angka Oktal : ")
                        konoktaldes(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Oktal(0-7)!!"+Style.RESET_ALL)
                        continue
            elif pit == 3:
                while True:
                    try:
                        desimal = input("Masukkan Bilangan Heksadesimal : ")
                        konheksades(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Heksadesimal(0-F)!!"+Style.RESET_ALL)
                        continue
            elif pit == 0:
                print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(0.5)
                break
            elif pit == 999:
                print(Fore.GREEN+"Keluar Dari Program"+Style.RESET_ALL); time.sleep(1)
                put = 999
                break
    elif put == 3:
        while pit != 0 and pit != 999:
            try:
                os.system("cls")
                print(Fore.LIGHTYELLOW_EX+"==KONVERSI ANTAR BILANGAN=="+Style.RESET_ALL)
                print("1. Biner -> Oktal")
                print("2. Biner -> Heksa")
                print("3. Oktal -> Biner")
                print("4. Oktal -> Heksa")
                print("5. Heksa -> Biner")
                print("6. Heksa -> Oktal")
                print("0. Kembali")
                print("999. Keluar")
                pit = int(input("Pilih Opsi : "))
            except ValueError:
                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL); time.sleep(1.5)
                continue
            if pit not in range(0, 7) and pit != 999:
                print(Fore.RED+"Opsi Yang Dimasukkan Salah!!"+Style.RESET_ALL); time.sleep(1.5)
                continue
            elif pit == 1:
                while True:
                    try:
                        desimal = input("Masukkan Angka Biner : ")
                        konbineroktal(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Biner(1 Atau 0)!!"+Style.RESET_ALL)
                        continue
            elif pit == 2:
                while True:
                    try:
                        desimal = input("Masukkan Angka Biner : ")
                        konbinerheksa(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Biner(1 Atau 0)!!"+Style.RESET_ALL)
                        continue
            elif pit == 3:
                while True:
                    try:
                        desimal = input("Masukkan Angka Oktal : ")
                        konoktalbiner(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Oktal(0-7)!!"+Style.RESET_ALL)
                        continue
            elif pit == 4:
                while True:
                    try:
                        desimal = input("Masukkan Angka Oktal : ")
                        konoktalheksa(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Oktal(0-7)!!"+Style.RESET_ALL)
                        continue
            elif pit == 5:
                while True:
                    try:
                        desimal = input("Masukkan Bilangan Heksadesimal : ")
                        konheksabiner(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Heksadesimal(0-F)!!"+Style.RESET_ALL)
                        continue
            elif pit == 6:
                while True:
                    try:
                        desimal = input("Masukkan Bilangan Heksadesimal : ")
                        konheksaoktal(desimal)
                        while True:
                            try:
                                neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                if neks == 'Y' or neks == 'y':
                                    print("")
                                    break
                                elif neks == 'N' or neks == 'n':
                                    print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                    break
                                else:
                                    print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                continue
                        if neks == 'N' or neks == 'n': break  
                    except:
                        print(Fore.RED+"Input Harus Bilangan Heksadesimal(0-F)!!"+Style.RESET_ALL)
                        continue
            elif pit == 0:
                print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(0.5)
                break
            elif pit == 999:
                print(Fore.GREEN+"Keluar Dari Program"+Style.RESET_ALL); time.sleep(1)
                put = 999
                break
    elif put == 4:
        while pit != 0 and pit != 999:
            try:
                pat = 1
                os.system("cls")
                print(Fore.LIGHTYELLOW_EX+"==OPERASI BILANGAN=="+Style.RESET_ALL)
                print("1. Bilangan Biner")
                print("2. Bilangan Oktal")
                print("3. Bilangan Heksa")
                print("0. Kembali")
                print("999. Keluar")
                pit = int(input("Pilih Opsi : "))
            except ValueError:
                print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL); time.sleep(1.5)
                continue
            if pit not in range(0, 4) and pit != 999:
                print(Fore.RED+"Opsi Yang Dimasukkan Salah!!"+Style.RESET_ALL); time.sleep(1.5)
                continue
            elif pit == 1:
                while pat != 0 and pat != 999:
                    try:
                        os.system("cls")
                        print(Fore.LIGHTYELLOW_EX+"==BILANGAN BINER=="+Style.RESET_ALL)
                        print("1. Pertambahan Biner")
                        print("2. Pengurangan Biner")
                        print("3. Perkalian Biner")
                        print("4. Pembagian Biner")
                        print("0. Kembali")
                        print("999. Keluar")
                        pat = int(input("Pilih Opsi : "))
                    except ValueError:
                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL); time.sleep(1.5)
                        continue
                    if pat not in range(0, 5) and pat != 999:
                        print(Fore.RED+"Opsi Yang Dimasukkan Salah!!"+Style.RESET_ALL); time.sleep(1.5)
                        continue
                    elif pat == 1:
                        while True:
                            try:
                                hit1 = input("Masukkan Bilangan Biner 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Biner 1 : {int(hit1,2)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Biner 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Biner 2 : {int(hit2,2)}"+Style.RESET_ALL)
                                binerjum(hit1,hit2)
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Biner(1 Atau 0)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 2:
                        while True:
                            try:
                                hit1 = input("Masukkan Bilangan Biner 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Biner 1 : {int(hit1,2)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Biner 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Biner 2 : {int(hit2,2)}"+Style.RESET_ALL)
                                binerkur(hit1,hit2)
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Biner(1 Atau 0)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 3:
                        while True:
                            try:
                                hit1 = input("Masukkan Bilangan Biner 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Biner 1 : {int(hit1,2)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Biner 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Biner 2 : {int(hit2,2)}"+Style.RESET_ALL)
                                binerkal(hit1,hit2)
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Biner(1 Atau 0)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 4:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Harus Bisa Dibagi"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Biner 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Biner 1 : {int(hit1,2)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Biner 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Biner 2 : {int(hit2,2)}"+Style.RESET_ALL)
                                if int(hit1,2) % int(hit2,2) == 0:
                                    binerbag(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Tidak Bisa Dibagi!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Biner(1 Atau 0)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 0:
                        print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(0.5)
                        break
                    elif pat == 999:
                        print(Fore.GREEN+"Keluar Dari Program"+Style.RESET_ALL); time.sleep(1)
                        put = 999
                        break
            elif pit == 2:
                while pat != 0 and pat != 999:
                    try:
                        os.system("cls")
                        print(Fore.LIGHTYELLOW_EX+"==BILANGAN OKTAL=="+Style.RESET_ALL)
                        print("1. Pertambahan Oktal")
                        print("2. Pengurangan Oktal")
                        print("3. Perkalian Oktal")
                        print("4. Pembagian Oktal")
                        print("0. Kembali")
                        print("999. Keluar")
                        pat = int(input("Pilih Opsi : "))
                    except ValueError:
                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL); time.sleep(1.5)
                        continue
                    if pat not in range(0, 5) and pat != 999:
                        print(Fore.RED+"Opsi Yang Dimasukkan Salah!!"+Style.RESET_ALL); time.sleep(1.5)
                        continue
                    elif pat == 1:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Pertama Harus Lebih Besar"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Oktal 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Oktal 1 : {int(hit1,8)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Oktal 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Oktal 2 : {int(hit2,8)}"+Style.RESET_ALL)
                                if int(hit1,8) > int(hit2,8):
                                    oktaljum(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Pertama Lebih Kecil!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Oktal(0-7)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 2:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Pertama Harus Lebih Besar"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Oktal 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Oktal 1 : {int(hit1,8)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Oktal 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Oktal 2 : {int(hit2,8)}"+Style.RESET_ALL)
                                if int(hit1,8) > int(hit2,8):
                                    oktalkur(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Pertama Lebih Kecil!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Oktal(0-7)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 3:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Pertama Harus Lebih Besar"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Oktal 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Oktal 1 : {int(hit1,8)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Oktal 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Oktal 2 : {int(hit2,8)}"+Style.RESET_ALL)
                                if len(hit1) == len(hit2):
                                    oktalkal(hit1,hit2)
                                elif int(hit1,8) > int(hit2,8):
                                    oktalkal(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Pertama Lebih Kecil!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Oktal(0-7)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 4:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Harus Bisa Dibagi"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Oktal 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Oktal 1 : {int(hit1,8)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Oktal 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Oktal 2 : {int(hit2,8)}"+Style.RESET_ALL)
                                if int(hit1,8) % int(hit2,8) == 0:
                                    oktalbag(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Tidak Bisa Dibagi!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Oktal(0-7)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 0:
                        print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(0.5)
                        break
                    elif pat == 999:
                        print(Fore.GREEN+"Keluar Dari Program"+Style.RESET_ALL); time.sleep(1)
                        put = 999
                        break
            elif pit == 3:
                while pat != 0 and pat != 999:
                    try:
                        os.system("cls")
                        print(Fore.LIGHTYELLOW_EX+"==BILANGAN HEKSADESIMAL=="+Style.RESET_ALL)
                        print("1. Pertambahan heksa")
                        print("2. Pengurangan heksa")
                        print("3. Perkalian heksa")
                        print("4. Pembagian heksa")
                        print("0. Kembali")
                        print("999. Keluar")
                        pat = int(input("Pilih Opsi : "))
                    except ValueError:
                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL); time.sleep(1.5)
                        continue
                    if pat not in range(0, 5) and pat != 999:
                        print(Fore.RED+"Opsi Yang Dimasukkan Salah!!"+Style.RESET_ALL); time.sleep(1.5)
                        continue
                    elif pat == 1:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Pertama Harus Lebih Besar"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Heksa 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Heksa 1 : {int(hit1,16)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Heksa 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Heksa 2 : {int(hit2,16)}"+Style.RESET_ALL)
                                if int(hit1,16) > int(hit2,16):
                                    heksajum(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Pertama Lebih Kecil!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Heksa(0-F)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 2:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Pertama Harus Lebih Besar"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Heksa 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Heksa 1 : {int(hit1,16)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Heksa 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Heksa 2 : {int(hit2,16)}"+Style.RESET_ALL)
                                if int(hit1,16) > int(hit2,16):
                                    heksakur(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Pertama Lebih Kecil!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Heksa(0-F)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 3:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Pertama Harus Lebih Besar"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Heksa 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Heksa 1 : {int(hit1,16)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Heksa 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Heksa 2 : {int(hit2,16)}"+Style.RESET_ALL)
                                if len(hit1) == len(hit2):
                                    heksakal(hit1,hit2)
                                elif int(hit1,16) > int(hit2,16):
                                    heksakal(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Pertama Lebih Kecil!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Heksa(0-F)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 4:
                        while True:
                            try:
                                print(Fore.LIGHTBLACK_EX+"Note : Bilangan Harus Bisa Dibagi"+Style.RESET_ALL)
                                hit1 = input("Masukkan Bilangan Heksa 1: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Heksa 1 : {int(hit1,16)}"+Style.RESET_ALL)
                                hit2 = input("Masukkan Bilangan Heksa 2: ")
                                print(Fore.LIGHTBLACK_EX+f"Nilai Heksa 2 : {int(hit2,16)}"+Style.RESET_ALL)
                                if int(hit1,16) % int(hit2,16) == 0:
                                    heksabag(hit1,hit2)
                                else:
                                    print(Fore.YELLOW+f"Bilangan Tidak Bisa Dibagi!!"+Style.RESET_ALL)
                                    print("")
                                    continue
                                while True:
                                    try:
                                        neks = str(input("Ingin Mengulangi Operasi?(Y/N) : "))
                                        if neks == 'Y' or neks == 'y':
                                            print("")
                                            break
                                        elif neks == 'N' or neks == 'n':
                                            print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(1.5)
                                            break
                                        else:
                                            print(Fore.RED+"Input Yang Dimasukkan Salah!!"+Style.RESET_ALL)
                                            continue
                                    except ValueError:
                                        print(Fore.RED+"Input Tidak Valid!!"+Style.RESET_ALL)
                                        continue
                                if neks == 'N' or neks == 'n': break  
                            except:
                                print(Fore.RED+"Input Harus Bilangan Heksa(0-F)!!"+Style.RESET_ALL)
                                continue
                    elif pat == 0:
                        print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(0.5)
                        break
                    elif pat == 999:
                        print(Fore.GREEN+"Keluar Dari Program"+Style.RESET_ALL); time.sleep(1)
                        put = 999
                        break
            elif pit == 0:
                print(Fore.LIGHTMAGENTA_EX+"Kembali Ke Menu..."+Style.RESET_ALL); time.sleep(0.5)
                break
            elif pit == 999:
                print(Fore.GREEN+"Keluar Dari Program"+Style.RESET_ALL); time.sleep(1)
                put = 999
                break
    elif put == 999:
        print(Fore.GREEN+"Keluar Dari Program"+Style.RESET_ALL); time.sleep(1)
        break