elements = ("apple", "banana", "pineapple", "orange", "cherry", "apple", "orange")
print(elements.count(input("Enter fruit: ")))

nums = (1,5,9,11,15,78,23)
print(min(nums), max(nums))

cars = ("ferrari", "bugatti", "tesla", "bmw", "mercedes")
print("Yes" if input("Enter car: ") in cars else "No")

empty = tuple()
if len(elements) > 0:
  print(elements[0], elements[-1])
if len(empty) > 0:
  print(empty[0], empty[-1])

print(len(elements))

new_tuple = elements[:3]
print(new_tuple)

combine_tuple = elements + new_tuple
print(combine_tuple)

print("Yes" if len(elements) > 0 else "No")

fruit = input("Enter fruit: ")
print([x for x in range(len(elements)) if elements[x] == fruit])

tuple1 = (5,8,3,5,7,9,0,79,54,36,76)
tuple2 = (0,3,6,8,9,10)
print(min(tuple1[:tuple1.index(min(tuple1))] + tuple1[tuple1.index(min(tuple1)) + 1:]), max(tuple1[:tuple1.index(max(tuple1))] + tuple1[tuple1.index(max(tuple1)) + 1:]))

singletuple = (1,)

list1 = [1,4,5,6,7,8,9]
print(tuple(list1))

print("Yes" if tuple2 == tuple(sorted(tuple2)) else "No")

try:
  start, end = map(int, input("Enter start and end indeces: ").split())
  print(min(tuple1[start:end]), max(tuple1[start:end]))
except:
  print("Error")

remove_num = int(input("Enter number what should remove: "))
new_tuple = tuple1[:tuple1.index(remove_num)] + tuple1[tuple1.index(remove_num) + 1:]
print(new_tuple)

try:
  big_tuple = []
  n = int(input("Enter length of elements: "))
  for i in range(0, len(tuple1), n):
    big_tuple.append(tuple(tuple1[i:i+n]))
  print(tuple(big_tuple))
except:
  print("Error")

try:
  repeated = (1,2,3,4)
  new_tpl = repeated * int(input("Enter number: "))
  print(new_tpl)
except Exception as e:
  print(e)

try:
  start, end = map(int, input("Enter start and end: ").split())
  new_tpl = tuple(range(start, end+1))
  print(new_tpl)
except Exception as e:
  print(e)

reversed_tuple = tuple1[::-1]
print(reversed_tuple)

tuple2 = (1,2,3,4,3,2,1)
print("Yes" if tuple2 == tuple2[::-1] else "No")

unique_tuple = tuple(set(tuple1))
print(unique_tuple)