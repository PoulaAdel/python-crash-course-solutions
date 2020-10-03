fav_number = {
    'teddy':1,
    'phill':2,
    'taison':3
}

for key,item in fav_number.items():
    print ("{0} : {1}".format(key,str(item)))

while True:
    again = input("\nWanna add someone else? (Y/N): ")
    if again.upper()=='N':
        break
    name = input("Your Name?: ")
    fav_number[name] = input("Your Favorit number?: ")

print("\nYour new dictionary is: ")
for key,item in fav_number.items():
    print ("{0} : {1}".format(key,str(item)))