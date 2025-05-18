set1 = {1,2,3,4,5,6,7,8,9,0}
set2 = {5,6,7,8,9,1,13}
set3 = {2,3,4}
set3 = set(set1.union(set2))
print(set3)

print(set1.intersection(set2), set1.difference(set2))

print(set1.issubset(set2))

try:
  print("Yes" if int(input("Enter number in set: ")) in set1 else "No")
except:
  print("Error")

print(len(set1))

list1 = [1,3,4,5,6,5,4,8,7,9,8,7,4,2,3]
print(set(list1))

try:
  set1.remove(int(input("Enter removable number: ")))
  print(set1)
except:
  print("Error")

set1.clear()

print(set1.symmetric_difference(set2))

try:
  set1.add(int(input("Enter number: ")))
  print(set1)
except:
  print("Error")

set1.pop()

print(min(set1), max(set1))

even = set()
odd = set()

for i in set1:
  if i % 2 == 0:
    even.add(i)
  else:
    odd.add(i)

print(even, odd)

try:
  start, end = map(int, input("Enter start and end: ").split())
  new_set = set(range(start, end+1))
  print(new_set)
except:
  print("Error")

set3 = set1.union(set2)
print(set3)

print("Yes" if set2.isdisjoint(set3) else "No")

list1 = [4,5,6,7,2,9,8,9,6]
print(list(set(list1)))

print(len(set(list1)))

import random

try:
  new_set = set()
  length = int(input("Enter length: "))
  while True:
    if len(new_set) >= length:
      break
    new_set.add(random.randint(0, 200))
  print(new_set)
except Exception as e:
  print(e)