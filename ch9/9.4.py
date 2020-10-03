# from resturant import Resturant
class Resturant():
    def __init__(self,resturant_name,cuisine_type,number_served=0):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    def open_resturant(self):
        print("{0} resturant is open now!".format(self.resturant_name.title()))
    def descripe_resturant(self):
        print("Resturant name: {0}\nResturant type: {1}\nServed Clients: {2}".format(
            self.resturant_name.title(),
            self.cuisine_type.title(),
            str(self.number_served)
            )
        )
    def update_number_served(self,number):
        self.number_served=number

esmo_a = Resturant("esmo a","halawany")
esmo_a.open_resturant()
esmo_a.descripe_resturant()
print("")
esmo_a.number_served = input("Change number served by property: ")
esmo_a.descripe_resturant()
print("")
number_served = input("Change number served by property: ")
esmo_a.update_number_served(int(number_served))
esmo_a.descripe_resturant()