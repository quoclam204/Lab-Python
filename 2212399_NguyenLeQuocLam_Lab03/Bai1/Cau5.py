list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

output = [a + b for a in list1 for b in list2]

print(output)