def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

# def make_magicians(magicians):
#     while magicians:
#         magician = magicians.pop()
#         print("The Great Magician %s"%magician.title())

def make_magicians(magicians):
    counter=0
    # while magicians: Won't work ! your not deleting any item so that it will be always true!
    while counter<len(magicians):
        magicians[counter] = "The Great Magician %s"%magicians[counter].title()
        print(magicians[counter])
        counter+=1
        

magicians=['chris','robert','izenhime']
#printing magicians
show_magicians(magicians)
#printing magicians with addition without changing the list
make_magicians(magicians[:])
print(str(magicians))
#printing magicians with addition with changing the list
make_magicians(magicians)
print(str(magicians))

