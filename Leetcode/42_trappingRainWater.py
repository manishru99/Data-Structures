class Solution:
    def find_left_max(self, height):
        #Find prefix Max
        prefix_max_arr = []
        current_max = float('-inf')
        for num in height:                        #O(n)
            current_max = max(current_max, num)
            prefix_max_arr.append(current_max)
        return prefix_max_arr

    def find_right_max(self, height):
        suffix_max_arr = []
        current_max = float('-inf')
        for num in reversed(height):          #O(n)
            #Update current max
            current_max = max(current_max, num)
            suffix_max_arr.append(current_max)
        suffix_max_arr.reverse()
        return suffix_max_arr

    def trap(self, height: List[int]) -> int:
        total = 0 #Total water trapped
        left_max_arr = self.find_left_max(height)
        right_max_arr = self.find_right_max(height)
        for i in range(len(height)):               #O(n)
            if height[i] < left_max_arr[i] and height[i] < right_max_arr[i]:
                total += min(left_max_arr[i], right_max_arr[i]) - height[i]
        return total


#TC = O(n)