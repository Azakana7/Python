
#! Durasi: 02:18:38
Numbers = [5, 6, 1]
max_number = Numbers[0]

#! Cara paling ribet untuk mencari max number
for Number in Numbers:
    if Number > max_number:
        max_number = Number

print(max_number)
print("\n")

#! Cara termudah untuk mencari max number
Angka = [23, 57, 1000, 50000]
Maksimal = max(Angka)
print(Maksimal)