from collections import Counter

def min_operations_to_palindrome(s, pairs):
    results = []
    for l, r in pairs:  #l and r for substr
        substr = s[l-1:r] #ind starts from 1
        freq = Counter(substr)  #o/p dict with counts
        odd_cnt = sum(1 for cnt in freq.values() if cnt % 2!=0)
        results.append(odd_cnt//2)
    return tuple(results)


S1 = "abadabcd"
pairs1 = [(1, 3), (2, 5)]
print(min_operations_to_palindrome(S1, pairs1)) 

S2 = "pmpkk"
pairs2 = [(1, 2), (3, 5), (4, 4)]
print(min_operations_to_palindrome(S2, pairs2)) 