
#! DURASI KE: 03:29:57 (Cara menulis file)

user = open("Basic/027Data_Read/insert2.txt", "r+") 
user.write("Woi - wireng")
user.write("\nWoi - ijooo")
print(user)

# #todo: CATATAN:
#! Jika file yang dituju tak ada namun sudah menggunakan mode "w" maka file akan otomatis dibuat
#! jika menggunakan "w" maka seluruh data pada file yg dituju akan dihapus dan diganti dengan yg baru jadi ati2