names = []

while True:
    action = input("Enter a name to add it to the list, type 'list' to see the current list, or type 'leave' to exit the program: ")
    
    if action.lower() == 'leave':
        print("Leaving the program... here is the final result of the list:")
        for name in names:
            print(name)
        break
    
    elif action.lower() == 'list':
        print("Here is the current list of names:")
        for name in names:
            print(name)
    
    else:
        names.append(action)