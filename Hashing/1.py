#find out how many times the number appears in the array
#[1, 2, 1, 3, 2] For 1 -> 2 (appears 2 times)

#Brute force approach

def find_num(arr, x):
    count = 0
    for i in arr:
        if(i == x):
            count += 1
    return count



arr = [1, 2, 1, 3, 2]
x = int(input("Enter x:"))
count = find_num(arr, x)
print(f'Num appears {count} times')


def find_char(str_i, x1):
    count1 = 0
    for i in str_i:
        if(i==x1):
            count1 += 1
    return count1

#For Character
str_i = 'abcada'
x1 = input("x: ")
count1 = find_char(str_i, x1)
print(f'Num appears {count1} times')

