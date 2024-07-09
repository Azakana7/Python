import random
import os
#! coba2 doang

trying = 0
max_Try = 3
realNumber = random.randint(1,10)

#userInput = int(input("Masukkan angka dari (1-9) : "))
while trying <= max_Try:
    userInput = int(input("Masukkan angka dari (1-10) : "))
    trying += 1
    if userInput == realNumber:
        print("Benar!")
        break
    elif trying > max_Try:
        print(f"Anda sudah mencapai batas, angka yang benar adalah {realNumber}")
    else:
        print("Salah!")
