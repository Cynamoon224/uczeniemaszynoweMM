from property import Property

class House(Property):
    def __init__(self, area, rooms: int, price, adres, plot: int):
        super().__init__(area, rooms, price, adres)
        self.plot = plot

    def __str__(self):
        return ("\n\nArea: "+self.area+"\nRooms: "+self.rooms+"\nPrice " +
                self.price+"\nAdres: "+self.adres+"\nPlot: "+self.plot)