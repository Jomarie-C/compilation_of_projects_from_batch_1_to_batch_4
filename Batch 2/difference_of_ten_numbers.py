first_number = float(input("Enter the first number: "))
result = first_number

for i in range(1, 10):
    number = float(input(f"Enter the next number({i} of 9): "))
    result -= number

