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