#class (kerangka) NamaClass:
class Cat:
    #_init_= consturtor
    #fungsi yang pertama kali di panggil
    #self = key/kunci khusus yang mengakses internal class
    def __init__(self, color, height):
        #set attribue2 yang ada di self
        self.color = color
        self.height = height
        

#buat objek (objec=k adalah turunan dari class)
garfield = Cat("orange", 10)
persia = Cat("white", 7)
#cek objek dari kelas kucing
print("obj garfield:", garfield)
print("obj garfield:", persia)
#akses atribute dari objek
print(f"garfield berwarna {garfield.color}")
print(f"garfield tinggi {garfield.height}cm")
print(f"persia berwarna {persia.color}")
print(f"persia tinggi {persia.height}cm")
