base = input("Enter base word: ")

passwords = [
    base + "123",
    base + "@123",
    base + "2024",
    base + "_01",
    base.capitalize() + "123",
    base + "!"
]

print("\nGenerated Passwords:")
for pwd in passwords:
    print(pwd)
