class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Brute force
        if not digits:
            return []

        op = []
        #Used dict to map numbers to letters
        phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

        #Backtracking recursive method
        def backtrack(combination, next_digits):
            #base case (no further digits to check)
            if not next_digits:
                op.append(combination)
            

        backtrack("", digits)
        return op
    
