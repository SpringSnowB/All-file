def find_target(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target and nums[i] != nums[j]:
                return [i,j]


nums = [2, 7, 11, 15]
target = 9
print(find_target(nums,target))