#Naive approach 
def fib(n):
    #2 base conditions
    if(n <= 1):
        return n
    return fib(n-1) + fib(n-2)


n = int(input("Enter the value of n: "))
#print(f"nth Fibonacci is:",fib(n))
print(f"{n}th Fibonacci is: {fib(n)}")

#TC: O(2^n)
#SC: O(n), due to recursion stack
