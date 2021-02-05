class Mobil:
    def __init__(self,type,model,harga,jumlahjaraktempuh,pemilik):
        self._Type=type
        self._Model=model
        self._Harga=harga
        self._JumlahJarakTempuh=jumlahjaraktempuh
        self._Pemilik=pemilik
        
    def GetTipe(self):
        return self._tipe
    def GetModel(self):
        return self._model
    def GetHarga(self):
        return self._harga
    def GetJumlahJarakTempuh(self):
        return self._jumlahjaraktempuh
    def GetPemilik(self):
        return self._pemilik
    def GetHargaSekarang(self):
        return self._Harga- (self._JumlahJarakTempuh*200000)
    
def main():
    MobilSaya=Mobil("Ferari",2020,30000000,30,"Zidane")
    HargaSekarang=MobilSaya.GetHargaSekarang()
    print("New price {}".format(HargaSekarang))

    MobilPapa=Mobil("BMW",2010,20000000,30,"Papa")
    HargaSekarang=MobilPapa.GetHargaSekarang()
    print("New price {}".format(HargaSekarang))
    
    
    
    
if __name__ == "__main__":main()