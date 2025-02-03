#Generate all subarrays
def gen_subarrays(arr):
    n = len(arr)
    sub_arr = []
    for i in range(n): #O(n)
        for j in range(i, n): #O(n)
            sub_arr.append(arr[i : j+1])  #O(n)
    return sub_arr

arr = [2, 5, 1, 7, 10]
print(gen_subarrays(arr))

#TC = O(n^3)