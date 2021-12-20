def fibonacci_one(n):
    
    if n == 0:
        return 0
    elif n ==1:
        return 1
    
    return fibonacci_one(n-1) + fibonacci_one(n-2)
    
def lucas(n):
    if n==0:
        return 2
    elif n ==1:
        return 1
    return lucas(n-1)+lucas(n-2)

def sum_series(n,i=0,j=1):
    if n == 0:
        return i
    elif n ==1:
        return j
    return sum_series(n-1,i,j)+sum_series(n-2,i,j)

