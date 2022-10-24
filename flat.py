from property import Property

class Flat(Property):
    def __init__(self, area, rooms: int, price, adres, floor):
        super().__init__(area, rooms, price, adres)
        self.floor = floor

    def __str__(self):
        return ("\n\nArea: "+self.area+"\nRooms: "+self.rooms+"\nPrice " +
                self.price+"\nAdres: "+self.adres+"\nFloor: "+self.floor)