# Minimum Size Subarray Sum

## Problem Description

Given an integer array `nums` of size `n` and an integer `target`, find the minimal length of a contiguous subarray such that the sum of the subarray is greater than or equal to `target`. If no such subarray exists, return 0.

### Example

#### Example 1:
- **Input**: `target = 7`, `nums = [2, 3, 1, 2, 4, 3]`
- **Output**: `2`
- **Explanation**: The subarray `[4, 3]` has a sum of `7`, which is greater than or equal to `7`, and its length is `2`.

#### Example 2:
- **Input**: `target = 4`, `nums = [1, 4, 4]`
- **Output**: `1`
- **Explanation**: The subarray `[4]` has a sum of `4`, which is equal to the target, and its length is `1`.

#### Example 3:
- **Input**: `target = 11`, `nums = [1, 1, 1, 1, 1, 1, 1, 1]`
- **Output**: `0`
- **Explanation**: No subarray has a sum greater than or equal to `11`, so the answer is `0`.

## Approach

We use the **sliding window** technique to efficiently solve this problem:
1. Expand the window by iterating through the array with the `right` pointer and updating the sum (`curr_sum`) as we include new elements.
2. Once the sum of the current window is greater than or equal to the target, try to shrink the window from the left by incrementing the `left` pointer while maintaining the sum condition. This allows us to find the smallest possible subarray length.
3. Track the minimum length of such valid subarrays.
