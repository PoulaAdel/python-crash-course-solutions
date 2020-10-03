def make_sandwich(*hashow):
    # toppings=[]
    # for topping in hashow:
    #     toppings.append(topping.title())
    # print('El hashow bta3k haykon: {}'.format(str(toppings)))

    print("El hashow bta3k haykon:")
    for topping in hashow:
        print ('- {}'.format(str(topping)))

make_sandwich("tuna","cheese")
make_sandwich("mashroum","tuna","gambary","kalemary")