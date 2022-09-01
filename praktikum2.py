def ditambah(x,y): #mendeklarasikan fungsi dengan nama ditambah dan parameternya adalah x dan y
    return x + y #mencetak hasil dari x + y

def dikurangi(x,y): #Mendeklarasikan fungsi dengan nama dikurangi dan parameternya adalah x dan y
    return x - y #mencetak hasil dari x - y

def dibagi(x,y): #mendeklarasikan fungsi dengan nama dibagi dan parameternya adalah x dan y
    return x / y #mencetak hasil dari x / y

def dikali(x,y): #mendeklarasikan fungsi dengan nama dikali dan parameternya adalah x dan y
    return x * y #mencetak hasil dari x * y


def kalkulator(): #mendeklarasikan fungsi dengan nama kalkulator
    print("Operasi Matematika : \n 1.Penjumlahan(+) \n 2.Pengurangan (-) \n 3.Pembagian (/) \n 4.Pengalian (*))")
    while True: #perulangan while jika benar
        operasi = input("Pilih operasi yang diinginkan : ") #menginput operasi matematika yang diinginkan
        if operasi == "1" or operasi == "2" or operasi == "3" or operasi == "4":
            x = float(input("Masukkan angka pertama: ")) #menginput angka pertama yang akan dioperasikan, angka bisa berupa koma(,)
            y = float(input("Masukkan angka kedua: ")) #menginput angka kedua yang akan dioperasikan, angka bisa berupa koma(,)
            if operasi == "1" or operasi == "+": #percabangan jika kondisi var. operasi adalah 1 atau +
                print(x, "+", y, "=" , ditambah(x,y)) #maka akan menampilkan nilai x + nilai y = hasil dari fungsi ditambah dengan parameter x dan parameter y
            elif operasi == "2" or operasi == "-": #percabangan jika kondisi var. operasi adalah 2 atau -
                print(x, "-", y, "=" , dikurangi(x,y)) #maka akan menampilkan nilai x - nilai y = hasil dari fungsi dikurangi dengan parameter x dan parameter y
            elif operasi == "3" or operasi == "/": #percabangan jika kondisi var. operasi adalah 3 atau /
                print(x, "/", y, "=" , dibagi(x,y)) #maka akan menampilkan nilai x / nilai y = hasil dari fungsi dibagi dengan parameter x dan parameter y
            elif operasi == "4" or operasi == "*": #percabangan jika kondisi var. operasi adalah 4 atau *
                print(x, "*", y, "=" , dikali(x,y)) #maka akan menampilkan nilai x * nilai y = hasil dari fungsi dikali dengan parameter x dan parameter y
        else: #percabangan selain kondisi percabangan sebelumnya
            print("Error") #maka menampilkan pesan Error
            print("Masukkan operasi matematika yang benar") #menampilkan pesan Masukkan operasi matematika yang benar
            continue #memulai perulangan dari awal
        break #memberhentikan perulangan
kalkulator() #memanggil fungsi kalkulator() untuk dijalankan