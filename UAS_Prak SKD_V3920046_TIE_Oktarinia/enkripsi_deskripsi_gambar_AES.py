# import library
import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES #import kriptografi AES


# mengambil nilai key
def getKey(keysize):
    key = os.urandom(keysize)
    return key

# mengambil unukran dari blok yang akan digunakan
def getIV(blocksize):
    iv = os.urandom(blocksize)
    return iv

# fungsi untuk enkripsi gambar
def encrypt_image(filename, key, iv):
    BLOCKSIZE = 16 # akan digunakan ukuran blok sepanjang 16
    encrypted_filename = "encrypted_" + filename # inisialisasi file gambar ketika berhasil di enkripsi

    with open(filename, "rb") as file1: # membuka file gambar 
        data = file1.read() # file gambar yang diinputkan tadi akan dibaca dengan variable data sebagai pembacanya

        # program untuk enkripsi gambar dengan AES
        cipher = AES.new(key, AES.MODE_CBC, iv) # pada chiper akan melakukan method dari proses AES dengan key dan blocksize yang telah ditentukan
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE)) # merupakan proses enkripsi yang digunakan chipertext dan data/file gambar tadi

        with open(encrypted_filename, "wb") as file2: # membuka file encrypted_filename tadi sebagai file 2
            file2.write(ciphertext) # kemudian file ke 2 akan dituliskan ciphertext
    return encrypted_filename

# tahap dekripsi sama seperti enkripsi hanya saja berbeda pada proses dekripsi dari file gambar tersebut
def decrypt_image(filename, key, iv):
    BLOCKSIZE = 16
    decrypted_filename = "decrypted_" + filename

    with open(filename, "rb") as file1:
        data = file1.read()

        cipher2 = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher2.decrypt(data), BLOCKSIZE) # merupakan proses dekripsi yang digunakan chiper2 dan data/file gambar tadi

        with open(decrypted_filename, "wb") as file2:
            file2.write(decrypted_data)

    return decrypted_filename


KEYSIZE = 16 # key yang digunakan
BLOCKSIZE = 16 # panjang blok 
filename = "jin.PNG" # file gambar yang ingin dienkripsi

key = getKey(KEYSIZE) # variable key mendenifisikan untuk pengambilan dari nilai variable KEYSIZE
iv = getIV(BLOCKSIZE) # iv key mendenifisikan untuk pengambilan dari nilai variable BLOCKSIZE

encrypted_filename = encrypt_image(filename, key, iv) 
# variable encrypted_filename akan menampung perintah encrypt_image yang didalamnya terdapat nilai dari
# filename, key, dan iv (block size)
decrypted_filename = decrypt_image(encrypted_filename, key, iv)
# variable encrypted_filename akan menampung perintah decrypted_image yang didalamnya terdapat nilai dari
# filename, key, dan iv (block size)