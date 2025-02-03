'''
Brute force
from collections import deque
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        i, j = 0, n-1
        tc = 0 #total cost
        #chosen_one = float('inf') #Initially chosen one is the 0th index
        
        # Use a deque to store the candidates from both ends
        left_cand = deque()
        right_cand = deque()
        
        # Keep hiring until we have hired k workers
        while k > 0:
            while len(left_cand) < candidates and i <= j:
                left_cand.append(costs[i])
                i += 1

            while len(right_cand) < candidates and i <= j:
                right_cand.append(costs[j])
                j -= 1

            #Till here in each session both queues are filled with max candidates
            
            #Now compare for lower costs
            # Ensure deques are not empty before finding min values
            if left_cand:
                min_left = min(left_cand)
            else:
                min_left = float('inf')
            
            if right_cand:
                min_right = min(right_cand)
            else:
                min_right = float('inf')
            
            # Now compare for lower costs
            if min_left <= min_right:
                tc += min_left
                left_cand.remove(min_left)
            else:
                tc += min_right
                right_cand.remove(min_right)
            
            #if left_cand and right_cand: #If there are workers in both
            #
            #elif left_cand: #workers remain only in left
            #    tc += left_cand.popleft()
            #elif right_cand: #workers remain only in right
            #     tc += right_cand.popleft()
            
            k -= 1
        return tc
'''
            

        
        




