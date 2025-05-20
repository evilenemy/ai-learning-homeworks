def invest(amount, rate, years=1):
    total = amount
    for i in range(years):
        total = total + total * rate
        print(f"year {i+1}: ${total:.2f}")


invest(100, 0.05, 4)
