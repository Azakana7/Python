
#! Durasi 03:16:19

level = ""

while True:
    try:
        level = input("Berapakah Level Anda: ")
        level = int(level)
        print(level)
        break

    except ValueError: #? Error bisa di definisikan dengan tipe error yang tersedia di terminal
        print("Yang anda masukkan bukanlah angka!")
        continue



#! Durasi 03:21:02 = General Error

def user_Char():
    try:
        Nama = str(input("Siapakah Nama Anda: "))
        Umur = str(input("Berapakah Umur Anda: "))
        lvl = str(input("Berapakah Level Anda: "))
        print({f"""

        YOUR NAME: {Nama}
        YOUR AGES: {Umur}
        YOUR LEVEL: {lvl}

"""})
    except:          #? (except:) digunakan untuk mengatasi error secara general/semuanya gitu deh
        print("Terjadi Kesalahan!")

user_Char()