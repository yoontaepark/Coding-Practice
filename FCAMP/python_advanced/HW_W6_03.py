# 과제3.
# n개의 정수로 이루어진 리스트 nums와 정수 target이 주어졌을 때, nums에 있는 정수 4개를 합하여 target을 만들 수 있는 모든 조합을 구하시오. 
# 단, 정답에는 동일한 정수 조합이 여러개 포함되어서는 안된다.

# 예시 입력

# nums = [1, 0, -1, 0, -2, 2]
# target = 0
# 출력:

# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# https://kkminseok.github.io/posts/leetcode_4Sum/

def solution(nums, target):
    nums.sort()
    size = len(nums)
    res = []
    for i in range(size-3):
        if i==0 or (i>0 and nums[i] != nums[i-1]):
            for j in range(i+1,size-2):
                if j == i+1 or (j > i+1 and nums[j] != nums[j-1]) :
                    lo, hi, ts = j+1, size-1, target-(nums[i] +nums[j])
                    while lo < hi:
                        if nums[lo] + nums[hi] == ts :
                            res.append([nums[i],nums[j],nums[lo],nums[hi]])
                            while lo <hi and nums[lo] == nums[lo+1] :
                                lo+=1
                            while lo < hi and nums[hi] == nums[hi-1] : 
                                hi-=1
                            lo+=1
                            hi-=1
                        elif nums[lo] + nums[hi] < ts :
                            lo+=1
                        else:
                            hi-=1

    return res    

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(solution(nums, target))