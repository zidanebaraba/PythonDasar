class Operations:
    def tambah(self,n1,n2):
        return n1+n2
    #INHERITANCE PEMBAGIAN
    def bagi(self,n1,n2):
        return n1/n2

class MultiOperation(Operations):
    def kali(self,n1,n2):
        return n1*n2
    #OVERIDE PERTAMBAHAN
    def tambah(self,n1,n2):
        return (n1+n2)*2
    
def main():
    muOp=MultiOperation()
    print("Perkalian = {}".format(muOp.kali(15,7)))
    print("Perkalian = {}".format(muOp.tambah(15,7)))
    print("Perkalian = {}".format(muOp.bagi(15,7)))
    
if __name__ == "__main__":
    main()