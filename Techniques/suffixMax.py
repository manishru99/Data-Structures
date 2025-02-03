
def suffixMax(arr):
    suffix_max_arr = []
    current_max = float('-inf')
    for num in reversed(arr):
        #Update current max
        current_max = max(current_max, num)
        suffix_max_arr.append(current_max)
    suffix_max_arr.reverse()
    return suffix_max_arr


arr = [2, 1, 0, 5, 3]
print("Input Array:", arr)
print("Suffix Max Array:", suffixMax(arr))