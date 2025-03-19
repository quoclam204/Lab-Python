def uniqueRows(input):

    # Chuyển mỗi danh sách trong input thành một tuple
    input = map(tuple, input)

    # set: lưu trữ các phần tử ko trùng lặp
    result = set(input)

    # in từng phần tử ra màn hình
    for row in list(result):
        print(row)

if __name__ == "__main__":
    input = [[0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1],
            [1, 1, 1, 0, 0]]
    uniqueRows(input)

    


