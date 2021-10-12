# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=false
# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary


# Sample Input
# 17

# Sample Output

#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001
    
def print_formatted(number):
    # your code goes here
    # loop starting from 1 to n
    for i in range(1, n+1):
        # will have bit_length of the biggest number n
        pad = n.bit_length()
        
        # print d, o, X, b in order with given length 
        print('{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}'.format(i, pad))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
    
    
