class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(not prices or n<2):
            return 0

        max_p = 0
        min_p = prices[0]
        
        for p in prices[1:]:
            if(p < min_p):
                min_p = p
            else:
                max_p = max(max_p, p - min_p)
        return max_p