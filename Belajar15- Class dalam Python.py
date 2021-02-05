class User:
    def SetUserName(self,userName):
        self._UserName=userName
    def GetUserName(self):
        return self._UserName

def main():
    u1=User()
    u1.SetUserName("Zidane")
    print(u1.GetUserName())
    
if __name__ == "__main__":main()