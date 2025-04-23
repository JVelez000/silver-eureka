N1 = float(input("Enter the first number: "))
N2 = float(input("Enter the second number: "))
N3 = float(input("Enter the third number: "))

if N1 == N2 == N3:
  print("All three numbers are equal")
elif N1 <= N2 and N1 <= N3:
  print(f"The smallest number is: {N1}")
elif N2 <= N1 and N2 <= N3:
  print(f"The smallest number is: {N2}")
else:
  print(f"The smallest number is: {N3}")