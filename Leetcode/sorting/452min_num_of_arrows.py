class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        cnt = 1
        end = points[0][1]
    
        for i in range(1, len(points)):
            curr_start = points[i][0]
            if curr_start > end:
                cnt += 1
                end = points[i][1]  
        return cnt

'''
TC = O(nlogn)
SC = O(n)
'''