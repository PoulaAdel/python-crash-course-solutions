locations = ['aswan', 'cairo', 'hurgada', 'germany', 'usa']

for target_list in locations:
    print("I wanna visit {}!".format(target_list.title()))

print("\n{}".format(str(locations)))
locations.remove('aswan')
print(locations)
locations.pop(1)
print(locations)
locations.append('aswan')
print(locations)
locations.insert(1,'luxor')

print ("\n")
for target_list in locations:
    print("I wanna visit {}!".format(target_list.title()))
