# When you split, use double array to find its numbers
# so, res[5] gets error while res[0][5] doesn't get an error 

test = ['3 0 1 4 0 10', '0 2 8 0 5 9'] 

for testing in test:
    res = []
    res.append(testing.split(' '))
    print(res[0][0])
