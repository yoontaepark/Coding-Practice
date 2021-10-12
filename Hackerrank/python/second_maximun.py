# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
  
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # use set to delete duplicate and sorted function to sort values
    # then print [-2] since we are looking for second max
    # can't use .sort() since set is not accepting this function
    print(sorted(set(arr))[-2])
