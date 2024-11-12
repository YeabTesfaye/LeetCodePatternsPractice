def minSubArrayLen(target, nums):
    curr_sum = 0  
    min_length = float("inf")  
    left = 0  

    for right in range(len(nums)):
        curr_sum += nums[right]  # Add the current element to the window sum

        # Shrink the window from the left as long as the sum is >= target
        while curr_sum >= target:
            min_length = min(min_length, right - left + 1) 
            curr_sum -= nums[left] 
            left += 1  

    # If no valid subarray was found, return 0, otherwise return the min length
    return min_length if min_length != float("inf") else 0


# Example usage
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))  # Output: 2
