import random

choices = ["rock", "paper", "scissors"]
p, c = 0, 0
while not ((p == 5) or (c == 5)):
    player_choice = input("Enter (rock, paper or scissors): ")
    if player_choice not in choices:
        print("Error!")
        continue
    random_choice = random.choice(choices)
    if player_choice == "rock":
        if random_choice == "paper":
            c += 1
            print(f"You lose!\nYou: {p}\nComputer: {c}")
            if c != 5:
                continue
        elif random_choice == "scissors":
            p += 1
            print(f"You win\nYou: {p}\nComputer: {c}")
            if p != 5:
                continue
        else:
            print(f"Next match!\nYou: {p}\nComputer: {c}")
    if player_choice == "paper":
        if random_choice == "rock":
            c += 1
            print(f"You lose!\nYou: {p}\nComputer: {c}")
            if c != 5:
                continue
        elif random_choice == "scissors":
            p += 1
            print(f"You win\nYou: {p}\nComputer: {c}")
            if p != 5:
                continue
        else:
            print(f"Next match!\nYou: {p}\nComputer: {c}")
    if player_choice == "scissors":
        if random_choice == "rock":
            c += 1
            print(f"You lose!\nYou: {p}\nComputer: {c}")
            if c != 5:
                continue
        elif random_choice == "paper":
            p += 1
            print(f"You win\nYou: {p}\nComputer: {c}")
            if p != 5:
                continue
        else:
            print(f"Next match!\nYou: {p}\nComputer: {c}")
else:
    print(
        f'{"YOU WIN THIS MATCH!\n" if p == 5 else "YOU LOSE THIS MATCH!\n"}You: {p}\nComputer: {c}'
    )
