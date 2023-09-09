# user dan password yang ada di sistem
users = ['Budi','Miya','Franco']
passwords = ['123456','panah','jangkar']
# masukkan password dan username
usrname = input("Enter username: ")
pwd = input("Enter password: ")
# check password
if usrname in users:
    pos = users.index(usrname)
    if pwd == passwords[pos]:
        print("Berhasil Masuk!")
    else:
        print("Ups gagal masuk")
else:
    print("Ini tidak dikenal! illegal")
