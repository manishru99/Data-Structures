#3. Longest Substring Without Repeating Characters
#Explanaation in LEeetcode coding doubts 2

#Substring: A substring is a contiguous non-empty sequence of characters within a string.
#Subsequence: A subsequence is a sequence that can be derived from another sequence of elements 
# without changing the order of the remaining elements.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        #naive
        #TC = O(n)*O(n)*O(n+n) = O(n^3)
        n = len(s)
        #sub_str = []
        maxLen = 0
        #generate all possible substr and check if unique
        for i in range(n):  #O(n)
            for j in range(i, n):  #O(n)
                #sub_str.append(s[i : j+1])
                sub_str = s[i : j+1]  #O(n)
                
                if len(sub_str) == len(set(sub_str)): #O(n)
                    maxLen = max(maxLen, len(sub_str))
        return maxLen
        
        #Better solution (accepted)
        #TC = O(n^3)
        #SC = O(n)
        n = len(s)
        maxLen = 0
        #generate all possible substr and check if unique
        for i in range(n):  #O(n)
            seen_chars = set()
            #unique = True
            for j in range(i, n):  #O(n)
                if s[j] in seen_chars:
                    #unique = False
                    #break if seen
                    break
                #Add if not seen before
                seen_chars.add(s[j])
                sub_str = s[i : j+1]  #O(n)
                #checks if the length of the substring is equal to the number of unique characters in it. 
                # If they are equal, it means that all characters in sub_str are unique.
                if len(sub_str) == len(set(sub_str)): #O(n)
                    maxLen = max(maxLen, len(sub_str))
        return maxLen
        ''' 
        #Optimized
        #TC = O(n)
        #SC = O(n)
        hash_map = {}
        n = len(s)
        maxLen = 0
        l, r = 0, 0
        while r < n:
            '''
            #Check if elem is in the map
            if hash_map[s[r]]:
                #Check the portion from l to r only
                if hash_map[s[r]] >= l:
                    l = hash_map[s[r]] + 1
            '''
            if s[r] in hash_map and hash_map[s[r]] >= l:
                l = hash_map[s[r]] + 1
            # Update the character's position in the map
            hash_map[s[r]] = r
            #Calculate the length of the current substring
            len_str = r-l+1
            #Check if maxLen can be updated
            maxLen = max(maxLen, len_str)
            
            r += 1
        return maxLen

        