class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        set_a = set()
        for i in range(len(nums)): #O(n)
            set_a.add(nums[i])  #Set insertion takes logn time
        #The above set has unique elements
        #Now put set elem back to array
        k = len(set_a)
        j = 0
        for x in set_a:   #O(n)
            nums[j] = x
            j += 1
        return k
        #TC = O(nlogn) + O(n)
        #SC = O(n)
        '''
        #Optimized
        #Two pointer approach
        l, r = 0, 0
        n = len(nums)
        while r < n:
            if nums[l] == nums[r]:
                r += 1
            else:
                nums[l+1] = nums[r]
                l += 1
                r += 1
        return l+1
        #TC = O(n)
        #SC = O(1)