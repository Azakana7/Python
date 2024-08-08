from time import sleep
#! Durasi: 03:00:03
def greetings_To_User(Nama):
    print(f"Halo {Nama}!")
    print("Selamat Belajar Python!")

greetings_To_User(input("Siapa Nama Anda >>> "))
sleep(1)
print("=========================")
sleep(1)
greetings_To_User(input("Siapa Nama Palsu Anda >>> ")) #! Dengan Fungsi kita bisa cukup membuat 1 blok koding untuk dipanggil berkali2