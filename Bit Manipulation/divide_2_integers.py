#29. Divide Two Integers

#Given two integers dividend and divisor, divide two integers 
#without using multiplication, division, and mod operator.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #Naive approach
        #Time Limit Exceeded for this solution
        '''
        sum = 0
        cnt = 0
        while(sum + divisor <= dividend):
            sum += divisor
            cnt += 1
        return cnt
        '''
        #Edge case
        if(dividend == divisor): return 1 
        #sign = True  #+ve
        #if(dividend >= 0 and divisor < 0): sign = False #-ve
        #if(dividend < 0 and divisor > 0): sign = False #-ve
        sign = (dividend < 0) == (divisor < 0)

        n = abs(dividend)
        d = abs(divisor)
        ans = 0

        while(n >= d):    #TC= log2 n
            cnt = 0
            #TC= log2 n
            while(n >= (d * pow(2, cnt+1))):  #2^cnt+1 is also d << (cnt+1)
                cnt += 1

            ans += pow(2, cnt)  #or (1 << cnt) 
            # or 2**cnt
            n = n - (d* (pow(2, cnt)))
        '''
        if(ans >= pow(2, 31) and sign == True):
            return INT_MAX
        if(ans >= pow(2, 31) and sign == False):
            return INT_MIN
        '''
        if not sign:
            ans = -ans

        # Handle overflow cases
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if ans > INT_MAX:
            return INT_MAX
        if ans < INT_MIN:
            return INT_MIN

        return ans 

#TC = O((log2 n)^2)
#SC = O(1)
