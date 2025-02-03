class Solution:
    
        
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        n = len(words)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    cnt += 1
        return cnt

    def isPrefixAndSuffix(self, str1, str2):
        if str2.startswith(str1) and str2.endswith(str1):
            return True
        else:
            return False
#TC = O(n**2)
#SC = O(1)