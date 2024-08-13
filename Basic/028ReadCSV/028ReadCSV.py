import csv
#! Durasi: 03:35:50
users = open("Basic/028READCSV/Data.CSV", "r")

users_CSV = csv.reader(users,delimiter=",") #! Artinya tiap kolom dipisahkan dengan koma

for row in users_CSV:
    print(f"Name: {row[0]}, username: {row[1]}, role: {row[2]}")

users.close() 

#Todo: 03:41:17 (selalu gunakan with statement untuk membuka sebuah file!)