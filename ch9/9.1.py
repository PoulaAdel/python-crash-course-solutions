class Resturant():
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
    def open_resturant(self):
        print("{0} resturant is open now!".format(self.resturant_name.title()))
    def descripe_resturant(self):
        print("Resturant name: {0}\nResturant type: {1}".format(
            self.resturant_name.title(),
            self.cuisine_type.title()
            )
        )


esmo_a = Resturant("esmo a","halawany")
esmo_a.open_resturant()
esmo_a.descripe_resturant()