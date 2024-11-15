#Using Functional recursion
# sum of n numbers

def sum_n(n):
    #base
    if(n==0):
        return 0
    return n + sum_n(n-1)

n = int(input("Enter n: "))
print(sum_n(n))