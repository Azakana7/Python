import random

print("""



 
   
   _____                                             _               
  / ____|                                           | |              
 | |  __ _   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                     
  By: Divo Saputra

""")

secret_Number = 5
#secret_Number = (random.randint(1, 10))

inputUserNumber = int(input("Dari (1-9), manakah angka yang benar: "))

while inputUserNumber != secret_Number:
  print("Tebakan salah! Coba lagi..")
  inputUserNumber = int(input("Dari (1-9), manakah angka yang benar: ")) 
print("Selamat anda benar!")