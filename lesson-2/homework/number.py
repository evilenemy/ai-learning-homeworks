# 1
print(f"{float(input("Enter number: ")):.2f}")

# 2
a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
print(max(a, b, c), min(a, b, c))

# 3
km = int(input("Enter kilometer: "))
print(f"{km} km equal to {km*1000} meter and {int(km*1e5)} centimeter")

# 4
a, b = int(input("Enter first number: ")), int(input("Enter second number: "))
x, y = divmod(a, b)
print(x, y)

# 5
temp = float(input("Enter temperature in C: "))
print(f"{(temp * 1.8) + 32:.1f}")

# 6
print(int(input("Enter number: ")) % 10)

# 7
print("Even" if int(input("Enter number: ")) % 2 == 0 else "Odd")