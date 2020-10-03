people =[
    {
        'name':'teddy',
        'age':13,
        'location':'hangkok'
    },
    {
        'name':'john',
        'age':21,
        'location':'germany'
    },
    {
        'name':'morad',
        'age':16,
        'location':'egypt'
    }
]

print("name\t\tage\t\tlocation".upper())
for person in people:
    print ("{0}\t\t{1}\t\t{2}".format(\
        person.get('name'),\
        str(person.get('age')),\
        person.get('location').title()))