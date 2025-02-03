class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        length = len(flowerbed)
        i = 0
        while i<length:  #O(n)
            #Check if empty
            if flowerbed[i] == 0:
                #Check if prev and next are also empty
                #or also if out of bounds
                prev_empty = (i==0) or (flowerbed[i-1] == 0)
                next_empty = (i == length-1) or (flowerbed[i+1]==0)

                if prev_empty and next_empty:
                    #Plant a flower
                    flowerbed[i] = 1
                    cnt += 1
                    #Skip next plot to avoid adjacent planting
                    i += 1
            # Move to the next plot
            i += 1
        if cnt >= n:
            return True
        else: 
            return False
        #or simply return
        #return cnt >= n

#TC = O(n)
#SC = O(1)


