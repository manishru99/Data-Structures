#Swap an array by recursion by using 2 pointers l and r
def rev_arr(arr, n, l, r):
    #base
    if(l>=r):
        return
    #swap logic
    #temp = a[l]       
    #a[l] = a[r]
    #a[r] = temp
    # Swap elements using tuple unpacking
    arr[l], arr[r] = arr[r], arr[l]
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