def make_profile(model_name, horse_power, *args, **kwargs):
    print ("Car Model:\n\t{}".format(model_name))
    print ("Car Horse Power:\n\t{}".format(str(horse_power)))
    print ("Other Spesifications:")
    for item in args:
        print("\t- %s"%str(item))
    print ("Extras:")
    for key,item in kwargs.items():
        print("\t- {0}: {1}".format(key,item))

make_profile("Mercedes",900,"Panorama View","SUV", color="blue",height="1 Meter")