# j = 0
# for i in range(len(nums)):
#    if nums[i] != 0:
#        nums[j],nums[i] = nums[i],nums[j]
#        j += 1
for i in nums:
    if i == 0:
        nums.remove(0)
        nums.append(0)