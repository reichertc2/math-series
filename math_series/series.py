def fibonacci_one(n):
    new_list = [0, ]
    for item in range(0, n):
        new_list.append(1)
        new_list.append(new_list[item]+new_list[item+1])

        # if n == 1:
        #     return 1
        # return fibonacci_one(n-1) + n
    return new_list


fibonacci_one(3)
