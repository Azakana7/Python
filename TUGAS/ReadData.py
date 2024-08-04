readUserData = open("TUGAS/insert.txt", "r")

print(readUserData.readable()) 

#! array = readUserData.read()    ==== MEMANGGIL BARIS PER BARIS MENGGUNAKAN ARRAY
#! print(array)  ==== MEMANGGIL BARIS PER BARIS MENGGUNAKAN ARRAY

index = 1
array = readUserData.read()
for user in array:
    print(f"{index} - {user}")
    index += 1

# readUserData.close()






#todo: CATATAN PENTING: 
#! r artinya read (Membaca data)
#! w artinya write (Menulis data)
#! a artinya Append (menambah data)
#! r+ artinya bisa baca & nulis 
#todo: PENUTUP CATATAN 
