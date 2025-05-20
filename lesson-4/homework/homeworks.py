# 1

# list1 = [1, 1, 2, 3, 4, 2]
# list2 = [1, 3, 4, 5]
# new_list = []

# for i in list1:
#   if i not in list2:
#     new_list.append(i)
# for i in list2:
#   if i not in list1:
#     new_list.append(i)
# print(new_list)

# 2

# try:
#   n = int(input("Enter number: "))
#   for i in range(1, n):
#     print(i**2)
# except ValueError:
#   print("Not a number")
# except Exception as e:
#   print(e)

# 3

# txt = input("Enter string: ")
# new_txt = txt[:3]

# for i in range(3, len(txt), 3):
#   if i == len(txt) - 1:
#     new_txt += txt[i]
#     break
#   if txt[i - 1] == "_":
#     continue
#   new_txt += "_" + txt[i : i + 3]

# print(new_txt)

# 4

# import random

# random_num = random.randint(1, 100)
# i = 1
# while i <= 10:
#   try:
#     num = int(input("Enter number: "))
#     if num == random_num:
#       print(f"You guessed it right! Tryings: {i}")
#       if input("Want to play again?: ") in [
#           "Y",
#           "YES",
#           "y",
#           "ok",
#       ]:
#         i = 1
#         continue
#       break
#     elif num < random_num:
#       print("Too low!")
#       i += 1

#       if i == 11:
#         print(f"Number was {random_num}")
#         if input("You lost. Want to play again?: ") in [
#           "Y",
#           "YES",
#           "y",
#           "ok",
#         ]:
#           i = 1
#           continue
#         else:
#           print("OK!")
#     elif num > random_num:
#       print("Too high!")
#       i += 1
#       if i == 11:
#         print(f"Number was {random_num}")
#       if input("You lost. Want to play again?: ") in [
#           "Y",
#           "YES",
#           "y",
#           "ok",
#         ]:
#           i = 1
#           continue
#       else:
#           print("OK!")
#   except ValueError:
#     print("Your entered value is wrong!")
#   except Exception as e:
#     print(e)

# 5

# password = input("Enter password: ")

# if len(password) < 8:
#     print("Password is too short.")
# elif len([x for x in password if x in "QWERTYUIOPALSKDJFHGZXCVBNM"]) < 1:
#     print("Password must contain an uppercase letter.")
# else:
#     print("Password is strong.")

# 6

# prime = [2, 3, 5, 7, 11]
# for i in range(3, 100, 2):
#     if i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
#         prime.append(i)

# print(prime)
