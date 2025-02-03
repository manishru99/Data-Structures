class Solution:
    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        
        while(low != high):
            mid = low + (high-low)//2
            k = self.hours_needed(piles, mid)

            if k <= h:
                high = mid
            else:
                low = mid + 1
        
        return low

    
    def hours_needed(self, piles, k):
        '''
        hr = 0 
        for pile in piles:
            hr += (pile + mid - 1) // mid  # This ensures we round up
        return hr
        '''
        hours = 0
        for pile in piles:
            if pile % k == 0:
                hours += pile // k
            else:
                hours += (pile // k) + 1
        return hours


'''
The number of iterations is approximately log2​(max(piles))
The hours_needed function iterates over all elements in piles, which takes O(n)
time, where n is the number of piles.
TC = O(n log2(max(piles)))
SC = O(1)
'''