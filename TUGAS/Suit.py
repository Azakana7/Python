import random
from colorama import Fore, Back, Style
#! PROGRAM BATU GUNTING KERTAS SEDERHANA WIRR

text = ("""



                                    @@@@@@@@@                                   
                               @@@@@@@@@@@@@@@@@@@(                             
               %%&&&@       ,@@@@@@@@@@@@@@@@@@@@@@@        &&&&@@              
                %%&&&&@     @@@@@@@@@@@@@@@@@@@@@@@@@     &&&&&&&               
             .#&&&&&&&&&&. .&@@@@@@@@@@@@@@@@@@@@@@@@...@&&&&&&&&&%             
             #########&&&&&#&&@@@@@@@@@@&@@@@@@@@@@@@@#%&&%%###%%%%             
                        ##&#%&&@@@@&%%%%&@@%%@@@@@@@@%###                       
                            %@         @@@%       (@%                           
                            /@%,     *@* (&%,     (@@                           
                            @@@@&#&&&@@   @@@&&@@@@@@@                          
                             (&&&&&@@@     @@@&&&&&&                            
                @@@,    @@@&&#%   @@@@@@@@@@@@@  .%%&&&&@    #@@@               
             %@&&&&&&&&&&&&&%#%%(( @,@,#&,@,@ , #@%%&&&&&&&&&&&&&&&             
              ###&&&&&&&%###  %&&&@@         @@@@@(  #%&&&&&&&&&%%              
                 #%%&%##        %&@@@@&@@@@@@@@@@       #%&&&%%                 
                                  #%&@@@@@@@@%                                  
                                      ..... 
                    By:𝕮𝖞𝖇𝖊𝖗𝕭𝖔𝖞𝖘
      
      List:
      1. Batu
      2. Gunting
      3. Kertas
      4. Exit

""")
print(text)

half_index = len(text) // 2
text_part1 = text[:half_index]
text_part2 = text[half_index:]

# Mewarnai bagian pertama dengan warna merah dan bagian kedua dengan warna default
print(Fore.RED + text_part1 + Fore.WHITE + text_part2 + Style.RESET_ALL)

def mainProgram():
    alat_Main = ["Batu", "Gunting", "Kertas"]
    Computer = random.sample(alat_Main, 1)[0]
    userInput = ""


    while userInput != "4" and userInput != "Exit": 
        userInput = input("Pilihan anda: ")

        #? Antisipasi kondisi tak diinginkan
        if userInput != "1" and userInput != "2" and userInput != "3" and userInput != "4" and userInput != "Exit":
            print("Perintah Invalid!")
            continue


        #! Kondisi pilihan user = 1
        if userInput == "1" and Computer == alat_Main[0]:
            print(f"Anda Seri!, Lawan Anda Mengeluarkan {Computer}")
            break
        elif userInput == "1" and Computer == alat_Main[1]:
            print(f"Anda Menang!, Lawan Anda Mengeluarkan {Computer}")
            break
        elif userInput == "1" and Computer == alat_Main[2]:
            print(f"Anda kalah!, Lawan Anda Mengeluarkan {Computer}")
            break

        #! Kondisi pilihan user = 2
        if userInput == "2" and Computer == alat_Main[0]:
            print(f"Anda Kalah!, Lawan Anda Mengeluarkan {Computer}")
            break
        elif userInput == "2" and Computer == alat_Main[1]:
            print(f"Anda Seri!, Lawan Anda Mengeluarkan {Computer}")
            break
        elif userInput == "2" and Computer == alat_Main[2]:
            print(f"Anda Menang!, Lawan Anda Mengeluarkan {Computer}")
            break

        #! Kondisi pilihan user = 3
        if userInput == "3" and Computer == alat_Main[0]:
            print(f"Anda Menang!, Lawan Anda Mengeluarkan {Computer}")
            break
        elif userInput == "3" and Computer == alat_Main[1]:
            print(f"Anda Kalah!, Lawan Anda Mengeluarkan {Computer}")
            break
        elif userInput == "3" and Computer == alat_Main[2]:
            print(f"Anda Seri!, Lawan Anda Mengeluarkan {Computer}")
            break

        if userInput != "4" or userInput != "Exit":
            break
        
    print("\nTerima kasih telah memainkan Game Saya!")



    

mainProgram()














# if userInput == "4":
#         break

#     while userInput != "1" and userInput != "2" and userInput != "3" :
#         print("Invalid!")
#         continue

#     if userInput == "1" and Computer == alat_Main[1]:
#         print("Anda menang!")
