class Mobil:
    def __init__(self,**kwargs):
        self._Data=kwargs
        
    def GetTipe(self):
        return self._Data["Tipe"]
    def GetModel(self):
        return self._Data["Model"]
    def GetHarga(self):
        return self._Data["Harga"]
    def GetJumlahJarakTempuh(self):
        return self._Data["JumlahJarakTempuh"]
    def GetPemilik(self):
        return self._Data["Pemilik"]
    def GetHargaSekarang(self):
        return self._Data["Harga"]- (self._Data["JumlahJarakTempuh"]*200000)
    
def main():
    MobilSaya=Mobil(Tipe="Ferari",Model=2020,Harga=30000000,JumlahJarakTempuh=30,Pemilik="Zidane")
    HargaSekarang=MobilSaya.GetHargaSekarang()
    print("New price {}".format(HargaSekarang))

    MobilPapa=Mobil(Tipe="BMW",Model=2010,Harga=20000000,JumlahJarakTempuh=30,Pemilik="Papa")
    HargaSekarang=MobilPapa.GetHargaSekarang()
    print("New price {}".format(HargaSekarang))
    
    
    
    
if __name__ == "__main__":main()