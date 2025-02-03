#Remove duplicates from Sorted Array

#Brute force
def removeDuplicates(arr):
    #Declare a HashSet.
    #Run a for loop from starting to the end.
    #Put every element of the array in the set.
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    #Store size of the set in a variable k.
    k = len(st)
    #Now put all elements of the set in the array from the starting of the array.
    #Return k
    index = 0
    for x in st:
        arr[index] = x
        index += 1
    return k

arr = [1, 1, 2, 2, 2, 3, 3]
k = removeDuplicates(arr)
print("The array after removing duplicate elements is ")
for i in range(k):
    print(arr[i], end=" ")