
#! Durasi: 02:40:07
user_Input = input("Masukkan Angka Anda: ")


Numbers = {
    "1": "satu",
    "2": "dua",
    "3": "tiga",
    "4": "empat",
    "5": "lima",
    "6": "enam",
    "7": "tujuh",
    "8": "delapan",
    "9": "sembilan"
    
}

output = ""

for n in user_Input:
    terbilang = Numbers.get(n, "Invalid")

    output = output + terbilang + " "

print(output)