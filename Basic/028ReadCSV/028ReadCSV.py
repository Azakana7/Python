import csv
#! Durasi: 03:35:50
users = open("Data.CSV" "r")

users_CSV = csv.reader(users,delimiter=",") #! Artinya tiap kolom dipisahkan dengan koma

users.close() 

print(users)
