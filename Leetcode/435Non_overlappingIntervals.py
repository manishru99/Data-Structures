#From Leetcode 75

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1: return 0
        #intervals.sort(key=lambda x: x[0])  #sort intervals list
        intervals.sort()   #O(nlogn)
        i = 0
        count = 0

        while i < n-1:   #O(n)
            if intervals[i][1] > intervals[i+1][0]: #end of i > start of i+1 it means overlapping
                intervals[i+1][1] = min(intervals[i][1], intervals[i+1][1])
                count += 1 
            i += 1
        return count

#TC = O(nlogn) 
'''
Resolving Overlaps:
If there's an overlap, the second interval (intervals[i+1]) is updated to have the smaller of the two end times (min(intervals[i][1], intervals[i+1][1])). This ensures that the interval with the smaller end time is preserved, minimizing the chance of future overlaps.
The count variable is incremented to track the number of intervals removed.


IMP:

Why Sorting Intervals is O(n log n):
When you call intervals.sort() or intervals.sort(key=lambda x: x[0]), Python sorts the list of intervals by the specified key (default: first element of each subarray).
Sorting a list of n intervals requires Python to:
Divide the list into smaller parts (like in merge sort), which requires log(n) steps.
Merge and compare the intervals in each step, requiring O(n) comparisons for each level of merging.
Combining these steps gives the total time complexity of O(n log n).


''' 
