list1 = [5, 20, 15, 20, 25, 50, 20]

def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)
