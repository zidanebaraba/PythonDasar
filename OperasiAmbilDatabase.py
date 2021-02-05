from ClassDatabase import DBConnect
    
def main():
    dbConnect=DBConnect()
    while 1:
        IndexOp=int(input("1- Add\n2- List Admin\n3- Hapus Record\n4- Update Umur\n0- Exit\nMasukan pilihan anda : "))
        if(IndexOp==0):
            break;
        if(IndexOp==1):
            Name=input("Masukan Nama: ")
            Age =int(input("Masukan Usia: "))
            dbConnect.Add(Name,Age)
        elif(IndexOp==2):
            dbConnect.ListAdmin()
        elif(IndexOp==3):
            ID=int(input("Masukan ID untuk dihapus: "))
            dbConnect.DeleteRecord(ID)
        elif(IndexOp==4):
            ID=int(input("Masukan ID : "))
            Name=input("Masukan Nama: ")
            Age= int(input("Masukan Umur Baru: "))
            dbConnect.UpdateRecord(ID,Name,Age)




if __name__ == "__main__":main()