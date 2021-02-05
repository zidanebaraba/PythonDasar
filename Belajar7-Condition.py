import datetime
DOB=input("Masukan Tahun Lahir Anda : ")
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(DOB)
if(Age>30):
    print("Anda dewasa dengan umur {}".format(Age))
elif(Age==30 and Age>=20):
    print("Anda mulai dewasa")
else:
    print("Anda masih muda")