from django.template.defaultfilters import upper,lower # library django untuk upper dan lower
nama="Muhammad Zidane"
nim=20160801289
print(nama, nim) # Ambil data nama dengan NIM 


DOB=1998
Age=2020-DOB
AgeMessage="Umur anda adalah {} dan lahir pada {}".format(Age,DOB) # Menambahkan variabel kedalam string
print(AgeMessage) # keluaran variable akan masuk kedalam String

Strlen=len(AgeMessage) # Penjabaran jumlah huruf
print(Strlen) # output hasil jumlah huruf
print(upper(AgeMessage)) # Mengubah huruf menjadi capital semua ( Harus import Django)
print(lower(AgeMessage)) # Mengubah huruf menjadi huruf kecil semua ( Harus import Django)