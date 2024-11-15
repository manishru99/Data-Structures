#Takes an elem and places/inserts it in it's correct position/order


def insertion_sort(arr, n):
    #The outer loop should start from i = 1 instead of i = 0 since the first element is already considered sorted in insertion sort.
    for i in range(1, n):
        j=i
        ## Move elements of arr[0..i-1], that are greater than arr[i], to one position ahead
        while( j>0 and arr[j-1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
            print("Runs")
        
    return arr

n = int(input("Size: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))

print("Array before sorting: ")
for i in range(n):
    print(arr[i])

arr = insertion_sort(arr, n)

print("Array after sorting: ")
for i in range(n):
    print(arr[i])


#TC = O(n^2)  (worst and avg case)
#TC = O(n)    (Best case)  
