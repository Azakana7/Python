
#! Durasi: 03:52:43
import random

users = ["Agung", "Adit", "Suki"]

batas_bawah = 0
batas_atas = len(users) - 1
random_int = random.randint(batas_bawah, batas_atas)
winner = users[random_int]
print(winner)

#! for i in range(5):
#!     rndm = random.randint(batas_bawah, batas_atas)
#!     print(rndm)