glossary={
    'import': "to get a module or function from another python file",
    'if': 'to use ocnditional statments',
    'for': 'used to loop an iteratable object like list or dictionary'
}

print("Word:\t\tMeaning:\n")
for key,value in glossary.items():
    print("{0}:\t\t{1}".format(key.upper(),value))
