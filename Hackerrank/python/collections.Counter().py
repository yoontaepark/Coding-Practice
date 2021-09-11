# collections.Counter()

# https://www.hackerrank.com/challenges/collections-counter/problem

# should import collections to use Counter function
import collections

# input number of shoes
numShoes = int(input())

# input shoes by using map function(will include all inputs in a row), and use Counter function
# Counter function creates a dictionary, which is {input1: # of input1, input2: # of input2...} 
# i.e input: 3 2 2 -> result: {3:1, 5:2}
shoes = collections.Counter(map(int, input().split()))

# input number of customers
numCust = int(input())

# initialize result, will print this as a final answer
earned = 0

# make a loop to check each customers
for i in range(numCust):
    # unpack values in size, price
    size, price = map(int, input().split())
    
    # if certain size of shoes is in stock
    if shoes[size]:
        # sell it and add to earned
        earned += price
        # also -1 for certain size of shoes stock
        shoes[size] -= 1
    
# after the loop, print total earned money
print(earned)
