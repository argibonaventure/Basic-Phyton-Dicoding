class Mobil: #class
    def __init__(self, merek,kecepatan): #constructor
        self.merek = merek # instance attribute 
        self.kecepatan = kecepatan
    


    def tambah_kecepatan(self): #Object Method
        self.kecepatan += 10

    @staticmethod #Static Method
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")

    @classmethod #Class Method
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()



print("=============================================================")

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10
 
 
class MobilSport(Mobil): #Inheritence
    def turbo(self): #
        self.kecepatan += 50

    def tambah_kecepatan(self): # override
        self.kecepatan += 20
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()     # Super
        print("Kecepatan Anda meningkat! Hati-Hati!")