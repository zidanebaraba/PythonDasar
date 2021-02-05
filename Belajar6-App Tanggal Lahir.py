import datetime
DOB=input("Masukan Tahun Lahir Anda : ")
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(DOB)
print("Umur anda adalah {}".format(Age))