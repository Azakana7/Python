
#? 
Command = ""

while Command != "exit":
    Command = input("Pilih Operasi: ")

    if Command == "exit":
        break #! Memaksa program untuk berhenti

    if Command != "+" and Command != "-" and Command != "x" and Command != ":":
        print("Perintah tidak dikenali!")
        continue #! Memaksa untuk mengulangi perulangan While    

    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))

    if Command == "+":
        print(a + b)
        break
    elif Command == "-":
        print( a - b)
        break
    elif Command == "x":
        print(a * b)
        break
    elif Command == ":":
        print(a / b)
        break

print("Terima kasih sudah memakai aplikasi saya!")
