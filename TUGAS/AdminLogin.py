
#! Program sederhana untuk login Atmin dengan memanfaatkan index dari Dictionary

user = input("Siapakah Nama Anda: ")
userInputName = user

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