def missingNum(nums):
    n = len(nums)
    
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual

nums1 = [3, 0, 1]
print(missingNum(nums1))

nums2 = [0, 1]
print(missingNum(nums2))

nums3 = [9,6,4,2,3,5,7,0,1]
print(missingNum(nums3))