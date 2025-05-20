try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Enter positive and not 0 value!")
        exit()
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")
except ValueError:
    print("Please enter number!")
except Exception as e:
    print(e)
