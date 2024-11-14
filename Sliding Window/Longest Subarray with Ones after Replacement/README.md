# Longest Subarray with Ones after Replacement - Solution

## Problem Description
Given a binary array `nums` and an integer `k`, the task is to find the longest contiguous subarray that can be obtained by replacing at most `k` `0`s with `1`s. The goal is to return the length of the longest subarray that contains at most `k` `0`s after flipping some of them to `1`s.

### Example

#### Example 1
- **Input:** `nums = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]`, `k = 2`
- **Output:** `6`
- **Explanation:** The longest subarray with at most 2 `0`s is `[1, 1, 0, 0, 0, 1]`.

#### Example 2
- **Input:** `nums = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]`, `k = 3`
- **Output:** `9`
- **Explanation:** The longest subarray with at most 3 `0`s is `[1, 0, 0, 1, 1, 0, 1, 1, 0]`.

## Approach

The solution uses the **Sliding Window** technique to maintain a window that contains at most `k` `0`s. The algorithm expands the window by moving the `right` pointer and adjusts the window by moving the `left` pointer whenever the count of `0`s exceeds `k`. This allows us to find the longest valid subarray.

### Steps:
1. **Initialize the Sliding Window**:
   - Use two pointers, `left` and `right`, to represent the window.
   - Maintain a counter `zeroCount` to keep track of the number of `0`s in the window.

2. **Expand the Window**:
   - Iterate through the array with the `right` pointer.
   - For each element at index `right`, if it is a `0`, increment the `zeroCount`.

3. **Shrink the Window**:
   - If `zeroCount` exceeds `k`, move the `left` pointer to the right until `zeroCount` becomes less than or equal to `k`.

4. **Update the Maximum Length**:
   - For each valid window (where `zeroCount <= k`), calculate the window size and update the maximum length found so far.

### Time Complexity:
- **O(n)**, where `n` is the length of the array. Both the `left` and `right` pointers traverse the array only once.

### Space Complexity:
- **O(1)**. The algorithm uses a constant amount of space for the `zeroCount`, `left`, and `maxLength` variables.

