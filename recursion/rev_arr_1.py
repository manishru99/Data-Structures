#Swap an array by recursion by using 1 pointer a
#TC = O(n)
#SC = O(n)
def rev_arr(arr, n, a):
    #base
    #if(a>=n//2):
    #    return
    if(a >= n // 2):
        return
    # Swap elements using tuple unpacking
    #Swapping here done in constant time O(1)
    arr[a], arr[n - a - 1] = arr[n - a - 1], arr[a]
    # Recursive call
    rev_arr(arr, n, a + 1)



n= int(input("Size: "))
arr = []
print("Enter arr elements: ")
for i in range(n):
    arr.append(int(input()))

rev_arr(arr, len(arr), 0)
for i in range(len(arr)):
    print(arr[i])