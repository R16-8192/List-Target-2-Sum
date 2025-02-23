import random
length = int(input("Enter list size : "))
numlist = []
while length > 0:
    i = random.randint(0, 9)
    numlist.append(i)
    length -= 1
print(numlist)
if len(numlist) == 0:
    print("The list is empty !!")
    exit()
target = int(input("Enter Target : "))
found = False
for i in range(len(numlist)):
    for j in range(i + 1 , len(numlist)):
        if numlist[i] + numlist[j] == target:
            print(f"[{i}, {j}]")
            found = True
            break
        if found:
            break
if not found:
    print("Target Not found !!")
