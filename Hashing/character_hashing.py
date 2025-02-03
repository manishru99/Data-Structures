#Code if the string contains only lowercase:
#ord() function returns the Unicode code point of a given character
def main():
    
    #n = int(input("Size of arr: "))
    #s = list(map( input("Enter the elements of the array: ").split()))
    s= input("Enter the string: ")
    #Precompute
    hash_map = [0] * 26
    for char in s:
        hash_map[ord(char) - ord('a')] += 1
    
    q = int(input("Enter num of queries: "))
    for _ in range(q):
        c = input("Enter character: ")

        #FETCH
        print(hash_map[ord(c) - ord('a')])


if __name__ == "__main__":
    main()