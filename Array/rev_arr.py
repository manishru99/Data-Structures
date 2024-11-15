#1,2,3,4,2
#O/p: 2,4,3,2,1

def rev_arr(arr, n):
    for i, _ in enumerate(arr[:n // 2]):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr


n = int(input("Size: "))
arr = []
for _ in range(n):
    arr.append(int(input()))
rev_arr(arr, n)
for i in range(n):
    print(arr[i])