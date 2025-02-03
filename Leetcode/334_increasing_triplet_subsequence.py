class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        #Brute
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if(nums[i] < nums[j] < nums[k]):
                        return True
        return False
        #TC=O(n**3)
        '''

        #Optimal
        x = float('inf')
        y = float('inf')

        for num in nums:   #O(n)
            #Small num update
            if(num <= x):
                x = num #Update
            #2nd small num update
            elif(num <= y):
                y = num #Update
            else:
                #If a num greater than both x and y exists afterwards
                return True
        #If we don't find anything
        return False

#TC = O(n)
#SC = O(1)
