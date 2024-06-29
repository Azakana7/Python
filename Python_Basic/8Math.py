#Durasi Materi: 01:04:25
#Fungsi untuk menyapa User
def sapaUser():
 Greeting = """============================================
|||SELAMAT DATANG DI KALKULATOR SEDERHANA|||
============================================"""
 print(Greeting)

#Luar Fungsi dari sapaUser
sapaUser()


def userAnswer():
    #Pertanyaan pertama
    X = input('Masukkan Angka Pertama: ')
    X = int(X) 

    # Pertanyaan kedua
    Y = input('Masukkan Angka Kedua: ')
    Y = int(Y)

    # Nanya ke user
    # Ask = input('Apa jenis operasi yang ingin anda Gunakan: ')


    
    def mathOperation():
       #Dibawah ini semuanya adalah fungsi2 yg akan diambil kalo perlu
       def Tambah():
          Plus = X + Y
          print(Plus)
        
        #Luar Fungsi dari Tambah
          Tambah()
    
    
    mathOperation()
userAnswer()
    