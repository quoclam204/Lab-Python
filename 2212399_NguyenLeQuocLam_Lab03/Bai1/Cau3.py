list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# list3 = [list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]]

list3 = [a + b for a, b in zip(list1, list2)]

print(list3)