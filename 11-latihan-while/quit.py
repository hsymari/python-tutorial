loop = 1
while loop == 1:
    respon = input("Masukkan 'quit' untuk keluar => ")
    if respon == 'quit':
        print('Oke Berhasil Keluar!')
        loop = 0
    else:
        print("Kamu mengetikkan %s" % respon)
