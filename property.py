class Property:
    def __init__(self, area, rooms: int, price, adres):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.adres = adres

    def __str__(self):
        return ("\n\nArea: "+self.area+"\nRooms: "+self.rooms+"\nPrice " +
                self.price+"\nAdres: "+self.adres)