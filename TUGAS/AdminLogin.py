from time import sleep
#! Program sederhana untuk login Atmin dengan memanfaatkan index dari Dictionary

user = input("Siapakah Nama Anda: ")
userInputName = user
sleep(0.5)
user_Passwd = input("Masukkan Kata Sandi Anda: ")
user_Input_Passwd = user_Passwd



Admin_Account = {
    "Username": "Divo",
    "adminTruePasswd": "ADMIN#1234"
}

if userInputName == Admin_Account["Username"] and user_Input_Passwd == Admin_Account["adminTruePasswd"]:
    print("Selamat datang di akun anda, Admin!")
else:
    print("Login Gagal!")

sleep(3)
while Admin_Account:
    askUser = input("Sandi anda terlalu lemah, apakah anda ingin menggantinya(Y/N): ")
    if askUser == "Y" or askUser == "y":
        username_New = input("Masukkan Nama Baru Anda: ")
        password_New = input("Masukkan Password baru anda: ")
        
        new_User_Identity = {
            "Username_New": username_New,
            "Password_New": password_New
        }
        print(f"""
        Username Baru Anda: {new_User_Identity['Username_New']}, 
        Password Baru Anda: {new_User_Identity['Password_New']}
        """)
        break
    elif askUser == "N" or askUser == "n":
        break

print("Program Selesai")