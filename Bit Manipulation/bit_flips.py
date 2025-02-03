#Minimum Bit Flips to Convert Number
# eg. start = 10 goal = 7
# 1010              0111
# bit flips = 3
# 

'''
def convert_to_binary(dec_num):
    return bin(dec_num)[2:]

def bit_flip(x1, x2):
    x1_b = str(convert_to_binary(x1))
    x2_b = str(convert_to_binary(x2))
    cnt = 0
    # Ensure both binaries are of the same length by padding with zeros
    max_len = max(len(x1_b), len(x2_b))
    x1_b = x1_b.zfill(max_len)
    x2_b = x2_b.zfill(max_len)

    # Loop through each digit from the end
    for i in range(1, max_len + 1):
        digit1 = int(x1_b[-i])
        digit2 = int(x2_b[-i])

        if(digit1 & digit2 == True):
            cnt += 1
    return cnt
'''
def bit_flip(x1, x2):
    #XOR of x1 and x2 will give a binary num where
    # bit flip is required.
    # (1010)
    #^(0111)
    #+(1101)
    # Then count num of 1s 
    ans = x1 ^ x2
    #Now hamming weight code
    cnt = 0
    while(ans != 0):
        ans = ans & (ans-1)
        cnt += 1
    return cnt
'''
Approach 2

'''
x1 = int(input("Enter start: "))
x2 = int(input("Enter goal: "))

print(bit_flip(x1, x2))