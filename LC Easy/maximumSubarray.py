nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum, current_sum = 0, 0

for i in range(0, len(nums) - 1):
    current_sum = nums[i]
    max_sum = max(current_sum, max_sum)
    print(max_sum)
    # for j in range(i+1, len(nums)-1):max_sum = max(max_sum, current_sum)max_sum = max(max_sum, current_sum)max_sum = max(max_sum, current_sum)max_sum = max(max_sum, current_sum)max_sum = max(max_sum, current_sum)max_sum = max(max_sum, current_sum)max_sum = max(max_sum, current_sum)
    #     current_sum += nums[j]
    #     max_sum = max(max_sum, current_sum)

# print(max_sum)
