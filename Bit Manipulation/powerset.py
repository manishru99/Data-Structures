
def subsets(self, nums: List[int]) -> List[List[int]]:
    #Bit manipulation sol
    #eg. nums = [1,2,3]
    n = len(nums)        #n = size of list
    subsets = 1<<n  #num of subsets
    #Run a loop from 0 to subsets-1
    #eg. from 0 to 7
    ans = []
    for num in range(0, subsets):  #O(2**n)
        lst = []
        for i in range(0, n):      #O(n)
            #Check if ith bit is set or not
            if(num & (1<<i)):
                lst.append(nums[i])
        ans.append(lst)
    return ans

#TC = O(n x 2**n)
#SC = O(n x 2**n)  (approx)




        