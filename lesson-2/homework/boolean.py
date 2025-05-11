# 1
print("Not empty" if input("Enter login: ") and input("Enter password: ") else "Empty")

# 2
print("Equal" if input("Enter first integer: ") == input("Enter second integer: ") else "Not equal")

# 3
number = int(input("Enter number: "))
print("Yes" if number % 2 == 0 and number >= 0 else "No")

# 4
print("Different" if len(set([int(input(f"Enter number {i+1}: ")) for i in range(3)])) == 3 else "No")

# 5
print("Same length" if len(input("Enter first sentence: ")) == len(input("Enter second sentence: ")) else "No")

# 6
print("Yes" if int(input("Enter number: ")) % 15 == 0 else "No")

# 7
print("Yes" if sum([int(input("Enter first number: ")), int(input("Enter second number: "))]) > 50 else "No")

# 8
print("Yes" if 10 <= int(input("Enter number: ")) <= 20 else "No")