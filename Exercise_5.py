guest_list = [
    "ana", "luis", "sofía",
    "samuel", "tomas", "steven", "stiven", "sara",
    "valeria", "isabella", "camila", "veronica",
    "adara", "miguel", "jorge", "nataly"
]

name = input("Enter your name: ").lower()

if name in guest_list:
    print("You're on the guest list. !you are welcome!")
else:
    print("You are not a on the guest list. !you are not welcome!")
