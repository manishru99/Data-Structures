
#Optimized approach
#Number Hashing
#Steps: 1. Precompute, 2. Fetch 

def main():
    # Input the size of the array
    n = int(input("Enter the size of the array: "))
    
    # Input the array elements
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    #We take the array input using input() and split it into a list of integers

    #PRECOMPUTE / prestoring: 
    # Create a hash (dictionary) to store the 
    # frequency of each number
    hash_map = {}
    for num in arr: #O(n)  #SC = O(k)  k is num of unique elem in the array
        #each index of the hash array represents an element in the given array
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    
    # Input the number of queries
    q = int(input("Enter the number of queries: "))
    
    # Process each query
    for _ in range(q):
        numb = int(input("Enter the number to fetch its frequency: "))
        
        #FETCH
        #TC = O(q) for q queries
        # Fetching and printing the frequency
        print(hash_map.get(numb,0)) #O(1) #Get numb or 0 by default if not present


#Total TC = O(n + q)
#Total SC = O(k)

# Call the main function
if __name__ == "__main__":
    main()