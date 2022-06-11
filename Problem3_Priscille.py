#PROBLEM 3
def is_sum_equal_to_target(nums, target):

    for i in range(len(nums)):
    #print(f" {i}, {nums[i]}")
        for j in range(1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target: 
                return f" [{i} , {nums[i]}] "

print(is_sum_equal_to_target([2, 7, 11, 15], 9))