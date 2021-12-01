def fibonacci_one(n):
    new_list = [0, ]
    for x in range(0, n+1):
        sum = new_list[x] + new_list[x-1]
        new_list.append(sum)
    length = len(new_list)
    return length

fibonacci_one(2)
