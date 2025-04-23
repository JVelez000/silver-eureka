N1 = input("Enter the first number: ")
N2 = input("Enter the second number: ")

if N1.isnumeric() and N2.isnumeric():
    N1 = int(N1)
    N2 = int(N2)

    if N1 <= N2:
        user_list = list(range(N1, N2 + 1))
    else:
        user_list = list(range(N2, N1 + 1))

    while True:
        search = input("Enter a number to search in the list, or type 'leave' to leave program : ")
        if search.lower() == 'leave':
            print("Leaving the program...")
            break
        elif search.isnumeric():
            search = int(search)
            if search in user_list:
                print(f"The number {search} is in the list.")
            else:
                print(f"The number {search} is not in the list.")
        else:
            print("Please enter a valid number or 'leave' to quit.")
else:
    print("Please enter valid numbers.")
