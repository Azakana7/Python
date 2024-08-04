def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  #! isalpha akan mengecek apakah karakter adalah huruf
            shift_amount = shift % 26  #! memastikan pergeseran antara 0 dan 25
            if char.islower():  #! jika huruf kecil
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():  #! Jika huruf besar
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char  
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

#? User memasukkan input
plaintext = input('Masukkan Huruf: ')
shift = int(input('Berapa kali anda ingin mengubahnya: '))

encrypted_text = caesar_encrypt(plaintext, shift)
print(f"Teks terenkripsi: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, shift)
print(f"Teks terdekripsi: {decrypted_text}")
