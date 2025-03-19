set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
    print("Không co phần tử chung nào hết")
else:
    print("Những phần tử chung là: ")
    print(set1.intersection(set2))