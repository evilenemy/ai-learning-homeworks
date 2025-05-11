#  Number
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

# String
# 1
from datetime import datetime
name, year = input("Enter name: "), int(input("Enter birth year: "))
print(f"{name}, you are {datetime.now().year - year} years old.")

# 2 - Extract car names from this text: txt = 'LMaasleitbtui'
txt = "LMaasleitbtui"
print(txt[1::2])

# 3
txt = input("Write something: ")
print("Length of the word: ", len(txt))
print("Upper: " + txt.upper() + "\nLower: " + txt.lower())

# 4
word = input("Write a word: ")
print("Palindrome" if word[::-1] == word else "Not palindrome")

# 5
string = input("Write word: ")
a, b = 0, 0
for i in string:
  if not i.isalpha():
    continue
  if i in "aeiou":
    a += 1
  elif i != ' ':
    b += 1
print(f"Vowels: {a}\nConsonant: {b}")

# 6
str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")
print("Contains" if str2 in str1 or str1 in str2 else "No")

# 7
string = input("Enter sentence: ")
rep = input("Replace: ")
rep_sen = input("With: ")
print(string.replace(rep, rep_sen))

# 8
string = input("Enter string: ")
print(f"First: {string[0]}\nLast: {string[-1]}")

# 9
print(input("Enter word: ")[::-1])

# 10
print(f"{len(input("Enter sentence: ").split(" "))} words")

# 11
string = input("Enter sentence or word: ")
isNumeric = False
for i in string:
  if i.isdigit():
    isNumeric = True
    break
print("Contains number" if isNumeric else "Not")

# 12
words_list = []
while True:
  word = input("Enter word (or enter /continue for completed list): ")
  if word == "/continue":
    break
  words_list.append(word)
sep = input("Enter seperator: ")
print(sep.join(words_list))

# 13
print(input("Enter sentence: ").replace(" ", ''))

# 14
str1, str2 = input("Enter first sentence: "), input("Enter second sentence: ")
print("Equal" if str1 == str2 else "Not equal")

# 15
sentence = input("Enter sentence: ").title()
print("".join(x[0] for x in sentence.split()))

# 16
sentence, char = input("Enter sentence: "), input("Enter removal character: ")
print(sentence.replace(char, ''))

# 17
print(''.join('*' if c in "aeiouAEIOU" else c for c in input("Enter sentence: ")))

# 18
string = input("Enter sentence: ")
start_str = input("Start with: ")
end_str = input("End with: ")
print("Yes" if string.startswith(start_str) and string.endswith(end_str) else "No")

# Boolean
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