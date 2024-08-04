
#! DURASI KE: 03:29:57 (Cara menulis file)

user = open("TUGAS/insert2.txt", "r+") 
user.write("Woi - hitam")
user.write("\nWoi - putih")

# #todo: CATATAN:
#! Jika file yang dituju tak ada namun sudah menggunakan mode "w" maka file akan otomatis dibuat
#! jika menggunakan "w" maka seluruh data pada file yg dituju akan dihapus dan diganti dengan yg baru jadi ati2