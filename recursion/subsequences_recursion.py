
def generate_subsequences(sequence, index = 0, current_subsequence=None, result=None):
    if result is None:
        result = []
    if current_subsequence is None:
        current_subsequence = []

    #base case: if we've reached the end of the sequence
    if(index == len(sequence)):          
        result.append(current_subsequence)
        return result
    
    #Exclude 
    generate_subsequences(sequence, index+1, current_subsequence, result)         

    #include
    generate_subsequences(sequence, index+1, current_subsequence + [sequence[index]], result)

    return result

sequence = [1, 2, 3]
subsequences = generate_subsequences(sequence)
print(subsequences)