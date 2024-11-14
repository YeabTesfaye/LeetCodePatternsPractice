def longestOnes(nums, k) -> int:
    left = 0
    maxLength = 0
    zeroCount = 0
        
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroCount += 1
            
        while zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
            
        maxLength = max(maxLength, right - left + 1)
        
    return maxLength

        

# Test cases
print(longestOnes([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],2))  # Output: 6
print(longestOnes([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))  # Output: 9

