#use backtracking in recursion to print 1,2,3,4
def num_seq_back(n):
    #base
    if(n<1):
        return
    num_seq_back(n-1)# First, call recursively to go to the smallest value
    print(n)  # Print the number when backtracking

n = int(input("Enter val n: "))
num_seq_back(n)