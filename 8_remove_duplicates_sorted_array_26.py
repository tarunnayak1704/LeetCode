def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l, nums

print(removeDuplicates([1,1,2,3,4,4,5,6,7,7,8]))