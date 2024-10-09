#using Array Reverse Using an Extra Array (Non In-place)

def rev_arr_using_extr_arr(arr):
    reversed_arr = arr[::-1]   #TC: O(n)
#Copying elements to a new array is a linear operation.

    print("\nReversed array using_extr_arr:", end=" ")
    for i in reversed_arr:
        print(i, end=" ")


def rev_arr_using_loop(arr, start, end):
    while(start<end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print("\nReversed arr using_loop:")
    print(arr)

#Array Reverse Inbuilt Methods (Non In-place)
def rev_arr_inbuilt(arr):
    reversed_arr = list(reversed(arr))
    return reversed_arr


#Array Reverse Recursion (In-place or Non In-place)
def rev_arr_using_recursion(arr, start, end):
    if(start>=end):
        return
    arr[start], arr[end] = arr[end], arr[start]
    rev_arr_using_recursion(arr, start+1, end-1)


or_arr = [1,2,3,4,5,6]
rev_arr_using_extr_arr(or_arr)

rev_arr_using_loop(or_arr, 0,5)

inbuilt_arr = rev_arr_inbuilt(or_arr)
print("\nrev_arr_inbuilt:",inbuilt_arr)

rec_arr = rev_arr_using_recursion(or_arr, 0,5)
print("\nrev_arr_using_recursion:",rec_arr)