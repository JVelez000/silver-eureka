age = input("Enter your age: ")

if age.isnumeric():
    age = int(age)
    if 0 <= age <= 120:
        print("This is a valid age.")
    else:
        print("This is an Invalid age.")
else:
    print("Please enter a valid number.")