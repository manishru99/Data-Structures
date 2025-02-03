#Cann be solved by sliding window or prefix sum
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #Naive
        #Tc = O(k^2)
        #SC = O(1)
        #as for loop and for each k it sums up k elements
        '''
        max_sum = 0
        n = len(cardPoints)
        for i in range(k+1):
            curr_sum = sum(cardPoints[:i]) + sum(cardPoints[n-(k-i):])
            #Update max_sum
            max_sum = max(curr_sum, max_sum)
        return max_sum
        '''

        #Optimized
        #TC = O(k + k) = O(k)
        #SC = O(1)
        lsum, rsum = 0, 0
        max_sum = 0
        n = len(cardPoints)
        for i in range(k): #O(k)
            lsum = lsum + cardPoints[i]
        max_sum = lsum
        right = n - 1
        #O(k)
        for i in range(k-1, -1, -1):  #from k-1 as we need elem from k-1 to 0 for window shrinkage
            lsum -= cardPoints[i]  
            rsum += cardPoints[right]
            right -= 1
            #Update maxsum
            max_sum = max(max_sum, lsum + rsum)
        return max_sum
    


        
        
        
        
        
        
        
        
        
        
