#check if palindrome: eg, madam
def palindrome(s, i):
    #base case: If the pointer reaches or crosses the middle, it's a palindrome
    if(i >= len(s)//2):
        return True 
    #char_arr[i] == char_arr[n-i-1] 
    if(s[i] != s[len(s)-i-1]):
        return False
    
    return palindrome(s, i+1) 

str = input("Enter string: ")
#char_arr = list(str)
if palindrome(str, 0):
    print(f'"{str}" is a palindrome')
else:
    print(f'"{str}" is not a palindrome')


#TC = O(n/2) = O(n)
#SC = O(n/2) = O(n)