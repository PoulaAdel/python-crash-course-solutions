def display_message(learned_object):
    print("I've learned %s"%str(learned_object))


stop_flag = True
while stop_flag:
    sub=input("What you've learned today?(enter 'q' to stop): ")
    if sub.lower()=='q':
        stop_flag=False
    else:
        display_message(sub)