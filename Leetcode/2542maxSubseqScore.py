from itertools import combinations
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        #Brute force
        m, n = len(nums1), len(nums2)
        score_max = float('-inf')

        for com in combinations(range(n), k):
            #nums1 sum of com
            nums1_sum = sum(nums1[i] for i in com)

            #num2 min of com
            nums2_min = min(nums2[i] for i in com)

            sc = nums1_sum*nums2_min
            score_max = max(score_max, sc)

        return score_max

