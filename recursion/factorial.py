def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)

n = int(input("Enter n: "))
print(fact(n))

#TC=O(n)
#SC=O(n) auxiliary space (taking stack space)