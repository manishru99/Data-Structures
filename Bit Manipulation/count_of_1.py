def hammingWeight(self, n: int) -> int:
    cnt = 0
    while( n != 0):
        n = (n & (n-1))
        cnt += 1
    return cnt

'''
Approach 2

cnt=0
for i in range(0,31):  #32 bit integer
      if(ans & (1<<i)):  #left shift to check each digit
            cnt += 1
'''