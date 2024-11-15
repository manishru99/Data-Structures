# Count subsequences with sum sum = k

def count_subseq_sum_k(sequence, k, index = 0, current_subseq = None, current_sum = 0):
    if(current_subseq is None):
        current_subseq = []

    #base
    if(index == len(sequence)):
        if(current_sum == k):
            return 1
        return 0

    #include
    l = count_subseq_sum_k(sequence, k, index+1, current_subseq + [sequence[index]], current_sum + sequence[index])

    #exclude
    r = count_subseq_sum_k(sequence, k, index+1, current_subseq, current_sum)

    return l+r



n = int(input("Enter seq length: "))
print("Enter elements:")
seq = []
for i in range(n):
    seq.append(int(input()))

target_sum = int(input("Enter k: "))
print(count_subseq_sum_k(seq, target_sum))

#TC = O(2^n)
#SC = O(n)




