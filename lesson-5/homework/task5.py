def is_prime(n):
    if n in [2, 3, 5, 7, 11]:
        return True
    return n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and n % 11 != 0


print(is_prime(271))
