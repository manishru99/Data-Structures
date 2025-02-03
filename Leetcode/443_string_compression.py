def compress(self, chars: List[str]) -> int:
        #Brute
        s = ""
        n = len(chars)
        i = 0

        while(i < n): #O(n)
            char = chars[i]
            cnt = 0
            #Count same chars
            while(i<n and chars[i] == char): #i starts from the outer ##O(n)
            #while loop i
                cnt += 1
                i += 1
            #Append the char to result
            s += char
            #Append the count only if > 1
            if(cnt > 1):
                s += str(cnt) 
            #Update the orig array
        for i in range(len(s)):    ##O(n)
            chars[i] = s[i]
        
        return len(s)

#TC = O(n) + O(n) + O(n) = O(n)
#SC = O(n) As using an extra str s 