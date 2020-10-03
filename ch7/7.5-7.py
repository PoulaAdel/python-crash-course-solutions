while True:
    age=input("Enter Your Age (enter 'quit' to stop): ")
    if age=='quit'.lower():
        break
    if int(age)<=3:
        print("Your ticket is free!")
    elif int(age)<12:
        print("Your ticket costs 10$")
    else:
        print("Your ticket costs 15$")
