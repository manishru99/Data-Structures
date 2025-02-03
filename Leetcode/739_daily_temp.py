class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        #Brute force
        '''
        for i in range(n):
            for j in range(i+1, n):
                #a higher temp found
                if temperatures[j] > temperatures[i]:
                    ans[i] = j-i
                    break
        return ans
        #TC = O(n**2)
        '''

        #Optimized approach
        stack = []

        for i in range(n-1, -1, -1): #right to left O(n)
            # Iterate from right to left
            # Pop indices from the stack where temperatures are less or equal to current
            #As stack is implemented with a list in python
            #stack[-1] is -ve indexing to access last elem in a list
            #which is nothing but the stack top
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            # If the stack is not empty, calculate the difference in indices
            if stack:
                answer[i] = stack[-1] - i
            
            # Push the current index onto the stack
            stack.append(i)
        
        return answer
#TC = O(n)
#SC = O(n)


        