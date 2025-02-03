class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat) #num of rows
        n = len(mat[0]) #num of cols

        vis_map = {}  #freq store
        #element_position_map = {}
        #Hint 2: Pre-process the positions
        for i in range(len(mat)):    #O(m)
            for j in range(len(mat[0])):   #O(n)
                vis_map[mat[i][j]] = (i, j)
        #print(vis)
        #Hint 3
        #Traverse the array and increment the corresponding row and column frequency using the pre-processed positions.
        row_freq = [0]*m
        col_freq = [0]*n
        for index, elem in enumerate(arr):
            if elem in vis_map:
                #FInd it's row, col number
                row, col = vis_map[elem]
                row_freq[row] += 1
                col_freq[col] += 1
                #Hint 4
                if row_freq[row] == n or col_freq[col] == m:
                    return index
        return -1

'''
TC = O(m*n)
SC = O(m*n)

'''