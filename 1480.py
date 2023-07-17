# 07/15/2023 Author: Yaw Karikari Wiafe
# running_sums = []
# nums = [2,7,9,8]
# prev_sum = 0
# for i in range(len(nums)):
#     prev_sum += nums[i]
#     running_sums.append(prev_sum)

# print(running_sums)

#################################

nums = [3,1,2,10,1]
#Alternative solution
for i in range(1,len(nums)):
    nums[i]+=nums[i-1]

print(nums)
