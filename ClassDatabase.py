import sqlite3

class DBConnect:
    
    def __init__(self):
        self._db=sqlite3.connect("information.db")
        # Create Database Table
        self._db.row_factory=sqlite3.Row
        self._db.execute("create table if not exists Admin(ID integer primary key autoincrement, Name text, Age int)")
        self._db.commit()
        
    def Add(self,Name,Age):
        self._db.row_factory=sqlite3.Row
        # insert value ke tabel
        self._db.execute("insert into Admin(Name,Age) values(?,?)",(Name,Age))
        self._db.commit()
        
    def ListAdmin(self):
        # Memperlihatkan seluruh data tabel
        cursor=self._db.execute("select * from Admin")
        for row in cursor:
            print("ID:{},Name:{},Age:{}".format(row["ID"],row["Name"],row["Age"]))
            
    def DeleteRecord(self,ID):
        self._db.row_factory=sqlite3.Row
        # menghapus data dari tabel
        self._db.execute("delete from Admin where ID='{}'".format(ID))
        self._db.commit()
        print("Record is deleted")
        
    def UpdateRecord(self,ID,Name,Age):
        self._db.row_factory=sqlite3.Row
        # Mengubah nilai date
        self._db.execute("update Admin set Name=? where ID=?",(Name,ID))
        self._db.execute("update Admin set Age=? where ID=?",(Age,ID))
        self._db.commit()
        print("Record updated")