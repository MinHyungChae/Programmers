def solution(n):
    bin_n = bin(n)[2:]
    bin_count = str(bin_n).count('1')
    
    big = n+1
    while True:
        bin_big = bin(big)[2:]
        bin_big_count = str(bin_big).count('1')
        
        if bin_big_count == bin_count:
            return big
        else:
            big += 1