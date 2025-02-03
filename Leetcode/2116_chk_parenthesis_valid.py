class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        st = []
        n = len(s)
        #For odd length hint
        if(n%2 != 0): return False 

        #left to right
        open_cnt = 0
        flexible_cnt = 0
        #open and flex parenthesis
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    open_cnt += 1
                else:  #here s[i] == ')'
                    open_cnt -= 1
            else:  #index is flexible
                flexible_cnt += 1
            
            #flex can't balance
            if open_cnt + flexible_cnt < 0:
                return False

            
        #right to left
        close_cnt = 0
        flexible_cnt = 0
        for i in range(n-1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    close_cnt += 1
                else:  #s[i]=='('
                    close_cnt -= 1
            else:  #inde is flexible
                flexible_cnt += 1

        #flex can't balance
            if close_cnt + flexible_cnt < 0:
                return False

        #both passed then str is valid
        return True
    
#TC = O(2n) = O(n)
#SC = O(1)

                    

            
