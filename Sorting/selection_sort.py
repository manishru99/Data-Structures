#Selection sort selects the minimum and brings to the front

def selection_sort(arr, n):
    #2 pointers
    #1 for the element to be checked
    #And other from i+1 to n
    #while(i<n):
    for i in range(n-1):
        #for each iteration ith index is considered min
        min_index = i 
        for j in range(i+1, n):
            if(arr[j] < arr[min_index]):
                min_index = j
        #move min element to it's correct position
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr




n = int(input("Size: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))

print("Array before sorting: ")
for i in range(n):
    print(arr[i])

arr = selection_sort(arr, n)

print("Array after sorting: ")
for i in range(n):
    print(arr[i])


#TC = O(n^2)
#As for each outer loop iteration, the inner loop runs for n-i-1 times
# = n + n-1 + n-2 + ...

