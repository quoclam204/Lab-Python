'''
3. Bài tập về chuỗi: viết 2 cách trong đó có 1 cách dùng vòng lặp

a. Đảo ngược 1 chuỗi, s= "hello" → olleh

b. Đảo ngược các từ trong chuỗi “how are you" → "you are how"

c. Kiểm tra một chuỗi có đối xứng hay không? Ví dụ: khokho, madam

d. Kiểm tra 1 chuỗi có phải là chuỗi palindrome hay không? (chuỗi palindrome là chuỗi có một nửa chuỗi là đảo ngược của chuỗi còn lại. 
    Ví dụ: abeeba, madam

e. Đếm tần suất xuất hiện của một từ trong đoan

'''

s = "hello"

# Câu a: C1
def dao_nguoc(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i] # a += text[len(text) - i]: lấy chỉ số cuối cùng và gán cho biến a vd: text[4] = o
    return a

print(dao_nguoc(s))

# C2
'''
return text[::-1]: bắt đầu từ đầu chuỗi và kết thúc cuối chuỗi, -1 là đi ngược lại

text[start:end:step]

start: Chỉ số bắt đầu (mặc định là 0).
end: Chỉ số kết thúc (mặc định là kết thúc chuỗi).
step: Bước đi (mặc định là 1).

'''
def dao_nguoc_2(text):
    return text[::-1]

print(dao_nguoc_2(s))

# câu b: C1
s2 = "how are you"

def dao_nguoc_3(text):
    a = ""
    catChuoi = str(text).split() # mặc định cắt theo khoản trắng
    for i in range(1, len(catChuoi) + 1):
        a += catChuoi[len(catChuoi) - i]  + " "
    return a

print(dao_nguoc_3(s2))

# C2
def dao_nguoc_4(text):
    catChuoi = str(text).split()
    for i in range(len(catChuoi) - 1, -1, -1): # chuỗi đi ngược từ vị trí cuối 
        print(catChuoi[i], end=' ')

dao_nguoc_4(s2)