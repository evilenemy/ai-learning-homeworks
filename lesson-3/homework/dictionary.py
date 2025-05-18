human = {"name": "MuhammadAli", "age": 21, "surname": "Magamedov", "country": "Uzbekistan", "city": "Bukhara", "location": {"lat": 31.3232345456, "lon": 64.576693275}}
human_2 = {"province": "Bukhara"}
key = input("Enter key: ")
if key in human.keys():
  print(human[key])
else:
  print("Not exists")

print(len(human.keys()))

keys = [x for x in human.keys()]
values = [x for x in human.values()]
print(keys, values)

human.update(human_2)
print(human)

key = input("Enter key: ")
if key in human.keys():
  human.pop(key)
  print(human)
else:
  print("key doesn't exists")

emptyDict = dict()

print("Not empty" if len(human.items()) > 0 else "empty")

key = input("Enter key: ")
if key in human.keys():
  print((key, human[key]))
else:
  print("Key doesn't exists")

key = input("Enter key: ")
if key in human.keys():
  human[key] = input("Enter value: ")
  print(human)
else:
  print("Key doesnot exist")

value = input("Enter value: ")
values = [x for x in human.values()]
print(values.count(value))

new_dict = {}
for key, value in human.items():
  new_dict[value] = key

print(new_dict)

keys = []
value = input("Enter value: ")

for key, val in human.items():
  if val == value:
    keys.append(key)

print(keys)

keys = [x for x in human.keys()]
values = [x for x in human.values()]
human2 = dict()

for i in range(len(keys)):
  human2[keys[i]] = values[i]

print(human2)

keys = []
nested_keys = []

for key, val in human.items():
  if type(val) == dict:
    keys.append(key)
    nested_keys.append([x for x in val.keys()])

print(f"Nested value keys: {','.join(keys)}" if len(keys) > 0 else "None")
print(human[keys[0]][nested_keys[0][0]] if len(keys) > 0 else "None")

dictionary = {}

while True:
  key = input("Enter key or /cancel: ")
  if key == "/cancel":
    break
  value = input("Enter value: ")
  dictionary[key] = value if len(value) > 0 else 'default'

print(dictionary)

random_dict = {"a": 10, "b": 20, "c": 30, "d": 10}
print(len(set([x for x in random_dict.values()])))

sorted_dict = dict()
keys = sorted([x for x in human.keys()])
for key in keys:
  sorted_dict[key] = human[key]
print(sorted_dict)

dict1 = {"apple": 3, "banana": 1, 'orange': 2}

sorted_val_dict = dict()
values = sorted(dict1.items(), key=lambda x: x[1])
print(values)

dict2 = {}
for key, value in dict1.items():
  if value > 1:
    dict2[key] = value

print(dict2)

human2 = {"name": "Abduvohid", "age": 20, "job": "developer"}
set1 = set([x for x in human.keys()])
set2 = set([x for x in human2.keys()])
print(list(set1.intersection(set2)))

tuple1 = (("age", 21), ("name", "Shaxriyor"), ("surname", "Abdumalikov"))
new_dict = {}
for i in tuple1:
  new_dict[i[0]] = i[1]

print(new_dict)

print([x for x in human.items()][0])