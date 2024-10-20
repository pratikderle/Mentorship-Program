def verify(nums):
    n = len(nums)
    count_drops = 0

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]: 
            count_drops += 1
        
        if count_drops > 1:
            return False
    
    return True

nums1 = [3,4,5,1,2]
nums2 = [2,1,3,4]
nums3 = [1,2,3]

print(verify(nums1))  
print(verify(nums2))
print(verify(nums3))