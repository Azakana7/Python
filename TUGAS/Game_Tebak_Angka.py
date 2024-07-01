import random
import os 
#! Durasi: 01:39:57

print("""


╔╦╗┌─┐┌┐ ┌─┐┬┌─  ╔═╗┌┐┌┌─┐┬┌─┌─┐
 ║ ├┤ ├┴┐├─┤├┴┐  ╠═╣││││ ┬├┴┐├─┤
 ╩ └─┘└─┘┴ ┴┴ ┴  ╩ ╩┘└┘└─┘┴ ┴┴ ┴
By: Divo Saputra

""")

secret_Number = 7
inputUserNumber = int(input("Dari (1-9), manakah angka yang benar?"))

if inputUserNumber == secret_Number:
  print('Selamat anda benar!')
  
  
elif inputUserNumber != secret_Number:
  masukan1 = int(input("Tolong Masukkan Kembali: "))
  inputUserNumber = masukan1
  if masukan1 == secret_Number:
    print("Selamat anda benar!")
    
    
  elif inputUserNumber != secret_Number:
     lebokan2 = input("Tolong Masukkan Kembali: ")
     lebokan2 = int(lebokan2)
  inputUserNumber = lebokan2
  if lebokan2 == secret_Number:
    print("Selamat anda benar!")
    
  elif inputUserNumber != secret_Number:
     C3 = input("Tolong Masukkan Kembali: ")
     C3 = int(C3)
  inputUserNumber = C3
  if C3 == secret_Number:
    print("Selamat anda benar!")
  else:
    print("Anda salah semua!")

    
  