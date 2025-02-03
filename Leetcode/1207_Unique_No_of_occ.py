class Solution:
    '''
    def are_values_unique(dictionary):
        values = list(dictionary.values())
        return len(values) == len(set(values))
    '''

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #Brute
        #Convert to dict
        #arr_dict = dict(arr)
        hash_map = {}
        #Precompute
        for num in arr:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        #Fetch
        #See if the values are unique
        occurrences = list(hash_map.values())
        return len(occurrences) == len(set(occurrences))

#TC =  O(n)
#SC = O(n)
