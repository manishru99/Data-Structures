def isPowerOfTwo(self, n: int) -> bool:
        
    #if(n and (n-1) == 0): return True
    #else: return False

    #return n>0 and (n and (n-1)) == 0
    return n > 0 and (n & (n - 1)) == 0