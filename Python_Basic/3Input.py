# Durasi Materi Video: 25:33
# from string import Template
def tanya():
    nama = input('siapakah nama anda: ')
    Umur = input('berapakah umur anda: ')
    Agama = input('Apa Nama Agamamu: ')
    Data_User = {
            "Nama": nama,
            "Umur": Umur,
            "Agama": Agama
        }
    print(f"Halo {Data_User['Nama']}\n Umur Anda: {Data_User['Umur']} \n Agama Anda: {Data_User['Agama']}")
tanya()