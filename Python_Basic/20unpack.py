
#! Durasi: 02:27:05
Numbers = (1, 2, 3, 4)

#! Yang bawah ribet njir 😹😹😹
#? x = Numbers[0] 
#? y = Numbers[1]
#? z = Numbers[2]
#? zz = Numbers[3]
#? print(zz)

#Todo: Nih cara yg EZZZ
x, y, z, zz = Numbers
print(zz)
print("\n")

#! Kalo pengen variabel selain x gausah dibaca tinggal pake

x, _, _, _, = Numbers
print(x)
print("\n")

#! Kalo pengen masukin nilai selain x ke dalam sebuah array tinggal pake:

x, *a = Numbers #? Jadi ntar semua nilai selain x bakalan disimpen ke *a
print(x)
print(a)
print("\n")

#Todo: Kalo variabel nya kebanyakan atau kekurangan nanti gimana bang?
#! Gw: pake nanya, ya Error lah puki
#? x, y = Numbers #! Variabel terlalu sedikit, sementara index nilainya banyak
#? print(x)
#? print("\n")

#! Atau
#? x, y, z, c, b = Numbers #! Variabel kebanyakan, sementara index nilainya lebih dikit
#? print(y)
#? print("\n")

"""
Output Error:

File "d:\Documents\Python_Learning\Python_Basic\20unpack.py", line 32, in <module>
    x, y = Numbers
    ^^^^
ValueError: too many values to unpack (expected 2)


File "d:\Documents\Python_Learning\Python_Basic\20unpack.py", line 37, in <module>
    x, y, z, c, b = Numbers         
    ^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected 5, got 4)


"""