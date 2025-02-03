#Swap an array by recursion by using 2 pointers l and r

#Number of recursive calls = n/2
#Work done per call = O(1)
#TC = O(n/2) = O(n)
#SC = O(n/2) = O(n)

#Same reason for both recursion depth is proportional to n/2

def rev_arr(arr, n, l, r):
    #base
    if(l>=r):
        return
    #swap logic
    #temp = a[l]       
    #a[l] = a[r]
    #a[r] = temp
    # Swap elements using tuple unpacking
    arr[l], arr[r] = arr[r], arr[l]    #O(1)
    # Recursive call
    rev_arr(arr, l+1, r-1)

n= int(input("Size: "))
a = []
print("Enter arr elements: ")
for i in range(n):
    a.append(int(input()))
#l, r = 0, n-1
#rev_arr(a, n, l, r)
rev_arr(a, 0, len(a) - 1)
for i in range(n):
    print(a[i])