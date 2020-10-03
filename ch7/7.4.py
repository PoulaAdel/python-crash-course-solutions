toppings=[]

topping=input("Enter Topping (type 'quit' to stop adding): ")
while topping!="quit":
    toppings.append(topping.title())
    topping=input("Enter Topping (type 'quit' to stop adding): ")

print("Making your pizza with toppings {}".format(str(toppings)))