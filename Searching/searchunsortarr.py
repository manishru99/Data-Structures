def findElement(arr, n, key):
    for i in range(n):              #TC=O(n)
        if(arr[i]== key):
            return i
    # If the key is not found
    return -1


if __name__ == '__main__':
    arr = []
    n = int(input("array size:"))
    key = int(input("key:"))
    for i in range(0,n):         #TC=O(n)
        e = int(input())
        arr.append(e)

    #search
    index = findElement(arr, n, key)
    if(index!=-1):
        print("Element is at position: "+ str(index+1))
    else:
        print("Not found!")

