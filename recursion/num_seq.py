#print 4,3,2,1

def rec_num_seq(n):
    #base case
    if(n<=0):
        return
    print(n)
    rec_num_seq(n-1)

n= int(input("Input: "))
rec_num_seq(n)


