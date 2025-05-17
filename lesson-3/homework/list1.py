list1 = ["apple", "banana", "orange", "banana", "apple", "pineapple"]
print(list1.count(input("Enter fruit that counts in given list: ")))

list1 = [1, 5, 6, 7, 8, 3, 55, 66, 32, 43]
print(sum(list1))

print(f"max: {max(list1)}; min: {min(list1)}")

try:
    print(
        "Yes" if list1.index(int(input("Enter number: "))) >= 0 else "Not in the list"
    )
except:
    print("Not in the list")

empty = []
if len(list1) > 0:
    print(list1[0], list1[-1])
if len(empty) > 0:
    print(empty[0], list1[-1])

new_list = list1[:3]
new_list_reverse = list1[::-1]
new_list_sorted = sorted(list1)
print(new_list, new_list_reverse, new_list_sorted)

old_with_duplicates = [2, 5, 6, 7, 5, 8, 7, 10, 14, 13, 11, 15, 14]
new_unique = list(set(old_with_duplicates))
print(new_unique)

try:
    index, number = map(int, input("Enter index and number (0 2): ").split())
    old_with_duplicates.insert(index, number)
except:
    print("Error")
print(old_with_duplicates)

try:
    number = int(input("Enter number: "))
    print(old_with_duplicates.index(number))
except:
    print("error")

print(len(list1) > 0)

even, odd = 0, 0
for i in list1:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, odd)

list2 = ["apple", "banana", "pineapple"]
list3 = [2, 4, 5, 6, 7, 9]
new_l = list2 + list3
print(new_l)

list2 = [1, 2, 3, 4, 5, 6]
subl = [3, 4, 5]
print(
    "Yes" if list2[list2.index(subl[0]) : list2.index(subl[-1]) + 1] == subl else "No"
)

# pro
found = False
for i in range(len(list2) - len(subl) + 1):
    if list2[i : i + len(subl)] == subl:
        found = True
        break

print("Yes" if found else "No")

try:
    index, number = map(int, input("Enter index and number: ").split())
    list1[index] = number
    print(list1)
except:
    print("Error")

print(f"Second max: {max(sorted(list1)[:-1])}; Second min: {min(sorted(list1)[1:])}")

even_l = [x for x in list1 if x % 2 == 0]
odd_l = [x for x in list1 if x % 2 == 1]
print(even_l, odd_l)

print(len(list1), list1.copy())

list1 = [10, 20, 30, 40, 50, 60]
print(list1[len(list1) // 2], list1[len(list1) // 2 - 1] if len(list1) % 2 == 0 else "")

try:
    index1, index2 = map(int, input("Enter indexes for sublist: ").split())
    print(max(list1[index1:index2]), min(list1[index1:index2]))
except:
    print("Error")

try:
    index = int(input("Enter index: "))
    list1.remove(list1[index])
    print(list1)
except Exception as e:
    print("Error")


def isSorted():
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            if list1[i] > list1[j]:
                return False
    return True


print(isSorted())

try:
    list2 = [1, 2, 3, 4]
    n = int(input("Enter num: "))
    print(list2 * n)
except:
    print("Error")

list2 = [2, 3, 0, 78]
print(sorted(list1 + list2))

try:
    elem = int(input("Enter number: "))
    i = 0
    indeces = []
    while i < len(old_with_duplicates):
        if old_with_duplicates.index(elem, i):
            indeces.append(old_with_duplicates.index(elem, i))
            i = old_with_duplicates.index(elem, i)
        i += 1
    print(indeces)
except Exception as e:
    print(e)

new_l = [list1[-1]] + list1[:-1]
print(new_l)

try:
    start, end = map(int, input("Enter start and last number: ").split())
    list2 = list(range(start, end + 1))
    print(list2)
except Exception as e:
    print(e)

list2 = [4, 78, -18, 543, 635, 32, 54, 6, -12, -435, -32, 8, 7, -5654, -1232, 543, -643]
print(
    f"Negative: {sum([x for x in list2 if x < 0])}; Positive: {sum([x for x in list2 if x > 0])}"
)

list2 = [1, 5, 7, 9, 7, 5, 1]
print("Yes" if list2 == list2[::-1] else "No")
print("Yes" if list1 == list1[::-1] else "No")

newl = []
try:
    n = int(input("Enter length list: "))
    for i in range(0, len(list1), n):
        newl.append(list1[i : i + n])
    print(newl)
except Exception as e:
    print(e)

new_unique_l = list(set(old_with_duplicates))
print(new_unique_l)
