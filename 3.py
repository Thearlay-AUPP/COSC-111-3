c = input("Number from 1 to 5: ")
list1 = [1, 2, 3, 4, 5]
try:
    c = int(c)
except ValueError:
    print("again")
else:
    list1 = [x for x in list1 if x <= c]
print(list1)