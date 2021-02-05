class Mobil:
    def SetTipe(self,type):
        self._Type=type
    def GetTipe(self):
        return self._tipe
    def SetModel(self,model):
        self._Model=model
    def GetModel(self):
        return self._model
    def SetHarga(self,harga):
        self._Harga=harga
    def GetHarga(self):
        return self._harga
    def SetJumlahJarakTempuh(self,jumlahjaraktempuh):
        self._JumlahJarakTempuh=jumlahjaraktempuh
    def GetJumlahJarakTempuh(self):
        return self._jumlahjaraktempuh
    def SetPemilik(self,pemilik):
        self._Pemilik=pemilik
    def GetPemilik(self):
        return self._pemilik
    def GetHargaSekarang(self):
        return self._Harga- (self._JumlahJarakTempuh*200000)
    
def main():
    MobilSaya=Mobil()
    MobilSaya.SetTipe("Ferari")
    MobilSaya.SetModel(2020)
    MobilSaya.SetHarga(30000000)
    MobilSaya.SetJumlahJarakTempuh(30)
    MobilSaya.SetPemilik("Zidane")
    HargaSekarang=MobilSaya.GetHargaSekarang()
    
    print("New price {}".format(HargaSekarang))

    MobilPapa=Mobil()
    MobilPapa.SetTipe("BMW")
    MobilPapa.SetModel(2010)
    MobilPapa.SetHarga(20000000)
    MobilPapa.SetJumlahJarakTempuh(30)
    MobilPapa.SetPemilik("Papa")
    HargaSekarang=MobilPapa.GetHargaSekarang()
    
    print("New price {}".format(HargaSekarang))
    
    
    
    
if __name__ == "__main__":main()