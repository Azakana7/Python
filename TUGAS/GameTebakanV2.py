import random

print("""



 
   _   _   _   _   _     _   _   _   _   _   _  
  / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ 
 ( G | u | e | s | s ) ( N | u | m | b | e | r )
  \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ 

By: Divo Saputra

""")

secret_Number = (random.randint(1, 10))
inputUserNumber = int(input("Dari (1-9), manakah angka yang benar?"))

while inputUserNumber != secret_Number:
  print("Tebakan salah! Coba lagi..")
  inputUserNumber = int(input("Dari (1-9), manakah angka yang benar?"))
print("Selamat anda benar!")