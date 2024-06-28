# Durasi Materi: 31:06
Name = input('Masukkan Nama Anda: ')
Year = input('Masukkan Tahun Lahir Anda: ')
currentYear = input('Masukkan Tahun Sekarang: ')
#print(type(Year))
currentYear = int(currentYear)
Year = int(Year)
# print(type(Year))

umurUserSekarang = currentYear - Year
print(f""" 
Hai {Name}  
Umur Kamu Sekarang adalah: {umurUserSekarang} 
dan kamu lahir pada {Year}
 """)

#Cara mengkonversi itu gampang njir, cuman perlu <Tipe Data>(<Nama Variabel>), misal int(Nilai)