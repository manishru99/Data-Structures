class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Brute
        #TC = O(n)
        #SC = O(n)
        n = len(nums)
        '''
        new_k = k % n  #rotate arr by 8 means rotate by 1
        rotated = [0]*n
        for i in range(n):  #O(n)
            rotated[(i + new_k) % n] = nums[i]
        #Copy elem 
        #Note:When you assign nums = rotated[:], you’re only changing the local reference to nums, not the original list.
        for i in range(n):
            nums[i] = rotated[i] 
        '''
        #Better
        #TC = O(k) + O(n-k) + O(k)
        ##TC = O(n+k) = O(n)
        #SC = O(k)
        '''
        if n == 0:
            return
        k = k % n
        if k > n:
            return
        temp = [0] * k
        for i in range(n-k, n):
            temp[i - n + k] = nums[i]
        for i in range(n - k - 1, -1, -1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = temp[i]
        '''
        #Optimized
        #TC = O(n)
        #SC = O(1)
        k = k % n 
        self.reverse(nums, 0, n - k - 1 )
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            

        