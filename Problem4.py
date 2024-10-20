def removeDup(nums):
    if len(nums) == 0:
        return 0
    k = 1
    
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    
    return k

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

k1 = removeDup(nums1)
k2 = removeDup(nums2)

print(k1)
print(nums1[:k1])

print(k2)
print(nums2[:k2])