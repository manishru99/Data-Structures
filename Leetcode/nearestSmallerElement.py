class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        #Approach 1: 2 for loops
        #Inside for loop will run from prev elem to 1st O(n^2)
        
        #Approach 2
        G = []
        st = []
        for num in A:
            while st and st[-1] >= num:
                st.pop()
            if st:  #Not empty
                G.append(st[-1])
            else:
                G.append(-1)
            #Push curr in st
            st.append(num)
        return G
        