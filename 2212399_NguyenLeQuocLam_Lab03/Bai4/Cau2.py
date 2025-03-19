dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


# ** Giải nén(gộp lại) những giá trị key value giống nhau
dict3 = {**dict1, **dict2}
print(dict3)