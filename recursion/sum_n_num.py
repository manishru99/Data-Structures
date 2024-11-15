#parameterised way
#sum of n numbers
def sum_n_num(i, sum):     #1st: 3,0
    #base
    if(i<1):               #3!<1
        print("Sum of num: ", sum)           #this will not execute
        return
    sum_n_num(i-1, sum+i)                     #recursive call, 2,3



n = int(input("Enter n:"))
sum_n_num(n, 0) #n=3