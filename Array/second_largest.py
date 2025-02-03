#Find Second Smallest and Second Largest Element in an array

#Considering we are not given an unique elements array
#And the array is not sorted
'''
#Brute force
#TC = O(nlogn + n)
def second_largest_smallest(a):    
    n = len(a)
    a.sort()  #TC = O(nlogn)
    largest = n-1
    sec_l = -1
    for i in range(n-2, -1, -1):  #TC = O(n) when elem not present
        if(a[i] < a[largest]):         #eg a = [7,7,7,7,7]
            sec_l = a[i]
            break
    
    smallest = 0
    sec_s = -1
    for i in range(0, n):
        if(a[i] > a[smallest]):
            sec_s = a[i]
            break
    
    return [sec_l, sec_s] #return as a list of sec_l and sec_s

#Better approach
#O(n + n + n + n) = O(4n) =approx(n)
def second_largest_smallest(a): 
    #First pass
    n = len(a)
    #Find largest
    largest = a[0]
    for i in range(len(a)):   #O(n)
        if(a[i] > largest):
            largest = a[i]
    #Find smallest
    smallest = a[0]
    for i in range(len(a)):   #O(n)
        if(a[i] < smallest):
            smallest = a[i]
    #print(smallest)

    #Second pass
    sec_l = -1
    sec_s = -1
    for i in range(len(a)):  #O(n)
        #Find sec_l
        if((a[i] > sec_l) and (a[i] != largest)):
            sec_l = a[i] 
    for i in range(len(a)):   #O(n)
        #Find sec_s
        if( (a[i] > smallest) and (a[i] != smallest) ):
            sec_s = a[i]
            break

    return [sec_l, sec_s]
'''
#Optimal approach
#TC: O(N), Single-pass solution

#SC: O(1)
def second_largest_smallest(a):
    #Assuming no -ve nos
    #If -ve nos present then we can take sec_l = - INT_MIN
    n = len(a)
    if(n<2):
        return -1
    #largest = a[0]
    largest = float('-inf')
    #sec_l = -1
    sec_l = float('-inf')
    smallest = float('inf')
    sec_s = float('inf')
    
    #sec largest
    for i in range(n):
        if( (a[i] > largest)):
            sec_l = largest
            largest = a[i]
        elif ( (a[i] > sec_l) and (a[i] != largest) ):
            sec_l = a[i]
            
    #sec smallest
    for i in range(n):
        if (a[i] < smallest):
            sec_s = smallest
            smallest = a[i]
        elif (a[i] < sec_s and a[i] != smallest):
            sec_s = a[i]
    
    return [sec_l, sec_s] 

    
    


a = [1, 2, 4, 7, 7, 5]
#a = [1, 2, 3, 4, 5]
op_lst = second_largest_smallest(a)
print(op_lst)