def rec_name(name, n):
    if(n<=0):
        return
    print(name)
    rec_name(name, n-1)

name = input()
n = int(input())
rec_name(name, n)

#TC = O(n)
#SC = O(n)



