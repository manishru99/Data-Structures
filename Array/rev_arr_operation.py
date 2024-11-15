#Naive approach
'''
def rotateArr(arr, d):
    n = len(arr)

    for i in range(d):
        #left rotate arr by 1 position in each iteration
        first = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]

        arr[n-1] = first


arr = [1,2,3,4,5,6]
d =2

rotateArr(arr,d)

for i in range(len(arr)):
    print(arr[i], end = " ")
'''
#Time Complexity: O(n*d), the outer loop runs d times, and within each iteration, 
# #the inner loop shifts all n elements of the array by one position, 
# resulting in a total of n*d operations.

#Using temp arr
def rotateArr(arr, d):
    n = len(arr)

    # Handle case when d > n
    d %= n
    
    # Storing rotated version of array
    temp = [0] * n

    # Copy last n - d elements to the front of temp
    for i in range(n-d):  #6-2
        temp[i] = arr[d+i]

    # Copy the first d elements to the back of temp
    for j in range(d):
        temp[n-d+j] = arr[j]

    # Copying the elements of temp in arr
    # to get the final rotated array
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2

    rotateArr(arr, d)

    # Print the rotated array
    for i in range(len(arr)):
        print(arr[i], end=" ")
#Time Complexity: O(n), as we are visiting each element only twice.
#Auxiliary Space: O(n), as we are using an additional temporary array.


