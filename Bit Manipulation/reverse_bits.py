def rev_bits(n):
    result = 0
    for i in range(32):
        # Extract the last bit of n and add it to the result
        result = (result << 1) | (n & 1)
        # Right shift n to process the next bit
        n >>= 1
    return result