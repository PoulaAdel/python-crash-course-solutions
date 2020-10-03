names=['eric','mona','mary']
for target_list in names:
    print("Hello my dear friend: {}, Let's have dinner tonight!".format(target_list.title()))
print("\n{} can't make it, she won't come!".format(names[1]))
names.remove('mona')
# or names.pop(1)
names.append('samy')
# or names.insert(1,'hany')
for target_list in names:
    print("Hello my dear friend: {}, Let's have dinner tonight!".format(target_list.title()))

print("\nSorry Fellas, I can only invite 2 people to dinner!")
for target_list in names:
    print("Hello my dear friend: {}, sorry I don't have place for you!".format(target_list.title()))
    names.pop(target_list)
