
def maxRunTime( n: int, batteries) -> int:
    '''
    batteries.sort(reverse=True)
    max_time = sum(batteries)

    for t in range(max_time, 0, -1):
        t_pow = 0
        for b in batteries:
            t_pow += min(b, t)
            if t_pow >= t*n:
                return t
    return 0
    '''
    '''
    #Optimal
    batteries.sort()  # Sort the batteries for optimal allocation
    left, right = 1, sum(batteries) // n

    while left < right:
        mid = left + (right - left)//2
        t_pow = 0

        for b in batteries:
            t_pow += min(b, mid)
        if t_pow >= mid*n:
            left = mid
        else:
            right = mid-1
    return left
    Sort batteries (O(m log m)
    Binary Search (O(log S))
    Sorting Batteries: 
    O(mlogm)
    Binary Search on t:
    O(log(∑batteries/n))
    Checking Feasibility of mid: 
    O(m)
    Overall, 
    O(mlogm), which is efficient for large inputs.
    '''
    total_power = sum(batteries)
    low, high, res = 0, total_power, 0
    
    while low <= high:
        mid = low + (high - low) // 2
        if isPossible(n, mid, batteries):
            res = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return res

def isPossible( n: int, k: int, batteries) -> bool:
    target = n * k
    total = sum(min(b, k) for b in batteries)
    return total >= target
    

b = [4, 2, 4]
print(maxRunTime(2, b))
'''
TC =
Binary Search: 
O(log(∑batteries))
Checking Feasibility (isPossible): 
O(m)
Overall Complexity: 
O(mlog(∑batteries)), which is efficient.
'''